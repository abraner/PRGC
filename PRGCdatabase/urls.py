from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "PRGCdatabase"
urlpatterns = [
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('home/', views.home, name='home'),
    ]