from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UserRegister, ProfileDetailView, ProfileUpdateView
from .forms import CustomUserRegisterForm

urlpatterns = [
    path('register/', UserRegister.as_view(), name='user_register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/user_login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/user_logout.html'), name='user_logout'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='user_profile'),
    path('profile/update/<int:pk>', ProfileUpdateView.as_view(), name='update_profile'),
]