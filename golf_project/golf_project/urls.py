from django.contrib import admin
from django.urls import path, include
from scorecard import views as scorecard_views # Import scorecard views directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scorecard.urls')),

    # Global fallback so {% url 'reset_tournament' %} will resolve without the scorecard: prefix
    path('admin-dashboard/reset/', scorecard_views.reset_tournament_action, name='reset_tournament'),
]





