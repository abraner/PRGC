from django.contrib import admin
from django.contrib.auth.views import LogoutView
# 🟢 1. Make sure Hole is imported alongside your other models
from .models import Hole, Player, Squad, GolfRound, PayoutSetting

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
