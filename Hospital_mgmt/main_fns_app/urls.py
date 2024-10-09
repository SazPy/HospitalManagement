# main_fns_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='main_fns_app/password_change_done.html'), name='password_change_done'),
    path('', views.dashboard, name='home'),  # Redirect root URL to dashboard/home
]
