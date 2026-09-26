import random
import json
import math
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # 💡 FIXED: Missing import explicitly declared here!
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum, Q, Min
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from .models import Player, GolfRound, Hole, Squad, HoleScore, PayoutSetting
from .forms import ScoringMemberRegistrationForm, ManualSquadForm, PayoutRulesForm
from collections import defaultdict


def chicago_points_from_scores(played_scores):
    """Sum Chicago points from hole scores (eagle+ 8, birdie 4, par 2, bogey 1)."""
    total = 0
    for score in played_scores:
        if score.gross_value is None or score.gross_value <= 0:
            continue
        relation_to_par = score.gross_value - score.hole.par
        if relation_to_par <= -2:
            total += 8
        elif relation_to_par == -1:
            total += 4
        elif relation_to_par == 0:
            total += 2
        elif relation_to_par == 1:
            total += 1
    return total


def adjust_18_chicago_quota_for_player(player, played_scores):
    """
    Update player.chicago_points_18 for next round from today's +/- vs quota.
    Moves quota by half the differential (same rule as finalize_tournament_round).
    Returns (old_quota, new_quota, differential) or None if no scores.
    """
    scores = list(played_scores.select_related('hole')) if hasattr(played_scores, 'select_related') else list(played_scores)
    if not scores:
        return None

    points_earned = chicago_points_from_scores(scores)
    hcp = player.handicap or 0
    current_quota = player.chicago_points_18 if (
                player.chicago_points_18 and player.chicago_points_18 > 0) else max(39 - hcp, 2)
    differential = points_earned - current_quota
    new_quota = max(2, min(54, current_quota + (differential // 2)))
    player.chicago_points_18 = new_quota
    player.save(update_fields=['chicago_points_18'])
    return current_quota, new_quota, differential


def apply_18_chicago_quota_updates(active_round):
    """Adjust next-round 18-hole Chicago quotas for every player who scored in this round."""
    updated = []
    player_ids = HoleScore.objects.filter(
        round=active_round, gross_value__gt=0
    ).values_list('player_id', flat=True).distinct()

    for player in Player.objects.filter(id__in=player_ids):
        played = HoleScore.objects.filter(round=active_round, player=player, gross_value__gt=0)
        result = adjust_18_chicago_quota_for_player(player, played)
        if result:
            updated.append((player, result))
    return updated


def adjust_ladies_handicap_for_player(player, played_scores):
    """
    Update player.ladies_league_handicap for next round from today's net vs par.
    Same rule as reset_tournament_action: -1 if net < -1 to par, +1 if net > +2 to par.
    Returns (old_hcp, new_hcp, net_differential) or None if no scores.
    """
    scores = list(played_scores.select_related('hole')) if hasattr(played_scores, 'select_related') else list(played_scores)
    if not scores:
        return None

    total_gross = sum(s.gross_value for s in scores if s.gross_value)
    total_par = sum(s.hole.par for s in scores)
    current_hcp = player.ladies_league_handicap or 0
    # 9-hole outing: apply half of stored ladies handicap as stroke allowance
    actual_net_strokes = total_gross - (current_hcp / 2.0)
    net_differential = actual_net_strokes - total_par

    if net_differential < -1:
        adjusted_hcp = current_hcp - 1
    elif net_differential > 2:
        adjusted_hcp = current_hcp + 1
    else:
        adjusted_hcp = current_hcp

    new_hcp = max(0, int(round(adjusted_hcp)))
    player.ladies_league_handicap = new_hcp
    player.save(update_fields=['ladies_league_handicap'])
    return current_hcp, new_hcp, net_differential


def apply_womens_handicap_updates(active_round):
    """Adjust next-round ladies_league_handicap for every player who scored in this round."""
    updated = []
    player_ids = HoleScore.objects.filter(
        round=active_round, gross_value__gt=0
    ).values_list('player_id', flat=True).distinct()

    for player in Player.objects.filter(id__in=player_ids):
        played = HoleScore.objects.filter(round=active_round, player=player, gross_value__gt=0)
        result = adjust_ladies_handicap_for_player(player, played)
        if result:
            updated.append((player, result))
    return updated


def adjust_mens_handicap_for_player(player, played_scores):
    """
    Update player.handicap for next round from today's net vs course par.
    Rule: new_hcp = old_hcp + (net_score - par) * 0.8, clamped 0–36.
    """
    scores = list(played_scores.select_related('hole')) if hasattr(played_scores, 'select_related') else list(played_scores)
    if not scores:
        return None

    total_gross = sum(int(s.gross_value) for s in scores if s.gross_value)
    course_par = sum(int(s.hole.par) for s in scores)
    old_hcp = int(player.handicap or 0)
    net_score = total_gross - old_hcp
    score_differential = net_score - course_par
    new_hcp = max(0, min(36, int(round(old_hcp + (score_differential * 0.8)))))
    player.handicap = new_hcp
    player.save(update_fields=['handicap'])
    return old_hcp, new_hcp, score_differential


def apply_mens_handicap_updates(active_round):
    """Recalculate and save handicap for every player who scored in this men's league round."""
    updated = []
    player_ids = HoleScore.objects.filter(
        round=active_round, gross_value__gt=0
    ).values_list('player_id', flat=True).distinct()

    for player in Player.objects.filter(id__in=player_ids):
        played = HoleScore.objects.filter(round=active_round, player=player, gross_value__gt=0)
        result = adjust_mens_handicap_for_player(player, played)
        if result:
            updated.append((player, result))
    return updated


def handicap_strokes_on_hole(player, hole):
    """USGA-style strokes received on a hole from full 18-hole handicap."""
    hcp = int(player.handicap or 0)
    idx = int(hole.handicap_index or 18)
    if hcp <= 0:
        return 0
    strokes = 0
    if idx <= hcp:
        strokes = 1
    if hcp > 18 and idx <= (hcp - 18):
        strokes = 2
    return strokes


def compute_round_skins(active_round, use_net=True):
    """
    Solo low-score skins by hole (ties = no skin that hole).
    Men's league uses net (gross − handicap strokes); otherwise gross.
    """
    skins_found = []
    if not active_round:
        return skins_found

    for hole in Hole.objects.all().order_by('hole_number'):
        hole_scores = list(
            HoleScore.objects.filter(
                round=active_round, hole=hole, gross_value__gt=0
            ).select_related('player')
        )
        if not hole_scores:
            continue

        scored = []
        for record in hole_scores:
            strokes = handicap_strokes_on_hole(record.player, hole) if use_net else 0
            net = int(record.gross_value) - strokes
            scored.append({
                'record': record,
                'gross': int(record.gross_value),
                'strokes': strokes,
                'net': net,
            })

        key = 'net' if use_net else 'gross'
        best = min(row[key] for row in scored)
        contenders = [row for row in scored if row[key] == best]
        if len(contenders) == 1:
            win = contenders[0]
            skins_found.append({
                'hole_number': hole.hole_number,
                'par': hole.par,
                'winner': win['record'].player,
                'score': win['gross'],
                'net_score': win['net'],
                'strokes': win['strokes'],
            })
    return skins_found


def format_skins_winners_html(skins_found, skins_pool=0):
    """
    Build leaderboard HTML summarizing skins by player with cash winnings.
    Each skin is worth skins_pool / total_skins_won (rounded to whole dollars).
    """
    if not skins_found:
        return "", []

    from collections import OrderedDict
    by_player = OrderedDict()
    for skin in skins_found:
        name = skin['winner'].name
        by_player.setdefault(name, [])
        by_player[name].append(skin['hole_number'])

    total_skins = len(skins_found)
    pool = float(skins_pool or 0)
    per_skin = (pool / total_skins) if total_skins > 0 else 0.0

    payout_rows = []
    lines = []
    for name, holes in by_player.items():
        hole_list = ", ".join(str(h) for h in holes)
        count = len(holes)
        winnings = int(round(per_skin * count, 0))
        label = "skin" if count == 1 else "skins"
        hole_word = "Hole" if count == 1 else "Holes"
        lines.append(
            f"<div style='margin-bottom:6px;'>"
            f"<strong>{name}</strong> - {count} {label} "
            f"({hole_word} {hole_list})"
            f"<span style='float:right; color:#e65100;'>${winnings}</span>"
            f"<div style='clear:both;'></div>"
            f"</div>"
        )
        payout_rows.append({
            'name': name,
            'skins': count,
            'holes': holes,
            'winnings': winnings,
        })

    per_skin_rounded = int(round(per_skin, 0))
    footer = (
        f"<div style='margin-top:8px; padding-top:6px; border-top:1px dashed #ffe082; "
        f"font-size:12px; font-weight:normal; color:#ff8f00;'>"
        f"{total_skins} skins won &middot; ${per_skin_rounded} per skin"
        f"</div>"
    )
    return "".join(lines) + footer, payout_rows


def adjust_9_team_chicago_quota_for_player(player, played_scores):
    """
    After a 9-hole Team Chicago round, adjust the player's 18-hole Chicago quota
    (source of truth). 9-hole points needed is always ceil(chicago_points_18 / 2).
    Moves 18-hole quota by the same half-differential rule used elsewhere.
    """
    scores = list(played_scores.select_related('hole')) if hasattr(played_scores, 'select_related') else list(played_scores)
    if not scores:
        return None

    points_earned = chicago_points_from_scores(scores)
    current_9 = _team_chicago_quota(player)
    differential = points_earned - current_9

    hcp = int(player.handicap or 0)
    current_18 = int(player.chicago_points_18 or 0)
    if current_18 <= 0:
        current_18 = max(39 - hcp, 2)

    # Half the 9-hole differential applied to the 18-hole source quota
    new_18 = max(2, min(54, current_18 + (differential // 2)))
    player.chicago_points_18 = new_18
    player.team_chicago_points_9 = max(1, math.ceil(new_18 / 2))
    player.save(update_fields=['chicago_points_18', 'team_chicago_points_9'])
    return current_9, player.team_chicago_points_9, differential


def apply_9_team_chicago_quota_updates(active_round):
    """Adjust next-round Chicago quotas after a 9-hole Team Chicago round."""
    updated = []
    player_ids = HoleScore.objects.filter(
        round=active_round, gross_value__gt=0
    ).values_list('player_id', flat=True).distinct()

    for player in Player.objects.filter(id__in=player_ids):
        played = HoleScore.objects.filter(round=active_round, player=player, gross_value__gt=0)
        result = adjust_9_team_chicago_quota_for_player(player, played)
        if result:
            updated.append((player, result))
    return updated


@csrf_exempt
@login_required
def update_score_ajax(request):
    if request.method == "POST":
        try:
            round_id = request.POST.get('round_id')
            player_id = request.POST.get('player_id')
            hole_id = request.POST.get('hole_id')
            strokes_val = request.POST.get('strokes') or "0"

            if not player_id or not hole_id:
                return JsonResponse({'status': 'failed', 'error': 'Missing identity parameters'}, status=400)

            gross_strokes = int(strokes_val) if (strokes_val and strokes_val.isdigit()) else 0
            player = get_object_or_404(Player, id=player_id)
            hole = get_object_or_404(Hole, id=hole_id)

            active_round = None
            if round_id and round_id.isdigit():
                active_round = GolfRound.objects.filter(id=round_id).first()
            if not active_round:
                active_round = GolfRound.objects.filter(is_active=True).first()

            # Save or update your 'HoleScore' table record row
            score_record, created = HoleScore.objects.get_or_create(
                round=active_round,
                player=player,
                hole=hole
            )

            # 1. Commit the raw gross strokes directly to your column
            score_record.gross_value = gross_strokes

            # 2. CHICAGO POINTS ALGORITHM RULE SYSTEM
            if gross_strokes > 0:
                hole_par = hole.par or 4  # Default fallback to Par 4 if missing
                score_relative_to_par = gross_strokes - hole_par

                # Strict Chicago tournament point allocation criteria rules mapping
                if score_relative_to_par == -3:
                    chicago_points = 6  # Albatross / Double Eagle
                elif score_relative_to_par == -2:
                    chicago_points = 4  # Eagle
                elif score_relative_to_par == -1:
                    chicago_points = 2  # Birdie
                elif score_relative_to_par == 0:
                    chicago_points = 0  # Par
                elif score_relative_to_par == 1:
                    chicago_points = -1  # Bogey
                else:
                    chicago_points = -2  # Double Bogey or Worse (including picking up ball)

                # Commit point variables straight into your net_value storage block
                score_record.net_value = chicago_points
            else:
                score_record.net_value = 0  # Default state for skipped or unplayed holes

            score_record.save()

            return JsonResponse({
                'status': 'success',
                'current_strokes': score_record.gross_value
            })

        except Exception as e:
            return JsonResponse({'status': 'failed', 'error': str(e)}, status=400)

    return JsonResponse({'status': 'failed', 'message': 'Invalid HTTP request method'}, status=400)


@login_required
def player_round_summary(request):
    active_round = GolfRound.objects.filter(is_active=True).first()
    player_profile = Player.objects.filter(user=request.user).first()
    squad = Squad.objects.filter(round=active_round, players=player_profile).first()

    summary_data = []
    if squad:
        for player in squad.players.all():
            stats = HoleScore.objects.filter(round=active_round, player=player).aggregate(
                total_gross=Sum('gross_value'),
                total_net=Sum('net_value')
            )
            g_total = stats['total_gross'] or 0
            n_total = stats['total_net'] or 0

            if "CHICAGO" in active_round.game_format:
                chicago_quota = 39 - player.handicap
                final_display_metric = n_total - chicago_quota
                metric_label = f"Chicago Points: {n_total} (Net: {'+' if final_display_metric >= 0 else ''}{final_display_metric})"
            else:
                metric_label = f"Gross: {g_total} | Net: {n_total}"

            summary_data.append({'player': player, 'metric_label': metric_label})

    context = {'squad': squad, 'summary': summary_data}
    return render(request, 'scorecard/player_summary.html', context)


# @login_required
def admin_dashboard(request):
    # Manual administrative authentication security shield block
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('/login/')

    # Look for the active round row (auto-creates if missing)
    active_round = GolfRound.objects.filter(is_active=True).first()
    if not active_round:
        active_round = GolfRound.objects.create(
            course_name="PRGC Championship Course",
            is_active=True,
            game_format=""
        )

    # -------------------------------------------------------------
    # INTERACTIVE FORM PROCESSOR MATRIX (Preserved Exactly)
    # -------------------------------------------------------------
    if request.method == 'POST':
        action = request.POST.get('action')

        # 1. Handle format switching selection dropdowns
        if action == 'change_format':
            new_format = request.POST.get('game_format')
            if active_round and new_format:
                active_round.game_format = new_format
                active_round.save(update_fields=['game_format'])
                messages.success(request, f"Active format changed to: {new_format}")
                return redirect('/admin-dashboard/')

        # 2. Handle real-time player check-in status toggles
        elif action == 'toggle_player':
            toggle_id = request.POST.get('toggle_player_id')
            if toggle_id:
                target_player = get_object_or_404(Player, id=toggle_id)
                target_player.is_playing_today = not target_player.is_playing_today

                # If they are being unchecked (benched), clear their cart pairing too
                if not target_player.is_playing_today and target_player.riding_partner:
                    partner = target_player.riding_partner
                    partner.riding_partner = None
                    partner.save(update_fields=['riding_partner'])
                    target_player.riding_partner = None

                target_player.save(update_fields=['is_playing_today', 'riding_partner'])
                return redirect('/admin-dashboard/')

        # ━ 🟢 NEW ACTION: PAIR UP RIDERS BEFORE SQUAD GENERATION ━
        elif action == 'assign_cart':
            player_id = request.POST.get('player_id')
            partner_id = request.POST.get('partner_id')  # Empty string means "Ride Solo"

            if player_id:
                player = get_object_or_404(Player, id=player_id)

                # Break old links for this player
                if player.riding_partner:
                    old_p = player.riding_partner
                    old_p.riding_partner = None
                    old_p.save(update_fields=['riding_partner'])
                player.riding_partner = None
                player.save(update_fields=['riding_partner'])

                # If pairing with someone, establish 2-way symmetrical link
                if partner_id:
                    partner = get_object_or_404(Player, id=partner_id)

                    # Break new partner's old links if they were paired elsewhere
                    if partner.riding_partner:
                        old_p2 = partner.riding_partner
                        old_p2.riding_partner = None
                        old_p2.save(update_fields=['riding_partner'])

                    player.riding_partner = partner
                    player.save(update_fields=['riding_partner'])
                    partner.riding_partner = player
                    partner.save(update_fields=['riding_partner'])
                    messages.success(request, f"🚙 Cart Link Saved: {player.name} & {partner.name}")
                else:
                    messages.success(request, f"Cleared cart link for {player.name}")

                return redirect('/admin-dashboard/')

        # -------------------------------------------------------------
    # GATHER DATA FOR RENDERING
    # -------------------------------------------------------------
    is_womens_league = False
    fmt = str(active_round.game_format or '').strip() if active_round else ''
    if fmt == '9_WOMENS_LEAGUE':
        is_womens_league = True

    is_scramble = fmt == '9_HOLE_SCRAMBLE'
    is_team_chicago = fmt in ('9_TEAM_CHICAGO', 'team_chicago_points_9')
    is_pairing_format = is_scramble or is_team_chicago

    active_squads = []
    assigned_captain_ids = []
    taken_hole_ids = []
    assigned_player_ids = []  # 🟢 NEW TRACKER ARRAY

    if active_round:
        active_squads = Squad.objects.filter(round=active_round).select_related(
            'scorekeeper', 'starting_hole'
        ).prefetch_related('players').order_by('squad_number')

        assigned_captain_ids = [s.scorekeeper.id for s in active_squads if s.scorekeeper]
        taken_hole_ids = [s.starting_hole.id for s in active_squads if s.starting_hole]

        # 🟢 COLLECT EVERY SINGLE PLAYER ALREADY PLACED ON A SQUAD (Captains + Teammates)
        for squad in active_squads:
            assigned_player_ids.extend(squad.players.values_list('id', flat=True))
            if is_team_chicago:
                squad.team_quota_total = sum(
                    _team_chicago_quota(p) for p in squad.players.all()
                )

    # 👥 UPGRADED DYNAMIC VIEWS FILTER: Exclude ANY player who already has a squad slot!
    checked_in_players = Player.objects.filter(is_playing_today=True).exclude(id__in=assigned_player_ids).order_by(
        'name')
    all_players = Player.objects.all().order_by('name')
    available_holes = Hole.objects.filter(hole_number__lte=9).exclude(id__in=taken_hole_ids).order_by('hole_number')

    # ... keep your math definitions exactly as they are below ...
    total_playing = Player.objects.filter(is_playing_today=True).count()
    squad_size_target = request.GET.get('team_size', '4')
    squad_size = int(squad_size_target) if squad_size_target.isdigit() else 4

    captains_needed = math.ceil(total_playing / squad_size) if total_playing > 0 else 0
    current_captains = Player.objects.filter(is_playing_today=True, is_captain=True).count()
    captain_difference = captains_needed - current_captains

    context = {
        'round': active_round, 'players': all_players, 'checked_in_players': checked_in_players,
        'is_womens_league': is_womens_league, 'active_squads': active_squads, 'available_holes': available_holes,
        'total_playing_count': total_playing, 'squad_size': squad_size, 'captains_needed': captains_needed,
        'current_captains_count': current_captains, 'captain_difference': captain_difference,
        'abs_captain_difference': abs(captain_difference),
        'is_scramble': is_scramble,
        'is_team_chicago': is_team_chicago,
        'is_pairing_format': is_pairing_format,
    }
    # Drain flash messages so admin action notes never clutter the dashboard UI
    list(get_messages(request))
    return render(request, 'scorecard/admin_dashboard.html', context)


@staff_member_required
def generate_squads_action(request):
    if request.method == "POST":
        active_round = GolfRound.objects.filter(is_active=True).first()
        if not active_round:
            active_round = GolfRound.objects.create(course_name="PRGC Championship Course", is_active=True)

        chosen_format = request.POST.get('game_format')
        if chosen_format:
            active_round.game_format = chosen_format
            active_round.save()

        Squad.objects.filter(round=active_round).delete()

        # CHANGED: Pulls exclusively the checked-in active players
        all_players = list(Player.objects.filter(is_playing_today=True))
        random.shuffle(all_players)

        course_holes = list(Hole.objects.all().order_by('hole_number'))
        squad_size = 5
        squad_index = 1
        hole_iterator = 0

        for chunk_start in range(0, len(all_players), squad_size):
            player_chunk = all_players[chunk_start: chunk_start + squad_size]
            assigned_hole = course_holes[hole_iterator % len(course_holes)]

            new_squad = Squad.objects.create(round=active_round, squad_number=squad_index, starting_hole=assigned_hole)
            new_squad.players.add(*player_chunk)

            # FIXED: Assigns the FIRST individual player from the list to be the scorekeeper
            if player_chunk:
                new_squad.scorekeeper = player_chunk[0]
                new_squad.save()

            squad_index += 1
            hole_iterator += 1

    return redirect('scorecard:admin_dashboard')


@staff_member_required
def reset_tournament_action(request):
    if request.method == "POST":
        # 1. Locate the current active round configuration row
        old_active_round = GolfRound.objects.filter(is_active=True).first()

        if old_active_round:
            # Detect what tournament league format was active today
            is_womens_9 = old_active_round.game_format == "9_WOMENS_LEAGUE"

            # 2. AUTOMATED HANDICAP FINALIZATION BACKEND SCANNERS ENGINE
            assigned_player_ids = HoleScore.objects.filter(round=old_active_round).values_list('player_id', flat=True)
            active_players = Player.objects.filter(
                Q(is_playing_today=True) | Q(id__in=assigned_player_ids)
            ).distinct()

            # Open scorecard/views.py and update the inner player loop inside reset_tournament_action:

            for player in active_players:
                played_scores = HoleScore.objects.filter(round=old_active_round, player=player, gross_value__gt=0)
                holes_played = played_scores.count()

                if holes_played > 0:
                    stats = played_scores.aggregate(g_sum=Sum('gross_value'))
                    total_gross_strokes = stats['g_sum'] or 0

                    played_hole_ids = played_scores.values_list('hole_id', flat=True)
                    total_par_played = Hole.objects.filter(id__in=played_hole_ids).aggregate(Sum('par'))[
                                           'par__sum'] or 0

                    # 🟢 CHOOSE CALCULATION METHOD & DB FIELD BASED ON ACTIVE FORMAT
                    if old_active_round.game_format == "9_WOMENS_LEAGUE":
                        adjust_ladies_handicap_for_player(player, played_scores)

                    elif old_active_round.game_format in ("18_IND_CHICAGO", "chicago_points_18"):
                        adjust_18_chicago_quota_for_player(player, played_scores)

                    elif old_active_round.game_format == "9_TEAM_CHICAGO":
                        adjust_9_team_chicago_quota_for_player(player, played_scores)

                    elif old_active_round.game_format in ("18_HOLE_MENS_LEAGUE", "18_GROSS_NET"):
                        adjust_mens_handicap_for_player(player, played_scores)

                    else:
                        # Fallback stroke-play step adjustment
                        current_hcp = player.handicap or 0
                        actual_net_strokes = total_gross_strokes - (current_hcp * (holes_played / 18.0))
                        net_differential = actual_net_strokes - total_par_played
                        adjusted_hcp = current_hcp - 2 if net_differential < -2 else (
                            current_hcp - 1 if net_differential < 0 else (
                                current_hcp + 1 if net_differential > 3 else current_hcp))
                        player.handicap = max(0, int(round(adjusted_hcp)))
                        player.save(update_fields=['handicap'])

            # 3. HOUSEKEEPING & ARCHIVING OPERATIONS
            # Delete all recorded scores tied to this specific old match session container
            HoleScore.objects.filter(round=old_active_round).delete()

            # Clear out squad configuration groups for this old session
            Squad.objects.filter(round=old_active_round).delete()

            # Deactivate and archive the old round out of active tracking spaces
            old_active_round.is_active = False
            old_active_round.save(update_fields=['is_active'])

        # 4. START FRESH TOURNAMENT GAME PROFILE AUTOMATION
        new_round = GolfRound.objects.create(
            course_name="PRGC Championship Course",
            is_active=True,
            game_format=""  # Kept as clean string to satisfy MySQL NOT NULL constraints safely
        )

        # Uncheck player checkboxes back to default benched empty positions
        Player.objects.all().update(is_playing_today=False)

        messages.success(
            request,
            f"🏁 Round finalized! New handicaps applied to player profiles. Fresh Tournament Session ID #{new_round.id} initiated successfully."
        )
        return redirect('scorecard:admin_dashboard')

    return redirect('scorecard:admin_dashboard')


@staff_member_required
def add_player_action(request):
    if request.method == "POST":
        player_name = request.POST.get('player_name', '').strip()
        handicap_str = request.POST.get('handicap', 0)
        handicap = int(handicap_str) if (handicap_str and str(handicap_str).isdigit()) else 0

        if player_name:
            safe_username = "".join(x for x in player_name.lower() if x.isalnum())
            suffix = 1
            final_username = safe_username

            while User.objects.filter(username=final_username).exists():
                final_username = f"{safe_username}{suffix}"
                suffix += 1

            new_user = User.objects.create_user(
                username=final_username,
                password="prgcplayer123!"
            )

            Player.objects.create(
                user=new_user,
                name=player_name,
                handicap=handicap,
                member_id=f"M-{new_user.id:04d}"
            )

        return redirect('scorecard:admin_dashboard')


@staff_member_required
def update_handicap_ajax(request):
    if request.method == "POST":
        player_id = request.POST.get('player_id')
        handicap_str = request.POST.get('handicap', 0)
        player = get_object_or_404(Player, id=player_id)

        player.handicap = int(handicap_str) if (handicap_str and str(handicap_str).isdigit()) else 0
        player.save()

        return JsonResponse({'status': 'success', 'new_handicap': player.handicap})

    return JsonResponse({'status': 'error'}, status=400)


@login_required
def fetch_latest_scores_ajax(request, hole_number):
    active_round = GolfRound.objects.filter(is_active=True).first()
    player_profile = Player.objects.filter(user=request.user).first()
    squad = Squad.objects.filter(round=active_round, players=player_profile).first()
    current_hole = get_object_or_404(Hole, hole_number=hole_number)
    updated_scores = []

    if squad:
        for player in squad.players.all():
            score_record, _ = HoleScore.objects.get_or_create(
                round=active_round,
                player=player,
                hole=current_hole
            )

            updated_scores.append({
                'player_id': player.id,
                'strokes': score_record.gross_value,
                'net_score': score_record.net_value if score_record.gross_value > 0 else "-",
                'handicap': player.handicap
            })

    return JsonResponse({'status': 'success', 'scores': updated_scores})


def login_view(request):
    error_message = None

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # STAFF REDIRECT: Send managers straight to the control panel
            if user.is_staff:
                return redirect('scorecard:admin_dashboard')

            # PLAYER REDIRECT: Look up player context mappings
            active_round = GolfRound.objects.filter(is_active=True).first()
            player = None

            try:
                player = Player.objects.get(user=user)
            except Player.DoesNotExist:
                player = Player.objects.filter(name__icontains=user.first_name).filter(
                    name__icontains=user.last_name).first()

            if player and active_round:
                player_squad = Squad.objects.filter(round=active_round, players=player).first()
                if player_squad and player_squad.starting_hole:
                    start_hole_num = player_squad.starting_hole.hole_number

                    # 🟢 NEW SEPARATE REDIRECT FOR SCRAMBLE TO AVOID LOGIC POLLUTION
                    if str(active_round.game_format).strip() == "9_HOLE_SCRAMBLE":
                        return redirect('scorecard:player_scorecard_scramble', hole_number=start_hole_num)

                    # Standard individual, men's league, and Chicago fallback remains untouched
                    return redirect('scorecard:player_scorecard', hole_number=start_hole_num)

            # Fallback for valid user accounts with no active group assignment
            return redirect('scorecard:player_scorecard_start')
        else:
            # Rejection statement if password/username lookup fails authentication
            error_message = "Invalid username or password. Please try again."

    # CRUCIAL: This return statement must be flush with the main function block level!
    # It catches all GET requests AND all failed POST requests.
    return render(request, 'scorecard/login.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('scorecard:login_view')


def register_view(request):
    if request.method == 'POST':
        form = ScoringMemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect straight back to your dashboard instead of player_list
            return redirect('scorecard:admin_dashboard')
    else:
        form = ScoringMemberRegistrationForm()

    return render(request, 'scorecard/register_player.html', {'form': form})


def view_all_members(request):
    players = Player.objects.all().order_by('name')
    return render(request, 'scorecard/all_members.html', {'players': players})  # <-- Sent as 'players'


@csrf_exempt
def toggle_playing_status_ajax(request):
    if request.method == 'POST':
        try:
            # Explicitly decode the raw incoming byte array to a clean string format
            body_unicode = request.body.decode('utf-8')
            data = json.loads(body_unicode)

            player_id = data.get('player_id')
            is_playing = data.get('is_playing')

            player = get_object_or_404(Player, id=player_id)
            player.is_playing_today = is_playing
            player.save(update_fields=['is_playing_today'])

            return JsonResponse({'status': 'success', 'is_playing_today': player.is_playing_today})
        except Exception as e:
            return JsonResponse({'status': 'failed', 'error': str(e)}, status=400)

    return JsonResponse({'status': 'failed', 'message': 'Invalid method'}, status=400)


@require_POST  # Ensures players can only be deleted via a POST request for security
def delete_player_action(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    player.delete()
    return redirect('scorecard:all_members')


def edit_player_view(request, player_id):
    player = get_object_or_404(Player, id=player_id)

    if request.method == 'POST':
        # Pass instance=player so it updates the existing record instead of creating a new one
        form = ScoringMemberRegistrationForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('scorecard:all_members')
    else:
        # Pre-fill form fields by extracting individual tokens out of your combined name column string
        name_parts = player.name.split(' ', 1)
        first_name = name_parts[0] if len(name_parts) > 0 else ""
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        form = ScoringMemberRegistrationForm(instance=player, initial={
            'first_name': first_name,
            'last_name': last_name
        })

    return render(request, 'scorecard/edit_player.html', {'form': form, 'player': player})


def resolve_player_for_user(user):
    """Map a logged-in User to their Player profile (FK, then name/username fallbacks)."""
    if not user or not user.is_authenticated:
        return None
    player = Player.objects.filter(user=user).first()
    if player:
        return player

    # Name-based fallbacks for accounts that were never linked
    if user.first_name and user.last_name:
        full = f"{user.first_name} {user.last_name}".strip()
        player = Player.objects.filter(name__iexact=full).first()
        if not player:
            player = Player.objects.filter(
                name__icontains=user.first_name
            ).filter(name__icontains=user.last_name).first()
        if player:
            if player.user_id is None:
                player.user = user
                player.save(update_fields=['user'])
            return player

    if user.username:
        player = Player.objects.filter(name__icontains=user.username).first()
        if player and player.user_id is None:
            player.user = user
            player.save(update_fields=['user'])
            return player
    return None


# @login_required
def player_scorecard(request, hole_number=None):
    # 🟢 Section 1 Initialization Block: Safeguards against local unbound scope compilation failures
    if not request.user.is_authenticated:
        return redirect('/login/')

    active_round = GolfRound.objects.filter(is_active=True).first()

    # Scramble uses its own captain-entry scorecard (roster + single team stroke input)
    if active_round and str(active_round.game_format or '').strip() == '9_HOLE_SCRAMBLE':
        return player_scorecard_scramble_view(request, hole_number=hole_number if hole_number is not None else 1)

    squad_players = []
    player_scores = []
    active_squad = None
    is_final_hole = False
    is_chicago_game = False
    is_womens_league = False
    is_scramble_game = False
    game_format = ""
    is_scorecard_editable = True
    squad_cumulative_to_par = 0

    # Globally define these variables at startup to prevent NameErrors on Finish Round branches
    squad_total_points_needed = 0
    squad_running_total_earned = 0

    # AUTOMATED SHOTGUN STARTING HOLE INTERCEPTOR ENGINE
    if hole_number is None and active_round:
        current_player = resolve_player_for_user(request.user)

        if current_player:
            active_squad = Squad.objects.filter(round=active_round, players=current_player).first()
            if active_squad and active_squad.starting_hole:
                shotgun_tee = active_squad.starting_hole.hole_number
                return redirect('scorecard:player_scorecard', hole_number=shotgun_tee)

    if hole_number is None:
        hole_number = 1

    try:
        hole_number = int(hole_number)
    except (ValueError, TypeError):
        hole_number = 1

    hole = get_object_or_404(Hole, hole_number=hole_number)
    next_hole = hole_number + 1 if hole_number < 18 else 1
    prev_hole = hole_number - 1 if hole_number > 1 else 18

    if active_round:
        raw_game_format = str(active_round.game_format or '')
        game_format = raw_game_format.strip()

        is_chicago_game = game_format in ["chicago_points_18", "team_chicago_points_9", "18_IND_CHICAGO",
                                          "9_TEAM_CHICAGO", "9_WOMENS_LEAGUE"]
        is_team_chicago = game_format in ["team_chicago_points_9", "9_TEAM_CHICAGO"]
        is_womens_league = game_format == "9_WOMENS_LEAGUE"
        is_scramble_game = game_format == "9_HOLE_SCRAMBLE"

        current_player = resolve_player_for_user(request.user)
        if current_player:
            active_squad = Squad.objects.filter(round=active_round, players=current_player).first()

            is_scorecard_editable = True

            # 🟢 FIXED: Checks if the user is the round-specific scorekeeper (Designated Captain)
            # instead of reading a permanent registration box on their member profile.
            if is_scramble_game:
                if active_squad:
                    if active_squad.scorekeeper != current_player and not request.user.is_staff:
                        is_scorecard_editable = False
                else:
                    is_scorecard_editable = False

            if active_squad and active_squad.starting_hole:
                start_h = active_squad.starting_hole.hole_number

                if is_scramble_game or is_womens_league or is_team_chicago:
                    full_tournament_route = list(range(start_h, 10)) + list(range(1, start_h))
                else:
                    front_seq = list(range(start_h, 10)) + list(range(1, start_h))
                    back_seq = list(range(start_h + 9, 19)) + list(range(10, start_h + 9))
                    full_tournament_route = front_seq + back_seq

                try:
                    current_index = full_tournament_route.index(hole_number)
                    route_limit_length = 9 if (is_team_chicago or is_womens_league or is_scramble_game) else len(
                        full_tournament_route)

                    if current_index == route_limit_length - 1:
                        is_final_hole = True

                    if current_index < route_limit_length - 1:
                        next_hole = full_tournament_route[current_index + 1]
                    else:
                        next_hole = full_tournament_route

                    if current_index > 0:
                        prev_hole = full_tournament_route[current_index - 1]
                    else:
                        prev_hole = full_tournament_route[route_limit_length - 1]
                except ValueError:
                    pass
            # HANDLE POST DATA SCORE SUBMISSIONS & SAVING
            if request.method == 'POST' and is_scorecard_editable:
                if active_squad:
                    squad_members = active_squad.players.all()

                    if is_scramble_game:
                        # 🟢 Symmetrical Score Mirroring grabs the captain's input and writes it for everyone
                        scramble_strokes_raw = request.POST.get(f'score_{current_player.id}')
                        if scramble_strokes_raw and scramble_strokes_raw.isdigit():
                            scramble_strokes = int(scramble_strokes_raw)
                            for p in squad_members:
                                HoleScore.objects.update_or_create(
                                    round=active_round, hole=hole, player=p,
                                    defaults={'gross_value': scramble_strokes}
                                )
                        else:
                            HoleScore.objects.filter(round=active_round, hole=hole, player__in=squad_members).delete()
                    else:
                        for p in squad_members:
                            strokes_raw = request.POST.get(f'score_{p.id}')
                            if strokes_raw and strokes_raw.isdigit():
                                HoleScore.objects.update_or_create(
                                    round=active_round, hole=hole, player=p,
                                    defaults={'gross_value': int(strokes_raw)}
                                )
                            else:
                                HoleScore.objects.filter(round=active_round, hole=hole, player=p).delete()

                # INDENTATION SAFE POST DATA NAVIGATION HANDLER BLOCK
                direction = request.POST.get('nav_direction', 'next')
                if direction == 'prev':
                    return redirect('scorecard:player_scorecard', hole_number=prev_hole)

                # 🏁 DYNAMIC FINISH ROUND GATE & AUTOMATED QUOTA ADJUSTMENT ENGINE
                elif direction == 'finish':
                    clean_fmt_key = str(game_format).strip().lower()

                    # Team Chicago: do NOT rewrite quotas here — today's standings must keep
                    # the quotas that were in effect for this round. Next-round updates run
                    # from the leaderboard "Update Next-Round Quotas" action (or erase round).
                    if clean_fmt_key in ["team_chicago_points_9", "9_team_chicago"]:
                        return redirect('/leaderboard/?format=9_team_chicago')

                    elif clean_fmt_key in ["chicago_points_18", "18_ind_chicago"]:
                        # Standings stay based on today's quotas; next-round updates run when the round is erased/finalized
                        return redirect('scorecard:tournament_leaderboard')

                    elif clean_fmt_key == "9_hole_scramble":
                        return redirect('/leaderboard/?format=9_hole_scramble')
                    elif clean_fmt_key == "18_gross_net":
                        return redirect('/leaderboard/?format=18_gross_net')
                    else:
                        return redirect('scorecard:tournament_leaderboard')

                else:
                    return redirect('scorecard:player_scorecard', hole_number=next_hole)

            # 🟢 Section 2 Data Assembly Block: Packages context dictionaries and renders templates
            if active_squad:
                squad_players = active_squad.players.all().order_by('name')

                # 👑 CAPTAIN SCORE LOOKUP OVERLAY: Pre-fetches the captain's score to mirror to teammates
                captain_strokes = ""
                if active_squad.scorekeeper:
                    cap_score = HoleScore.objects.filter(round=active_round, hole=hole,
                                                         player=active_squad.scorekeeper).first()
                    if cap_score and cap_score.gross_value:
                        captain_strokes = cap_score.gross_value

                for player in squad_players:
                    existing_score = HoleScore.objects.filter(round=active_round, hole=hole, player=player).first()
                    active_display_hcp = player.ladies_league_handicap or 0 if is_womens_league else player.handicap or 0

                    chicago_target = 0
                    prior_points_earned = 0
                    current_hole_points = ""

                    current_strokes = existing_score.gross_value if (
                                existing_score and existing_score.gross_value is not None) else None

                    if is_chicago_game:
                        if game_format in ["chicago_points_18", "18_IND_CHICAGO"]:
                            round_quota = player.chicago_points_18 if (
                                        player.chicago_points_18 and player.chicago_points_18 > 0) else max(
                                39 - active_display_hcp, 2)
                        elif game_format in ["team_chicago_points_9", "9_TEAM_CHICAGO"]:
                            round_quota = _team_chicago_quota(player)
                        elif game_format == "9_WOMENS_LEAGUE":
                            round_quota = max(20 - active_display_hcp, 1)
                        else:
                            round_quota = 0

                        chicago_target = round_quota

                        # Cumulative points from other holes (same 8/4/2/1 scale as scorecard JS)
                        prior_scores = HoleScore.objects.filter(
                            round=active_round, player=player, gross_value__gt=0
                        ).exclude(hole=hole).select_related('hole')
                        prior_points_earned = chicago_points_from_scores(prior_scores)

                        this_hole_points = 0
                        if current_strokes is not None and int(current_strokes) > 0:
                            relation_to_par = int(current_strokes) - hole.par
                            if relation_to_par <= -2:
                                this_hole_points = 8
                            elif relation_to_par == -1:
                                this_hole_points = 4
                            elif relation_to_par == 0:
                                this_hole_points = 2
                            elif relation_to_par == 1:
                                this_hole_points = 1

                        # Running total shown in Chgo. Points: prior holes + this hole (if scored)
                        current_hole_points = prior_points_earned + this_hole_points

                    player_scores.append({
                        'player': player,
                        'display_hcp': active_display_hcp,
                        'chicago_target': chicago_target,
                        'prior_points': prior_points_earned,
                        'current_points': current_hole_points,
                        'score': {
                            'strokes': current_strokes if current_strokes else ''
                        },
                        # 👑 SYNCHRONIZATION TOKEN PASS:
                        # Feeds the captain's score text directly to regular teammate display rows
                        'captain_stroke_sync': captain_strokes
                    })

    # Accumulate running totals for the team summary banner display elements
    if active_squad and player_scores:
        for p_row in player_scores:
            squad_total_points_needed += int(p_row.get('chicago_target') or _team_chicago_quota(p_row['player']))
            squad_running_total_earned += int(p_row.get('current_points') or 0)

    # Format-specific leaderboard link (keeps Chicago / scramble / women's boards separate)
    leaderboard_url = '/leaderboard/'
    fmt_key = str(game_format or '').strip().lower()
    if fmt_key == '9_womens_league':
        leaderboard_url = '/leaderboard/?format=9_womens_league'
    elif fmt_key in ('chicago_points_18', '18_ind_chicago'):
        leaderboard_url = '/leaderboard/?format=chicago_points_18'
    elif fmt_key in ('team_chicago_points_9', '9_team_chicago'):
        leaderboard_url = '/leaderboard/?format=9_team_chicago'
    elif fmt_key == '9_hole_scramble':
        leaderboard_url = '/leaderboard/?format=9_hole_scramble'
    elif fmt_key == '18_gross_net':
        leaderboard_url = '/leaderboard/?format=18_gross_net'

    context = {
        'current_hole': hole,
        'hole_number': hole_number,
        'next_hole': next_hole,
        'prev_hole': prev_hole,
        'round': active_round,
        'squad': active_squad,
        'squad_players': squad_players,
        'player_scores': player_scores,
        'is_final_hole': is_final_hole,
        'is_chicago_game': is_chicago_game,
        'is_womens_league': is_womens_league,
        'is_scramble_game': is_scramble_game,
        'is_scorecard_editable': is_scorecard_editable,
        'squad_total_points_needed': squad_total_points_needed,
        'squad_running_total_earned': squad_running_total_earned,
        'leaderboard_url': leaderboard_url,
    }

    if active_round and (is_scramble_game or game_format in ["team_chicago_points_9", "9_TEAM_CHICAGO"]):
        return render(request, 'scorecard/player_scorecard_teamchicago.html', context)

    return render(request, 'scorecard/player_scorecard.html', context)


@staff_member_required
def update_payout_settings_view(request):
    rules, created = PayoutSetting.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = PayoutRulesForm(request.POST, instance=rules)
        if form.is_valid():
            form.save()
            messages.success(request, "💸 Men's League Payout Split Matrix rules updated successfully!")
            return redirect('scorecard:admin_dashboard')
    else:
        form = PayoutRulesForm(instance=rules)

    return render(request, 'scorecard/payout_settings.html', {'form': form})


@staff_member_required
def skins_verification_panel(request):
    active_round = GolfRound.objects.filter(is_active=True).first()
    fmt = str(active_round.game_format or '').strip().lower() if active_round else ''
    use_net = fmt in ('18_hole_mens_league', 'mens_league')
    skins_found = compute_round_skins(active_round, use_net=use_net)

    context = {
        'round': active_round,
        'skins_found': skins_found,
        'use_net': use_net,
    }
    return render(request, 'scorecard/skins_panel.html', context)


@csrf_exempt
@login_required
def update_format_ajax(request):
    if request.method == "POST":
        try:
            round_id = request.POST.get('round_id')
            game_format = request.POST.get('game_format') or "18_GROSS_NET"

            # Fetch the current active round tracking row
            active_round = None
            if round_id and round_id.isdigit():
                active_round = GolfRound.objects.filter(id=round_id).first()
            if not active_round:
                active_round = GolfRound.objects.filter(is_active=True).first()

            if active_round:
                # 🟢 FIXED: Force commit the format string directly to your MySQL row columns
                active_round.game_format = game_format
                active_round.save(update_fields=['game_format'])

                # Clean up any cached model states or old handicap projections in player tables
                Player.objects.filter(is_playing_today=True).update(new_handicap=0)

                return JsonResponse({
                    'status': 'success',
                    'current_format': active_round.game_format
                })

            return JsonResponse({'status': 'failed', 'error': 'No active round found'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'failed', 'error': str(e)}, status=400)

    return JsonResponse({'status': 'failed', 'message': 'Invalid method structure'}, status=400)


@staff_member_required
def finalize_handicaps_action(request):
    if request.method == "POST":
        active_round = GolfRound.objects.filter(is_active=True).first()
        if active_round:
            # Overwrite the primary handicap with the new calculated handicap for all active players
            active_players = Player.objects.filter(is_playing_today=True)
            for player in active_players:
                if player.new_handicap > 0 or player.handicap > 0:
                    # Move the projection into the primary field officially
                    player.handicap = player.new_handicap if player.new_handicap > 0 else player.handicap
                    player.save(update_fields=['handicap'])

            messages.success(request,
                             "🔒 Today's round handicaps have been officially finalized and locked into player profiles for the next match!")
        return redirect('scorecard:admin_dashboard')
    return redirect('scorecard:admin_dashboard')


@login_required
def finish_round_update_quotas(request):
    """
    Staff end-of-round action from the leaderboard.
    - 18-hole Chicago: updates chicago_points_18 from today's +/- to quota
    - 9-hole Team Chicago: updates 18-hole Chicago from today's 9-hole +/- 
    - 18-hole Men's League: recalculates player.handicap from net vs par
    - 18-hole Individual Gross/Net: same handicap update into player.handicap
    - 9-hole Women's: updates ladies_league_handicap from today's net vs par
    Locked by GolfRound.metrics_finalized so it cannot run twice.
    """
    if not request.user.is_staff:
        return redirect('scorecard:leaderboard')

    active_round = GolfRound.objects.filter(is_active=True).first()
    if not active_round:
        return redirect('scorecard:leaderboard')

    fmt = str(active_round.game_format or '').strip().lower()

    if active_round.metrics_finalized:
        messages.info(request, "Next-round metrics were already updated for this round.")
        if fmt in ("chicago_points_18", "18_ind_chicago"):
            return redirect('/leaderboard/?format=chicago_points_18')
        if fmt in ("9_team_chicago", "team_chicago_points_9"):
            return redirect('/leaderboard/?format=9_team_chicago')
        if fmt in ("18_hole_mens_league", "mens_league"):
            return redirect('scorecard:tournament_leaderboard')
        if fmt == "18_gross_net":
            return redirect('/leaderboard/?format=18_gross_net')
        if fmt == "9_womens_league":
            return redirect('/leaderboard/?format=9_womens_league')
        return redirect('scorecard:leaderboard')

    if fmt in ("chicago_points_18", "18_ind_chicago"):
        apply_18_chicago_quota_updates(active_round)
        active_round.metrics_finalized = True
        active_round.save(update_fields=['metrics_finalized'])
        messages.success(
            request,
            "18-Hole Chicago quotas updated for next round based on today's +/- to quota."
        )
        return redirect('/leaderboard/?format=chicago_points_18')

    if fmt in ("9_team_chicago", "team_chicago_points_9"):
        apply_9_team_chicago_quota_updates(active_round)
        active_round.metrics_finalized = True
        active_round.save(update_fields=['metrics_finalized'])
        messages.success(
            request,
            "9-Hole Team Chicago quotas updated for next round based on today's +/- to quota."
        )
        return redirect('/leaderboard/?format=9_team_chicago')

    if fmt in ("18_hole_mens_league", "mens_league"):
        updated = apply_mens_handicap_updates(active_round)
        active_round.metrics_finalized = True
        active_round.save(update_fields=['metrics_finalized'])
        messages.success(
            request,
            f"Men's league handicaps updated for {len(updated)} player(s) "
            f"(new_hcp = old_hcp + (net − par) × 0.8)."
        )
        return redirect('scorecard:tournament_leaderboard')

    if fmt == "18_gross_net":
        updated = apply_mens_handicap_updates(active_round)
        active_round.metrics_finalized = True
        active_round.save(update_fields=['metrics_finalized'])
        messages.success(
            request,
            f"18-Hole Individual handicaps updated for {len(updated)} player(s) "
            f"and saved to the Handicap field (new_hcp = old_hcp + (net − par) × 0.8)."
        )
        return redirect('/leaderboard/?format=18_gross_net')

    if fmt == "9_womens_league":
        apply_womens_handicap_updates(active_round)
        active_round.metrics_finalized = True
        active_round.save(update_fields=['metrics_finalized'])
        messages.success(
            request,
            "Ladies league handicaps updated for next round based on today's net scores."
        )
        return redirect('/leaderboard/?format=9_womens_league')

    return redirect('scorecard:leaderboard')


@csrf_exempt  # Ensure proper security/CSRF handling according to your framework setup
@require_POST
def update_player_quota(request, player_id):
    try:
        data = json.loads(request.body)
        new_quota = int(data.get('chicago_points_18'))

        # Enforce rule boundaries (quota baseline floor protection)
        if new_quota < 2:
            return JsonResponse({'status': 'error', 'message': 'Quota cannot be less than 2.'}, status=400)

        player = get_object_or_404(Player, id=player_id)
        player.chicago_points_18 = new_quota
        player.save()  # Persists directly to your table

        return JsonResponse({'status': 'success', 'updated_quota': player.chicago_points_18})

    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({'status': 'error', 'message': 'Invalid data provided.'}, status=400)


# @login_required
def tournament_leaderboard(request):
    # SECURITY FIX: Direct hardcoded path string mapping avoids NoReverseMatch compiler check bugs
    if not request.user.is_authenticated:
        return redirect('/login/')

    active_round = GolfRound.objects.filter(is_active=True).first()

    # 🟢 FIXED: Grab any explicit layout parameters straight from the browser URL address bar window path
    url_format_override = request.GET.get('format', '').strip().lower()

    net_leaderboard = []
    is_mens_league = False
    is_chicago = False
    is_team_game = False
    is_stroke_play_game = False
    is_scramble_game = False
    clean_fmt_check = ""

    # Initialize money variables with default values to prevent context crashes
    total_individual_count = 0
    entry_fee_val = 12.00
    course_cut_val = 2.00
    closest_to_hole_rate = 2.00
    skins_rate = 3.00

    calculated_total_pot = 0.00
    calculated_course_money = 0.00
    calculated_closest_pin_pool = 0.00
    calculated_skins_pool = 0.00
    calculated_net_placement_pool = 0.00

    if active_round:
        # DETECT SYSTEM SELECTION STRINGS STRIPPING WHITESPACE (PRESERVING CASING)
        raw_game_format = str(active_round.game_format or '')
        game_format = raw_game_format.strip()
        clean_fmt_check = game_format.lower()

        # 🟢 FIXED: If the URL address bar explicitly dictates a format suffix tag override, force the engine to align with it!
        if url_format_override:
            clean_fmt_check = url_format_override
            game_format = url_format_override

        # EXACT MATCH ENGINE CHECKERS
        is_chicago = clean_fmt_check in ["chicago_points_18", "team_chicago_points_9", "18_ind_chicago",
                                         "9_team_chicago"]
        is_team_game = clean_fmt_check in ["team_chicago_points_9", "9_team_chicago"]
        is_stroke_play_game = clean_fmt_check in ["9_womens_league", "18_gross_net"]
        is_scramble_game = clean_fmt_check == "9_hole_scramble"

        if clean_fmt_check in ["18_hole_mens_league", "mens_league"]:
            is_mens_league = True

        # DEFENSIVE HEADCOUNT FILTER: Only pull players with an active score record in THIS round
        assigned_player_ids = HoleScore.objects.filter(
            round=active_round,
            gross_value__gt=0
        ).values_list('player_id', flat=True)

        # GATHER TOTAL ACTUAL INDIVIDUALS FOR THE FINANCIAL SUMMARY DISPLAY CARD
        all_active_individuals = Player.objects.filter(id__in=assigned_player_ids).distinct()
        total_individual_count = all_active_individuals.count()

        base_list = []
        is_team_chicago_active = clean_fmt_check in ["team_chicago_points_9", "9_team_chicago"]

        # 👥 BRANCH 1: THE TEAM CHICAGO GROUPING BOARD MATRIX ENGINE
        if is_team_chicago_active:
            active_squads = Squad.objects.filter(round=active_round).distinct()

            for squad in active_squads:
                squad_members = list(squad.players.all())
                if not squad_members:
                    continue

                total_squad_gross_strokes = 0
                total_squad_chicago_points = 0
                # Full team quota target (matches scorecard Group Target)
                total_squad_quota_target = sum(_team_chicago_quota(p) for p in squad_members)
                squad_holes_played = 0
                has_any_scores = False

                # 🟢 FIXED: Identify the Designated Captain and compile other partners separately
                squad_captain = squad.scorekeeper  # Pulls the designated leader from the database row record
                captain_name = squad_captain.name if squad_captain else "Unassigned Captain"

                partner_names_list = []

                for player in squad_members:
                    # If this player is NOT the captain, add them to the teammate stack list
                    if squad_captain and player.id != squad_captain.id:
                        partner_names_list.append(player.name)
                    elif not squad_captain:
                        partner_names_list.append(player.name)

                    played_scores = HoleScore.objects.filter(
                        round=active_round, player=player, gross_value__gt=0
                    ).select_related('hole')

                    if played_scores.exists():
                        has_any_scores = True
                        squad_holes_played = max(squad_holes_played, played_scores.count())

                        player_gross = played_scores.aggregate(g_sum=Sum('gross_value'))['g_sum'] or 0
                        total_squad_gross_strokes += player_gross
                        total_squad_chicago_points += chicago_points_from_scores(played_scores)

                if has_any_scores:
                    # Points Net +/- : total Chicago points earned this round.
                    # Green when over team quota, red when under, yellow when even.
                    squad_quota_diff = total_squad_chicago_points - total_squad_quota_target

                    display_gross = total_squad_gross_strokes
                    display_net = f"{total_squad_chicago_points} Pts"
                    if squad_quota_diff > 0:
                        to_par_str = f"+{squad_quota_diff}"
                        points_net_class = "plus"
                        points_net_display = f"+{squad_quota_diff}"
                    elif squad_quota_diff < 0:
                        to_par_str = str(squad_quota_diff)
                        points_net_class = "minus"
                        points_net_display = str(squad_quota_diff)
                    else:
                        to_par_str = "0"
                        points_net_class = "even"
                        points_net_display = "0"
                    sort_net_metric = -squad_quota_diff

                    base_list.append({
                        'is_team_row': True,
                        # 🟢 FIXED: Package Captain and Teammates cleanly as separate entities to the template payload
                        'captain_label': f"Team {captain_name}",
                        'teammates_list': partner_names_list,
                        'holes_played': squad_holes_played,
                        'strokes': display_gross,
                        'net_score': display_net,
                        'to_par': to_par_str,
                        'points_net_diff': squad_quota_diff,
                        'points_net_display': points_net_display,
                        'points_net_class': points_net_class,
                        'points_earned': total_squad_chicago_points,
                        'points_quota': total_squad_quota_target,
                        'sort_net': sort_net_metric,
                        'payout': 0.00
                    })


        # 👥 BRANCH 1B: 9-HOLE SCRAMBLE — one row per squad (captain team score only)
        elif is_scramble_game or clean_fmt_check == "9_hole_scramble":
            active_squads = (
                Squad.objects.filter(round=active_round)
                .select_related('scorekeeper', 'starting_hole')
                .prefetch_related('players')
                .order_by('squad_number')
            )

            for squad in active_squads:
                squad_captain = squad.scorekeeper
                squad_members = list(squad.players.all().order_by('name'))

                # Ensure captain appears even if missing from M2M
                if squad_captain and squad_captain not in squad_members:
                    squad_members.insert(0, squad_captain)

                if not squad_captain and not squad_members:
                    continue

                if not squad_captain:
                    squad_captain = squad_members[0]

                captain_name = squad_captain.name
                partner_names_list = [
                    p.name for p in squad_members if p.id != squad_captain.id
                ]

                # Team score lives on the captain (same strokes written to all members)
                played_scores = HoleScore.objects.filter(
                    round=active_round, player=squad_captain, gross_value__gt=0
                ).select_related('hole')
                holes_played = played_scores.count()
                if holes_played == 0:
                    continue

                g_sum = played_scores.aggregate(g_sum=Sum('gross_value'))['g_sum'] or 0

                if squad.starting_hole:
                    start_h = squad.starting_hole.hole_number
                    scramble_route = list(range(start_h, 10)) + list(range(1, start_h))
                else:
                    scramble_route = list(range(1, 10))

                played_hole_numbers = scramble_route[:holes_played]
                total_route_par = (
                    Hole.objects.filter(hole_number__in=played_hole_numbers)
                    .aggregate(Sum('par'))['par__sum'] or 0
                )
                relative_to_par = g_sum - total_route_par
                to_par_str = (
                    "E" if relative_to_par == 0
                    else (f"{relative_to_par}" if relative_to_par < 0 else f"+{relative_to_par}")
                )

                base_list.append({
                    'is_team_row': True,
                    'captain_label': captain_name,
                    'teammates_list': partner_names_list,
                    'holes_played': holes_played,
                    'strokes': g_sum,
                    'net_score': to_par_str,
                    'to_par': to_par_str,
                    'sort_net': g_sum,
                    'payout': 0.00,
                })


        # 👤 BRANCH 2: THE STANDARD INDIVIDUAL SCANNERS (MEN'S LEAGUE / GROSS-NET / CHICAGO / WOMEN'S)
        else:
            for player in all_active_individuals:
                played_scores = HoleScore.objects.filter(round=active_round, player=player, gross_value__gt=0)
                holes_played = played_scores.count()
                stats = played_scores.aggregate(g_sum=Sum('gross_value'))
                g_sum = stats['g_sum'] or 0

                display_gross = g_sum
                display_net = "-"
                sort_net_metric = g_sum if holes_played > 0 else 999
                to_par_str = "E"
                hcp = player.handicap or 0

                if is_mens_league or (clean_fmt_check == "18_gross_net"):
                    n_sum = g_sum - hcp
                    display_net = n_sum
                    sort_net_metric = n_sum if holes_played > 0 else 999
                    if holes_played > 0:
                        played_hole_ids = played_scores.values_list('hole_id', flat=True)
                        total_completed_par = Hole.objects.filter(id__in=played_hole_ids).aggregate(Sum('par'))[
                                                  'par__sum'] or 0
                        to_par_raw = n_sum - total_completed_par
                        to_par_str = f"E" if to_par_raw == 0 else (
                            f"{to_par_raw}" if to_par_raw < 0 else f"+{to_par_raw}")

                elif clean_fmt_check == "9_womens_league":
                    # 9-hole women's league: stroke-play net using ladies_league_handicap (not Chicago points)
                    ladies_hcp = player.ladies_league_handicap or 0
                    n_sum = g_sum - ladies_hcp
                    display_net = n_sum
                    sort_net_metric = n_sum if holes_played > 0 else 999
                    if holes_played > 0:
                        played_hole_ids = played_scores.values_list('hole_id', flat=True)
                        total_completed_par = Hole.objects.filter(id__in=played_hole_ids).aggregate(Sum('par'))[
                                                  'par__sum'] or 0
                        to_par_raw = n_sum - total_completed_par
                        to_par_str = f"E" if to_par_raw == 0 else (
                            f"{to_par_raw}" if to_par_raw < 0 else f"+{to_par_raw}")

                elif clean_fmt_check in ["chicago_points_18", "18_ind_chicago"]:
                    # Individual Chicago: points earned vs personal quota target
                    total_chicago_points = 0
                    for score in played_scores.select_related('hole'):
                        relation_to_par = score.gross_value - score.hole.par
                        if relation_to_par <= -2:
                            total_chicago_points += 8
                        elif relation_to_par == -1:
                            total_chicago_points += 4
                        elif relation_to_par == 0:
                            total_chicago_points += 2
                        elif relation_to_par == 1:
                            total_chicago_points += 1

                    quota = player.chicago_points_18 if (
                                player.chicago_points_18 and player.chicago_points_18 > 0) else max(
                        39 - hcp, 2)

                    quota_diff = total_chicago_points - quota
                    display_net = f"{total_chicago_points} Pts"
                    to_par_str = f"+{quota_diff}" if quota_diff > 0 else (
                        f"{quota_diff}" if quota_diff < 0 else "E")
                    # Better (more points over quota) sorts first — same as team Chicago
                    sort_net_metric = -quota_diff if holes_played > 0 else 999

                base_list.append({
                    'is_team_row': False,
                    'player': player,
                    'holes_played': holes_played,
                    'strokes': display_gross if holes_played > 0 else "-",
                    'net_score': display_net,
                    'to_par': to_par_str,
                    'sort_net': sort_net_metric,
                    'payout': 0.00
                })
        # 🏃‍♂️ RUN ORDER PASS FOR LEADERBOARD POSITIONS
        ordered_list = sorted(base_list, key=lambda x: x['sort_net'])

        # 📈 MONEY MATRIX INITIALIZATION
        if total_individual_count > 0:
            if clean_fmt_check in ["18_gross_net", "9_hole_scramble", "team_chicago_points_9", "9_team_chicago",
                                   "9_womens_league"]:
                entry_fee_val = 6.00
                course_cut_val = 2.00
                closest_to_hole_rate = 0.00
                skins_rate = 0.00
            else:
                entry_fee_val = 12.00
                course_cut_val = 2.00
                closest_to_hole_rate = 2.00
                skins_rate = 3.00

            calculated_total_pot = total_individual_count * entry_fee_val
            calculated_course_money = total_individual_count * course_cut_val
            calculated_closest_pin_pool = total_individual_count * closest_to_hole_rate
            calculated_skins_pool = total_individual_count * skins_rate
            calculated_net_placement_pool = calculated_total_pot - (
                        calculated_course_money + calculated_closest_pin_pool + calculated_skins_pool)

            # 📈 DYNAMIC PLACEMENT PAYOUT ENGINE
            item_count_to_payout = len([x for x in ordered_list if x['holes_played'] > 0])
            if item_count_to_payout <= 2:
                payout_percentages = [1.00]
            elif item_count_to_payout <= 3:
                payout_percentages = [0.60, 0.40]
            elif item_count_to_payout <= 15:
                payout_percentages = [0.50, 0.30, 0.20]
            else:
                payout_percentages = [0.40, 0.30, 0.20, 0.10]

            placement_prizes = [calculated_net_placement_pool * pct for pct in payout_percentages]

            # 🛠️ PLACEMENT TIE RESOLUTION MATRIX
            from collections import defaultdict
            score_groups = defaultdict(list)
            for idx, p_row in enumerate(ordered_list):
                if p_row['holes_played'] > 0:
                    score_groups[p_row['sort_net']].append(idx)

            sorted_score_keys = sorted(score_groups.keys())
            current_prize_rank_index = 0

            for score_key in sorted_score_keys:
                tied_player_indices = score_groups[score_key]
                tied_count = len(tied_player_indices)

                true_display_rank = current_prize_rank_index + 1
                is_currently_tied = tied_count > 1

                slots_to_span = list(range(current_prize_rank_index, current_prize_rank_index + tied_count))
                combined_prize_pool = 0.0
                for slot in slots_to_span:
                    if slot < len(placement_prizes):
                        combined_prize_pool += placement_prizes[slot]

                even_split_share = combined_prize_pool / tied_count if tied_count > 0 else 0.0

                for player_idx in tied_player_indices:
                    ordered_list[player_idx]['payout'] = int(round(even_split_share, 0))
                    ordered_list[player_idx]['true_rank'] = true_display_rank
                    ordered_list[player_idx]['is_tied'] = is_currently_tied

                current_prize_rank_index += tied_count

        net_leaderboard = ordered_list

    # Compute all raw integer baselines to remove math filters from HTML blocks
    raw_pin_pool = float(calculated_closest_pin_pool) if calculated_closest_pin_pool else 0.0
    pin_split_integer = int(round(raw_pin_pool / 2, 0)) if raw_pin_pool > 0 else 0

    if clean_fmt_check in ["18_gross_net", "9_hole_scramble", "team_chicago_points_9", "9_team_chicago",
                           "9_womens_league"]:
        entry_fee_label = "6.00"
    else:
        entry_fee_label = "12.00"

    # Men's league: auto-compute net skins for the Round Skins Winners panel
    skins_found = []
    skins_winners_html = ""
    skins_payout_rows = []
    skins_per_skin_value = 0
    if active_round and (is_mens_league or clean_fmt_check in ("18_hole_mens_league", "mens_league")):
        skins_found = compute_round_skins(active_round, use_net=True)
        skins_winners_html, skins_payout_rows = format_skins_winners_html(
            skins_found, skins_pool=calculated_skins_pool
        )
        if skins_found:
            skins_per_skin_value = int(round(float(calculated_skins_pool or 0) / len(skins_found), 0))

    context = {
        'round': active_round,
        'net_leaderboard': net_leaderboard,
        'is_mens_league': is_mens_league or (clean_fmt_check == "18_hole_mens_league"),
        'is_chicago': is_chicago,
        'is_team_game': is_team_game,
        'is_team_chicago': is_team_game or (
            active_round and str(active_round.game_format or '').strip() in (
                '9_TEAM_CHICAGO', 'team_chicago_points_9', '9_team_chicago'
            )
        ),
        'is_stroke_play_game': is_stroke_play_game or (clean_fmt_check == "18_gross_net"),
        'is_scramble_game': is_scramble_game or (clean_fmt_check == "9_hole_scramble"),
        'total_individual_count': total_individual_count,
        'skins_found': skins_found,
        'skins_winners_html': skins_winners_html,
        'skins_payout_rows': skins_payout_rows,
        'skins_per_skin_value': skins_per_skin_value,
        'skins_total_won': len(skins_found),

        # Whole-number visibility triggers
        'closest_pin_pool_int': int(round(raw_pin_pool, 0)),
        'skins_pool_int': int(round(float(calculated_skins_pool or 0), 0)),
        'entry_fee_display': entry_fee_label,

        # Financial strings pass cleanly formatted to whole dollar integers
        'total_pot': f"{int(round(calculated_total_pot, 0))}",
        'course_money': f"{int(round(calculated_course_money, 0))}",
        'closest_pin_pool': f"{int(round(raw_pin_pool, 0))}",
        'skins_pool': f"{int(round(float(calculated_skins_pool or 0), 0))}",
        'net_pool': f"{int(round(calculated_net_placement_pool, 0))}",

        # Pre-calculated full dollar variable passes safely to HTML
        'pin_payout_each': pin_split_integer,
        'metrics_finalized': bool(active_round and getattr(active_round, 'metrics_finalized', False)),
    }
    return render(request, 'scorecard/leaderboard.html', context)


@require_POST
def save_stroke_api(request):
    try:
        data = json.loads(request.body)
        player_id = data.get('player_id')
        hole_id = data.get('hole_id')
        round_id = data.get('round_id')
        gross_value = data.get('gross_value')  # Can be integer score or None

        # Convert back-end target objects
        g_round = get_object_or_404(GolfRound, id=round_id)
        hole = get_object_or_404(Hole, id=hole_id)
        player = get_object_or_404(Player, id=player_id)

        # 🟢 Fetch or initialize the instance to rewrite scores seamlessly
        hole_score, created = HoleScore.objects.get_or_create(
            round=g_round,
            hole=hole,
            player=player
        )

        if gross_value is not None and str(gross_value).strip() != "":
            hole_score.gross_value = int(gross_value)
        else:
            hole_score.gross_value = None  # Clears score from database if unselected

        hole_score.save()
        return JsonResponse({'status': 'success', 'message': 'Score saved successfully'})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


def finalize_tournament_round(request, round_id):
    # Manual security check: Safely restricts logged-out requests
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('scorecard:login')

    if int(round_id) == 0:
        messages.error(request,
                       "Cannot finalize match. There is no active tournament round session initialized in the database right now.")
        return redirect('/admin-dashboard/')

    active_round = get_object_or_404(GolfRound, id=round_id)
    game_format = str(active_round.game_format or '').strip()

    # Isolate only players who logged active scores to run their handicap calculations
    assigned_player_ids = HoleScore.objects.filter(
        round=active_round,
        gross_value__gt=0
    ).values_list('player_id', flat=True).distinct()

    active_players = Player.objects.filter(id__in=assigned_player_ids)
    for player in active_players:
        played_scores = HoleScore.objects.filter(round=active_round, player=player, gross_value__gt=0)
        holes_count = played_scores.count()

        if holes_count > 0:
            total_gross = played_scores.aggregate(g_sum=Sum('gross_value'))['g_sum'] or 0
            course_par = sum(score.hole.par for score in played_scores) if holes_count < 18 else 72

            # Map out raw Chicago points accumulated during this round layout pass
            total_chicago_points = 0
            for score in played_scores:
                rel_par = score.gross_value - score.hole.par
                if rel_par <= -2:
                    total_chicago_points += 8
                elif rel_par == -1:
                    total_chicago_points += 4
                elif rel_par == 0:
                    total_chicago_points += 2
                elif rel_par == 1:
                    total_chicago_points += 1

            # BRANCH A: MEN'S LEAGUE & 18-HOLE INDIVIDUAL GROSS/NET
            if game_format in ["18_HOLE_MENS_LEAGUE", "18_GROSS_NET"]:
                adjust_mens_handicap_for_player(player, played_scores)

            # BRANCH B: 18-HOLE CHICAGO POINTS GAMES
            elif game_format in ["18_IND_CHICAGO", "chicago_points_18"]:
                adjust_18_chicago_quota_for_player(player, played_scores)

            # BRANCH C: 9-HOLE LADIES LEAGUE FORMAT
            elif game_format == "9_WOMENS_LEAGUE":
                adjust_ladies_handicap_for_player(player, played_scores)

            # BRANCH D: 9-HOLE TEAM CHICAGO FORMAT
            elif game_format in ["team_chicago_points_9", "9_TEAM_CHICAGO"]:
                adjust_9_team_chicago_quota_for_player(player, played_scores)

    # SECTION 4: SHIELD CLOSURE ENFORCEMENT ENGINE
    # -------------------------------------------------------------
    # 🟢 FIXED: Clears out old game format string & shuts off the active round marker
    active_round.game_format = ""
    active_round.is_active = False
    active_round.save(update_fields=['game_format', 'is_active'])

    # 2. Directly clear the database bits at the engine level
    Player.objects.all().update(is_playing_today=0)

    # 3. Direct looping verification cleanup pass
    for p in Player.objects.all():
        p.is_playing_today = False
        p.save(update_fields=['is_playing_today'])

    # 4. INITIATE THE NEXT FRESH TOURNAMENT BLANK CONTAINER
    GolfRound.objects.create(
        course_name="PRGC Championship Course",
        is_active=True,
        game_format=""  # Kept as an empty string to safely pass MySQL NOT NULL constraints
    )

    messages.success(request,
                     "Tournament round finalized successfully. Handicaps adjusted, and a fresh round slate has been initialized for next week!")
    return redirect('/admin-dashboard/')


def _team_chicago_quota(player):
    """
    9-hole Team Chicago points needed for a player:
    half of their 18-hole Chicago Points, rounded up.
    """
    return player.team_chicago_quota


def _auto_fill_team_chicago_squads(active_squads, remaining_pool, squad_size):
    """
    Fill captain-seeded squads so each team's total Chicago points targets
    stay as even as possible. Cart partners stay together as one block.
    """
    remaining_by_id = {p.id: p for p in remaining_pool}
    remaining_ids = set(remaining_by_id.keys())

    # Seed state from existing squad members (captains + anyone already placed)
    squad_state = []
    for squad in active_squads:
        members = list(squad.players.all())
        squad_state.append({
            'squad': squad,
            'count': len(members),
            'points': sum(_team_chicago_quota(m) for m in members),
            'member_ids': {m.id for m in members},
        })

    def add_players_to_state(state, players):
        state['squad'].players.add(*players)
        for p in players:
            state['count'] += 1
            state['points'] += _team_chicago_quota(p)
            state['member_ids'].add(p.id)
            remaining_ids.discard(p.id)
            remaining_by_id.pop(p.id, None)

    # Prefer putting a captain's cart partner on that captain's squad first
    for state in squad_state:
        captain = state['squad'].scorekeeper
        if not captain:
            continue
        partner = captain.riding_partner
        if partner and partner.id in remaining_ids:
            if state['count'] + 1 <= squad_size:
                add_players_to_state(state, [partner])

    # Build cart-pair / solo blocks from whoever is still unassigned
    used = set()
    blocks = []
    for pid in list(remaining_ids):
        if pid in used or pid not in remaining_by_id:
            continue
        player = remaining_by_id[pid]
        partner = player.riding_partner
        if partner and partner.id in remaining_ids and partner.id not in used:
            blocks.append([player, partner])
            used.add(player.id)
            used.add(partner.id)
        else:
            blocks.append([player])
            used.add(player.id)

    # Highest quotas first → always land on the current lowest-total squad
    blocks.sort(key=lambda b: sum(_team_chicago_quota(p) for p in b), reverse=True)

    leftovers = []
    for block in blocks:
        block_size = len(block)
        block_pts = sum(_team_chicago_quota(p) for p in block)
        candidates = [s for s in squad_state if s['count'] + block_size <= squad_size]
        if not candidates:
            leftovers.append(block)
            continue
        # Tie-break: lowest points, then smallest headcount
        target = min(candidates, key=lambda s: (s['points'], s['count']))
        add_players_to_state(target, block)

    # Spillover: place leftovers on the lowest-points team (may exceed target size)
    for block in leftovers:
        if not any(p.id in remaining_by_id for p in block):
            continue
        target = min(squad_state, key=lambda s: (s['points'], s['count']))
        add_players_to_state(target, [p for p in block if p.id in remaining_by_id])

    for state in squad_state:
        state['squad'].save()

    totals = [s['points'] for s in squad_state]
    spread = (max(totals) - min(totals)) if totals else 0
    return spread


@staff_member_required
def generate_random_scramble_squads(request, round_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('scorecard:login')

    active_round = get_object_or_404(GolfRound, id=round_id)

    if request.method == "POST":
        # 1. 🛑 FIXED: Gather the squads you ALREADY built with their manual hole assignments.
        # DO NOT call Squad.objects.filter(round=active_round).delete() here or it wipes your choices!
        active_squads = list(Squad.objects.filter(round=active_round).select_related('scorekeeper', 'starting_hole'))

        if not active_squads:
            messages.error(request,
                           "❌ Cannot run auto-grouping logic. You must manually assign at least one Captain to a Starting Hole first!")
            return redirect('/admin-dashboard/')

        # 2. Extract every single checked-in player for today
        all_checked_in = list(Player.objects.filter(is_playing_today=True).select_related('riding_partner'))

        # 3. Track players who are ALREADY assigned to a squad (your captains)
        assigned_player_ids = set()
        for squad in active_squads:
            assigned_player_ids.update(squad.players.values_list('id', flat=True))

        # 4. Isolate only the remaining unassigned field players
        remaining_pool = [p for p in all_checked_in if p.id not in assigned_player_ids]

        # 5. Extract target squad size configuration out of browser parameters (default to 4-man block)
        squad_size_target = request.GET.get('team_size', '4')
        squad_size = int(squad_size_target) if squad_size_target.isdigit() else 4

        fmt = str(active_round.game_format or '').strip()
        is_team_chicago = fmt in ('9_TEAM_CHICAGO', 'team_chicago_points_9')

        if is_team_chicago:
            spread = _auto_fill_team_chicago_squads(active_squads, remaining_pool, squad_size)
            messages.success(
                request,
                f"⚡ Team Chicago auto-group complete! Filled squads targeting {squad_size} players each, "
                f"balancing Chicago points (team quota spread: {spread} pts)."
            )
        else:
            random.shuffle(remaining_pool)

            # 6. Fill up existing squads WITHOUT touching their captains or hole assignments
            for squad in active_squads:
                while squad.players.count() < squad_size and remaining_pool:
                    squad.players.add(remaining_pool.pop(0))
                squad.save()

            # 7. Symmetrical spillover loop for any lingering trailing headcounts
            while remaining_pool:
                for squad in active_squads:
                    if remaining_pool:
                        squad.players.add(remaining_pool.pop(0))
                        squad.save()

            messages.success(request,
                             f"⚡ Auto-Grouping Successful! Filled existing squads using a target of {squad_size} players per team while preserving your hole assignments.")
    return redirect('/admin-dashboard/')


# @login_required
def admin_scramble_overview(request):
    # Manual administrative authentication security shield block
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('scorecard:login')

    active_round = GolfRound.objects.filter(is_active=True).first()
    compiled_squads = []
    unassigned_players = []

    if active_round:
        # Fetch all squads generated for today's active match session
        db_squads = Squad.objects.filter(round=active_round).order_by('starting_hole__hole_number')

        for squad in db_squads:
            squad_members = squad.players.all().order_by('-is_captain', 'name')

            # Map cart arrangements visually within the squad row loop
            cart_groups = []
            paired_ids = set()

            for player in squad_members:
                if player.id in paired_ids:
                    continue

                partner = player.riding_partner
                # If they have a cart mate riding along on this exact same squad row, bind them
                if partner and partner in squad_members:
                    cart_groups.append({
                        'type': 'Cart Pair 🚗',
                        'players': [player, partner]
                    })
                    paired_ids.add(player.id)
                    paired_ids.add(partner.id)
                else:
                    cart_groups.append({
                        'type': 'Solo Rider 🛴',
                        'players': [player]
                    })
                    paired_ids.add(player.id)

            compiled_squads.append({
                'squad_obj': squad,
                'captain': squad_members.filter(is_captain=True).first(),
                'headcount': squad_members.count(),
                'cart_groups': cart_groups,
                'starting_hole': squad.starting_hole.hole_number if squad.starting_hole else "TBD"
            })

        # Defensive check: Isolate any checked-in player left behind without a squad row assignment
        assigned_player_ids = HoleScore.objects.filter(round=active_round).values_list('player_id', flat=True)
        unassigned_players = Player.objects.filter(is_playing_today=True).exclude(
            id__in=Squad.objects.filter(round=active_round).values_list('players__id', flat=True)
        )

    context = {
        'round': active_round,
        'compiled_squads': compiled_squads,
        'unassigned_count': len(unassigned_players),
        'unassigned_players': unassigned_players,
    }
    return render(request, 'scorecard/admin_scramble_overview.html', context)


def clear_cart_pairings_action(request):
    # SECURITY MATRIX: Blocks unauthorized or logged-out browser sessions
    if not request.user.is_authenticated or not (request.user.is_staff or request.user.is_superuser):
        return redirect('/login/')

    # Clear player-level cart links used by scramble / team chicago pairing UI
    cleared = Player.objects.filter(riding_partner__isnull=False).update(riding_partner=None)
    messages.success(
        request,
        f"💥 Cleared cart pairings for today's field ({cleared} player link(s) reset)."
    )

    return redirect('/admin-dashboard/')


# 🟢 PATH HOOK: HANDLES THE ADMIN SIDE-POT FORM DATA SUBMISSIONS
@login_required
def save_side_pots(request, round_id):
    if not request.user.is_staff:
        return redirect('/login/')

    if request.method == 'POST':
        target_round = get_object_or_404(GolfRound, id=round_id)

        # Pull the text values directly from the admin dashboard fields
        target_round.skins_winners_text = request.POST.get('skins_text', '').strip()
        target_round.closest_pin_text = request.POST.get('pin_text', '').strip()

        # Save explicitly to the database round row session
        target_round.save(update_fields=['skins_winners_text', 'closest_pin_text'])
        messages.success(request, "Side pot notes updated successfully!")

    return redirect('scorecard:tournament_leaderboard')


@csrf_exempt
@login_required
def toggle_captain_status_ajax(request):
    if not request.user.is_staff:
        return JsonResponse({'status': 'failed', 'error': 'Unauthorized access'}, status=403)

    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            data = json.loads(body_unicode)

            player_id = data.get('player_id')
            player = get_object_or_404(Player, id=player_id)

            # Flips the boolean state natively in the database row
            player.is_captain = not player.is_captain
            player.save(update_fields=['is_captain'])

            return JsonResponse({
                'status': 'success',
                'is_captain': player.is_captain,
                'player_name': player.name
            })
        except Exception as e:
            return JsonResponse({'status': 'failed', 'error': str(e)}, status=400)

    return JsonResponse({'status': 'failed', 'message': 'Invalid HTTP method structure'}, status=400)


@csrf_exempt
@login_required
def assign_scramble_hole_ajax(request):
    if not request.user.is_staff:
        return JsonResponse({'status': 'failed', 'error': 'Unauthorized'}, status=403)

    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            data = json.loads(body_unicode)

            player_id = data.get('player_id')
            hole_number = data.get('hole_number')

            active_round = GolfRound.objects.filter(is_active=True).first()
            player = get_object_or_404(Player, id=player_id)

            if not active_round:
                return JsonResponse({'status': 'failed', 'error': 'No active round'}, status=400)

            # If a hole number is provided, create/update the squad and attach the captain
            if hole_number and str(hole_number).isdigit():
                hole_obj = get_object_or_404(Hole, hole_number=int(hole_number))

                # Clean out any old squad this hole number was assigned to first
                Squad.objects.filter(round=active_round, starting_hole=hole_obj).delete()

                # Clean out any old squad this specific captain was leading today
                Squad.objects.filter(round=active_round, scorekeeper=player).delete()

                # Determine the next sequential squad number
                next_num = Squad.objects.filter(round=active_round).count() + 1

                # Create the squad shell with this captain as scorekeeper
                new_squad = Squad.objects.create(
                    round=active_round,
                    starting_hole=hole_obj,
                    squad_number=next_num,
                    scorekeeper=player
                )
                new_squad.players.add(player)
                new_squad.save()

                return JsonResponse({'status': 'success', 'message': f'Hole {hole_number} assigned'})
            else:
                # If hole is cleared, dismantle the squad shell
                Squad.objects.filter(round=active_round, scorekeeper=player).delete()
                return JsonResponse({'status': 'success', 'message': 'Hole assignment cleared'})

        except Exception as e:
            return JsonResponse({'status': 'failed', 'error': str(e)}, status=400)

    return JsonResponse({'status': 'failed', 'message': 'Invalid method'}, status=400)


@staff_member_required
def reset_scramble_tournament_action(request):
    if request.method == "POST":
        # 1. Locate and permanently delete the current active round container row
        active_round = GolfRound.objects.filter(is_active=True).first()
        if active_round:
            fmt = str(active_round.game_format or '').strip().lower()
            # Apply next-round adjustments from today's results before wiping scores (once only)
            if not active_round.metrics_finalized:
                if fmt in ("chicago_points_18", "18_ind_chicago"):
                    apply_18_chicago_quota_updates(active_round)
                    messages.success(
                        request,
                        "18-Hole Chicago quotas updated for next round based on today's +/- to quota."
                    )
                elif fmt in ("9_team_chicago", "team_chicago_points_9"):
                    apply_9_team_chicago_quota_updates(active_round)
                    messages.success(
                        request,
                        "9-Hole Team Chicago quotas updated for next round based on today's +/- to quota."
                    )
                elif fmt in ("18_hole_mens_league", "mens_league", "18_gross_net"):
                    apply_mens_handicap_updates(active_round)
                    messages.success(
                        request,
                        "Men's league handicaps updated for next round based on today's net vs par."
                    )
                elif fmt == "9_womens_league":
                    apply_womens_handicap_updates(active_round)
                    messages.success(
                        request,
                        "Ladies league handicaps updated for next round based on today's net scores."
                    )

            # Symmetrical database cascading lookups will automatically clear HoleScores and Squads
            active_round.delete()
            messages.success(request, "💥 Active tournament round session completely erased from database columns.")

        # 2. Directly clear out checked-in markers on all active members to reset the field roster
        Player.objects.all().update(is_playing_today=False, is_captain=False, riding_partner=None)

        # 3. Instantiate a fresh, clean tournament container row for your next scramble game
        GolfRound.objects.create(
            course_name="PRGC Championship Course",
            is_active=True,
            game_format=""  # Empty string to satisfy database constraints cleanly
        )

        messages.success(request,
                         "🔄 Fresh tournament round initialized successfully! All fields reset to pristine states.")
    return redirect('scorecard:admin_dashboard')


# ━ 🟢 RE-INJECTED HOOK: DISMANTLE SQUAD ACTION CONTROLLER ━
@staff_member_required
@require_POST
def dismantle_squad_action(request, squad_id):
    """
    Dismantles an active tournament squad row cleanly by its database primary ID,
    automatically freeing up its assigned captain and starting hole space back to the dashboard pools.
    """
    squad = get_object_or_404(Squad, id=squad_id)
    squad_num = squad.squad_number

    # Symmetrical cascading rules handle freeing up the players automatically
    squad.delete()

    messages.success(request, f"💥 Squad #{squad_num} benched and dismantled successfully.")
    return redirect('scorecard:admin_dashboard')


# ━ 🟢 RE-INJECTED HOOK: MANUAL SQUAD CREATE RENDERER ━
@staff_member_required
def manual_squad_create_view(request):
    """
    Fallback manual constructor form layout processing matrix for managers to
    manually patch up specific team rows if automated shufflers aren't used.
    """
    active_round = GolfRound.objects.filter(is_active=True).first()
    if not active_round:
        active_round = GolfRound.objects.create(course_name="PRGC Championship Course", is_active=True)

    if request.method == 'POST':
        form = ManualSquadForm(request.POST)
        if form.is_valid():
            squad = form.save(commit=False)
            squad.round = active_round

            existing_squads_count = Squad.objects.filter(round=active_round).count()
            squad.squad_number = existing_squads_count + 1

            if not squad.starting_hole:
                squad.starting_hole = Hole.objects.filter(
                    hole_number=squad.squad_number if squad.squad_number <= 18 else 1
                ).first()

            # 💡 FIX: Extract the designated captain/scorekeeper from the form field data
            # Assumes your form field name is 'scorekeeper'. Change to 'captain' if that's your form field name.
            squad.scorekeeper = form.cleaned_data.get('scorekeeper')

            squad.save()
            selected_players = form.cleaned_data.get('players')
            squad.players.set(selected_players)

            messages.success(request, f"📢 Squad #{squad.squad_number} hand-configured and saved successfully!")
            return redirect('scorecard:admin_dashboard')
    else:
        form = ManualSquadForm()

    return render(request, 'scorecard/manual_squad.html', {'form': form})



@login_required
def player_scorecard_scramble_view(request, hole_number=1):
    active_round = GolfRound.objects.filter(is_active=True).first()
    player_profile = resolve_player_for_user(request.user)

    active_squad = None
    if active_round:
        # Optional staff override: ?squad=<id>
        squad_param = request.GET.get('squad')
        if squad_param and str(squad_param).isdigit() and request.user.is_staff:
            active_squad = Squad.objects.filter(
                round=active_round, id=int(squad_param)
            ).select_related('scorekeeper', 'starting_hole').prefetch_related('players').first()

        if not active_squad and player_profile:
            active_squad = Squad.objects.filter(
                round=active_round
            ).filter(
                Q(players=player_profile) | Q(scorekeeper=player_profile)
            ).select_related('scorekeeper', 'starting_hole').prefetch_related('players').distinct().first()

        # Staff with no personal squad: open the first active scramble squad
        if not active_squad and request.user.is_staff:
            active_squad = Squad.objects.filter(
                round=active_round
            ).select_related('scorekeeper', 'starting_hole').prefetch_related('players').order_by(
                'squad_number'
            ).first()

    # Shotgun start redirect when landing without a hole / on hole 1 by default
    try:
        hole_number = int(hole_number) if hole_number is not None else 1
    except (ValueError, TypeError):
        hole_number = 1

    if active_squad and active_squad.starting_hole:
        start_h = active_squad.starting_hole.hole_number
        full_route = list(range(start_h, 10)) + list(range(1, start_h))
        # First visit to /play/ often lands on hole 1 — send captain to their tee
        if request.method == 'GET' and request.resolver_match and request.resolver_match.url_name in (
            'player_scorecard_start', 'player_scorecard_base'
        ):
            return redirect('scorecard:player_scorecard_scramble', hole_number=start_h)
    else:
        full_route = list(range(1, 10))

    if hole_number not in full_route:
        hole_number = full_route[0]

    hole = get_object_or_404(Hole, hole_number=hole_number)
    try:
        idx = full_route.index(hole_number)
    except ValueError:
        idx = 0
        hole_number = full_route[0]
        hole = get_object_or_404(Hole, hole_number=hole_number)

    next_hole = full_route[(idx + 1) % len(full_route)]
    prev_hole = full_route[(idx - 1) % len(full_route)]
    is_final_hole = idx == len(full_route) - 1

    # Captain (or staff) may enter the team score
    is_scorecard_editable = False
    if active_squad and active_squad.scorekeeper:
        if request.user.is_staff:
            is_scorecard_editable = True
        elif player_profile and active_squad.scorekeeper_id == player_profile.id:
            is_scorecard_editable = True
        elif active_squad.scorekeeper.user_id and active_squad.scorekeeper.user_id == request.user.id:
            is_scorecard_editable = True

    teammates = []
    if active_squad:
        for p in active_squad.players.all().order_by('name'):
            if not active_squad.scorekeeper or p.id != active_squad.scorekeeper_id:
                teammates.append(p)

    if request.method == 'POST':
        direction = request.POST.get('action', 'next')

        if not is_scorecard_editable:
            messages.error(request, "Only the team captain (or staff) can enter scramble scores.")
        elif active_squad:
            strokes_raw = request.POST.get('score')
            squad_members = list(active_squad.players.all())
            # Ensure captain is included even if not in M2M yet
            if active_squad.scorekeeper and active_squad.scorekeeper not in squad_members:
                squad_members.append(active_squad.scorekeeper)

            if strokes_raw and str(strokes_raw).isdigit():
                gross_strokes = int(strokes_raw)
                for member in squad_members:
                    HoleScore.objects.update_or_create(
                        round=active_round, hole=hole, player=member,
                        defaults={'gross_value': gross_strokes, 'net_value': 0}
                    )
            else:
                HoleScore.objects.filter(
                    round=active_round, hole=hole, player__in=squad_members
                ).delete()

        if direction == 'prev':
            return redirect('scorecard:player_scorecard_scramble', hole_number=prev_hole)
        if direction == 'finish':
            return redirect('/leaderboard/?format=9_hole_scramble')
        return redirect('scorecard:player_scorecard_scramble', hole_number=next_hole)

    current_team_score = ""
    prior_to_par = 0
    prior_holes_scored = 0
    if active_squad and active_squad.scorekeeper and active_round:
        existing_score = HoleScore.objects.filter(
            round=active_round, hole=hole, player=active_squad.scorekeeper
        ).first()
        if existing_score and existing_score.gross_value:
            current_team_score = existing_score.gross_value

        # Running +/- excludes current hole so the dropdown can add it live
        prior_scores = HoleScore.objects.filter(
            round=active_round,
            player=active_squad.scorekeeper,
            gross_value__isnull=False,
            gross_value__gt=0,
        ).exclude(hole=hole).select_related('hole')
        for scored in prior_scores:
            hole_par = scored.hole.par if scored.hole and scored.hole.par else 4
            prior_to_par += int(scored.gross_value) - int(hole_par)
            prior_holes_scored += 1

    # Squad picker for staff testing multiple teams
    all_squads = []
    if request.user.is_staff and active_round:
        all_squads = list(
            Squad.objects.filter(round=active_round).select_related('scorekeeper').order_by('squad_number')
        )

    context = {
        'current_hole': hole,
        'hole_number': hole_number,
        'next_hole': next_hole,
        'prev_hole': prev_hole,
        'round': active_round,
        'squad': active_squad,
        'teammates': teammates,
        'is_final_hole': is_final_hole,
        'is_scorecard_editable': is_scorecard_editable,
        'current_team_score': current_team_score,
        'prior_to_par': prior_to_par,
        'prior_holes_scored': prior_holes_scored,
        'all_squads': all_squads,
        'is_staff_viewer': request.user.is_staff,
    }
    return render(request, 'scorecard/player_scorecard_scramble.html', context)



