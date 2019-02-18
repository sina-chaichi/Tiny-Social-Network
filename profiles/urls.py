from django.urls import path
from django.contrib.auth import views as views_auth
from . import views_profile

app_name = 'profiles'

urlpatterns = [
    path('ورود/',
    views_auth.LoginView.as_view(template_name='profiles/login.html'),
    name='ورود'),
    path('خروج/', views_auth.LogoutView.as_view(), name='خروج'),
    path('ثبت/', views_profile.SignUp.as_view(), name='ثبت'),


]
