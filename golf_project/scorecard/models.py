from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    name = models.CharField(max_length=100)
    handicap = models.IntegerField(default=0)
    new_handicap = models.IntegerField(default=0)

    member_id = models.CharField(max_length=20, unique=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_playing_today = models.BooleanField(default=False, verbose_name="Playing Today")

    chicago_points_18 = models.IntegerField(default=0, verbose_name="18 Hole Chicago Quota")
    team_chicago_points_9 = models.IntegerField(default=0, verbose_name="9 Hole Team Chicago Quota")
    ladies_league_handicap = models.IntegerField(default=0, verbose_name="Ladies League Handicap")

    # 🟢 9-HOLE SCRAMBLE TEAM BINDING
    is_captain = models.BooleanField(default=False, verbose_name="Team Captain")
    riding_partner = models.OneToOneField(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='cart_mate', verbose_name="Riding Partner (Same Cart)"
    )

    @property
    def team_chicago_quota(self):
        """Points required for 9-hole Team Chicago: the stored 9-hole field."""
        return int(self.team_chicago_points_9 or 0)

    # 💡 CLEANED: Removed duplicate save/str methods that were cluttering your file
    def save(self, *args, **kwargs):
        is_new = self.id is None
        super().save(*args, **kwargs)
        if is_new:
            self.member_id = f"GLF-{self.id}"
            super().save(update_fields=['member_id'])

    def __str__(self):
        return self.name


class Hole(models.Model):
    hole_number = models.IntegerField()
    par = models.IntegerField(default=4)
    handicap_index = models.IntegerField(default=1)

    class Meta:
        ordering = ['hole_number']

    def __str__(self):
        return f"Hole {self.hole_number} (Par {self.par})"


class GolfRound(models.Model):
    GAME_FORMAT_CHOICES = [
        ('18_GROSS_NET', '18-Hole Individual Gross/Net'),
        ('18_HOLE_MENS_LEAGUE', "18-Hole Men's Handicap League"),
        ('18_IND_CHICAGO', '18-Hole Individual Chicago Points'),
        ('9_TEAM_CHICAGO', '9-Hole Team Chicago Points'),
        ('9_WOMENS_LEAGUE', '9-Hole Women\'s League'),
        ('9_HOLE_SCRAMBLE', "Scramble Tournament (9 Holes)"),
    ]
    date_played = models.DateTimeField(auto_now_add=True)
    course_name = models.CharField(max_length=200, default="PRGC Course")
    game_format = models.CharField(max_length=30, choices=GAME_FORMAT_CHOICES, default='18_GROSS_NET')
    is_active = models.BooleanField(default=True)
    # Locks end-of-round quota/handicap updates so they cannot be applied twice
    metrics_finalized = models.BooleanField(default=False)
    # Men's league side-pot notes (closest-to-pin is often manual; skins can be auto-filled)
    skins_winners_text = models.TextField(blank=True, default="")
    closest_pin_text = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{self.course_name} - {self.get_game_format_display()} ({self.date_played.strftime('%Y-%m-%d')})"


class Squad(models.Model):
    round = models.ForeignKey(GolfRound, on_delete=models.CASCADE, related_name="squads")
    squad_number = models.IntegerField()
    starting_hole = models.ForeignKey(Hole, on_delete=models.PROTECT, related_name="starting_squads")
    players = models.ManyToManyField(Player, related_name="squads")
    scorekeeper = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True, related_name="managed_squads")

    def __str__(self):
        return f"Squad {self.squad_number} (Starts Hole {self.starting_hole.hole_number})"

    # 💡 AUTOMATED CAPTAIN SYNCHRONIZATION OVERRIDE
    def save(self, *args, **kwargs):
        # Check if the squad already exists to see who the former captain was
        if self.pk:
            try:
                old_squad = Squad.objects.get(pk=self.pk)
                old_captain = old_squad.scorekeeper
            except Squad.DoesNotExist:
                old_captain = None
        else:
            old_captain = None

        # Call standard save first so database relationships commit cleanly
        super().save(*args, **kwargs)

        # If the captain changed or was newly assigned
        if old_captain != self.scorekeeper:
            # Step A: Turn off the captain flag for the previous captain
            if old_captain:
                old_captain.is_captain = False
                old_captain.save(update_fields=['is_captain'])

            # Step B: Turn on the captain flag for the newly assigned scorekeeper
            if self.scorekeeper:
                self.scorekeeper.is_captain = True
                self.scorekeeper.save(update_fields=['is_captain'])


