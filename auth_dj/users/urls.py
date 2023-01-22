from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
    path(
        'login/', 
        LoginView.as_view(template_name='users/login.html'),
        name='login')
]