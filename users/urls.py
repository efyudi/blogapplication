from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UserRegister, ProfileDetailView, ProfileUpdateView
from .forms import CustomUserRegisterForm
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('register/', UserRegister.as_view(), name='user_register'),

    path('login/', auth_views.LoginView.as_view(template_name='users/user_login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),

    path('profile/<int:pk>', ProfileDetailView.as_view(), name='user_profile'),
    path('profile/update/<int:pk>', ProfileUpdateView.as_view(), name='update_profile'),

    path('password-reset/', PasswordResetView.as_view(template_name="users/password_reset.html"), name="password_reset"),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password-reset/complete', PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
    
]