class HoleScore(models.Model):
    round = models.ForeignKey(GolfRound, on_delete=models.CASCADE, related_name="scores")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="hole_scores")
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE, related_name="player_scores")

    # FLEXIBLE FIELD SYSTEM: Holds whatever numerical value the current active game tracks
    gross_value = models.IntegerField(default=0)  # Stores Gross Strokes, Chicago points hit, etc.
    net_value = models.IntegerField(default=0)    # Stores calculated Net Strokes, Quota metrics, etc.

    class Meta:
        unique_together = ('round', 'player', 'hole')

    def __str__(self):
        return f"{self.player.name} - Hole {self.hole.hole_number}: {self.gross_value}"


class PayoutSetting(models.Model):
    entry_fee = models.DecimalField(max_digits=6, decimal_places=2, default=12.00)
    course_cut_per_player = models.DecimalField(max_digits=6, decimal_places=2, default=2.00)
    specialty_pot_percentage = models.IntegerField(default=10, help_text="Percentage of remainder for Skins/KP")

    skins_split_percentage = models.IntegerField(default=50)
    kp_split_percentage = models.IntegerField(default=50)

    # NEW FIELDS: Administrative slots to save game winners text
    skins_winners = models.CharField(max_length=255, default="", blank=True, help_text="Enter names or 'No skins won'")
    kp_winners = models.CharField(max_length=255, default="", blank=True, help_text="Enter names of closest to the hole winners")


    def __str__(self):
        return f"Payout Rules: Fee ${self.entry_fee} | Course ${self.course_cut_per_player}"


class Cost(models.Model):
    """One row of entry costs and the golf course amount, edited in Django admin."""

    mens_league_18 = models.DecimalField(
        max_digits=6, decimal_places=2, default=12.00,
        verbose_name="18-Hole Men's League cost",
    )
    gross_net_18 = models.DecimalField(
        max_digits=6, decimal_places=2, default=6.00,
        verbose_name="18-Hole Individual Gross/Net cost",
    )
    scramble_9 = models.DecimalField(
        max_digits=6, decimal_places=2, default=6.00,
        verbose_name="9-Hole Scramble cost",
    )
    team_chicago_9 = models.DecimalField(
        max_digits=6, decimal_places=2, default=6.00,
        verbose_name="9-Hole Team Chicago Points cost",
    )
    womens_league_9 = models.DecimalField(
        max_digits=6, decimal_places=2, default=6.00,
        verbose_name="9-Hole Women's League cost",
    )
    chicago_18 = models.DecimalField(
        max_digits=6, decimal_places=2, default=12.00,
        verbose_name="18-Hole Individual Chicago Points cost",
    )
    golf_course_amount = models.DecimalField(
        max_digits=6, decimal_places=2, default=2.00,
        verbose_name="Golf course amount",
    )

    class Meta:
        verbose_name = "Cost"
        verbose_name_plural = "Cost"

    def __str__(self):
        return "Game costs"

    @classmethod
    def amounts_for_format(cls, fmt):
        """Return (game cost, golf course amount) for the active game format."""
        row = cls.objects.order_by('pk').first()
        if row is None:
            row = cls.objects.create()
        key = str(fmt or '').strip()
        field = _COST_FIELD_BY_FORMAT.get(key) or _COST_FIELD_BY_FORMAT.get(key.lower(), 'mens_league_18')
        return getattr(row, field), row.golf_course_amount


# Model choice values and the older leaderboard names for the same games.
_COST_FIELD_BY_FORMAT = {
    '18_HOLE_MENS_LEAGUE': 'mens_league_18',
    '18_hole_mens_league': 'mens_league_18',
    'mens_league': 'mens_league_18',
    '18_GROSS_NET': 'gross_net_18',
    '18_gross_net': 'gross_net_18',
    '9_HOLE_SCRAMBLE': 'scramble_9',
    '9_hole_scramble': 'scramble_9',
    '9_TEAM_CHICAGO': 'team_chicago_9',
    '9_team_chicago': 'team_chicago_9',
    'team_chicago_points_9': 'team_chicago_9',
    '9_WOMENS_LEAGUE': 'womens_league_9',
    '9_womens_league': 'womens_league_9',
    '18_IND_CHICAGO': 'chicago_18',
    '18_ind_chicago': 'chicago_18',
    'chicago_points_18': 'chicago_18',
}



