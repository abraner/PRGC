from django.urls import path
from . import views

app_name = 'scorecard'

urlpatterns = [
    # Bridges the blank root path directly to the login box
    path('', views.login_view, name='home_redirect'),

    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('play/hole/', views.player_scorecard, name='player_scorecard_base'),
    path('play/hole/<int:hole_number>/', views.player_scorecard, name='player_scorecard'),
    path('play/', views.player_scorecard, name='player_scorecard_start'),

    path('update-score/', views.update_score_ajax, name='update_score_ajax'),
    path('leaderboard/', views.tournament_leaderboard, name='leaderboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/generate/', views.generate_squads_action, name='generate_squads'),
    path('play/summary/', views.player_round_summary, name='player_summary'),
    path('play/finish/', views.finish_round_update_quotas, name='finish_round'),
    path('update-handicap/', views.update_handicap_ajax, name='update_handicap_ajax'),
    path('play/fetch-scores/<int:hole_number>/', views.fetch_latest_scores_ajax, name='fetch_latest_scores'),


    path('admin-dashboard/add-player/', views.add_player_action, name='add_player'),
    path('register/', views.register_view, name='register_view'),

    path('admin-dashboard/reset/', views.reset_tournament_action, name='reset_tournament'),
    path('admin-dashboard/all-members/', views.view_all_members, name='all_members'),
    # Ensure name match is explicit
    path('admin-dashboard/toggle-playing/', views.toggle_playing_status_ajax, name='toggle_playing_ajax'),
    path('admin-dashboard/delete-player/<int:player_id>/', views.delete_player_action, name='delete_player'),
    path('admin-dashboard/edit-player/<int:player_id>/', views.edit_player_view, name='edit_player'),
    path('admin-dashboard/manual-squad/', views.manual_squad_create_view, name='manual_squad'),
    path('admin-dashboard/dismantle-squad/<int:squad_id>/', views.dismantle_squad_action, name='dismantle_squad'),
    path('admin-dashboard/payout-settings/', views.update_payout_settings_view, name='payout_settings'),
    path('admin-dashboard/skins-verifier/', views.skins_verification_panel, name='skins_verifier'),
    path('admin-dashboard/update-format/', views.update_format_ajax, name='update_format_ajax'),


    # Keep your consolidated reset action route intact:
    path('admin-dashboard/reset-slate/', views.reset_tournament_action, name='reset_tournament_action'),

    # 🛠️ NEW SAFETY ALIAS CATCH: Prevents any old template references anywhere from crashing the dashboard!
    path('admin-dashboard/finalize-handicaps/', views.reset_tournament_action, name='finalize_handicaps_action'),
    path('scorecard/save-stroke-api/', views.save_stroke_api, name='save_stroke_api'),
    path('tournament-leaderboard/', views.tournament_leaderboard, name='tournament_leaderboard'),

    path('finalize-round/<int:round_id>/', views.finalize_tournament_round, name='finalize_tournament_round'),

    # Scramble match routing rules paths
    path('admin-scramble-overview/', views.admin_scramble_overview, name='admin_scramble_overview'),
    path('generate-scramble-squads/<int:round_id>/', views.generate_random_scramble_squads, name='generate_random_scramble_squads'),
    path('admin-dashboard/clear-carts/', views.clear_cart_pairings_action, name='clear_cart_pairings'),
    path('leaderboard/save-side-pots/<int:round_id>/', views.save_side_pots, name='save_side_pots'),
     path('admin-dashboard/toggle-captain/', views.toggle_captain_status_ajax, name='toggle_captain_status_ajax'),

    # ⛳ Ensure this line exists exactly as written with matching view attributes
    path('admin-dashboard/assign-scramble-hole/', views.assign_scramble_hole_ajax, name='assign_scramble_hole_ajax'),
    path('admin-dashboard/reset-game/', views.reset_scramble_tournament_action, name='reset_scramble_tournament_action'),
    path('admin-dashboard/dismantle-squad/<int:squad_id>/', views.dismantle_squad_action, name='dismantle_squad_action'),
    path('scramble-scorecard/<int:hole_number>/', views.player_scorecard_scramble_view, name='player_scorecard_scramble'),

]



