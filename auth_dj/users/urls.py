from django.urls import path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
    )
from django.urls.base import reverse_lazy
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),

    path('signup/', views.SignUp.as_view(), name='signup'),

    path(
        'logout/',
        LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
    path(
        'login/', 
        LoginView.as_view(template_name='users/login.html'),
        name='login'),
    
    
    path(
        'password-reset/', 
        PasswordResetView.as_view(template_name='users/password_reset.html',
        html_email_template_name='users/password_reset_email.html',
        success_url = reverse_lazy("users:password_reset_done")),
        name='password-reset'),

    path(
        'password-reset/done/',
        PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),

    path(
        'password-reset-confirm/<uidb64>/<token>/', 
        PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path(
        'password-reset-complete/',
        PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
    
]