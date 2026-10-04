from django.contrib import admin
from django.contrib.auth.views import LogoutView
# 🟢 1. Make sure Hole is imported alongside your other models
from .models import Hole, Player, Squad, GolfRound, PayoutSetting, Cost

# Open Django Admin in the same tab; "View site" returns to the tournament control panel
admin.site.site_url = '/admin-dashboard/'


def _admin_logout(request, extra_context=None):
    """Log out of Django Admin and return to the PRGC admin dashboard."""
    defaults = {
        "extra_context": {
            **admin.site.each_context(request),
            "has_permission": False,
            **(extra_context or {}),
        },
        "next_page": "/admin-dashboard/",
    }
    request.current_app = admin.site.name
    return LogoutView.as_view(**defaults)(request)


admin.site.logout = _admin_logout

# 🟢 2. Register the Hole model so the table appears in the admin dashboard
admin.site.register(Hole)

# Keep your existing registrations below intact
admin.site.register(Player)
admin.site.register(Squad)
admin.site.register(GolfRound)
admin.site.register(PayoutSetting)


@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    """One Cost row. Game costs and the golf course amount are edited here."""

    fields = (
        'mens_league_18',
        'gross_net_18',
        'scramble_9',
        'team_chicago_9',
        'womens_league_9',
        'chicago_18',
        'golf_course_amount',
    )

    def has_add_permission(self, request):
        return not Cost.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        Cost.objects.get_or_create(pk=1)
        return super().changelist_view(request, extra_context=extra_context)
