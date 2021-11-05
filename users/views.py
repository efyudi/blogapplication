from django.contrib import messages
from django.contrib.auth.forms import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, DetailView, UpdateView
from django.shortcuts import render, reverse
from django.urls import reverse_lazy

from .forms import CustomUserRegisterForm
from .models import Profile


class UserRegister(FormView):
    template_name = 'users/user_register.html'
    form_class = CustomUserRegisterForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "User successfully registered!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('user_login')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/profile.html'
    model = User


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'users/update_profile.html'
    fields = ["profile_pic", "bio"]

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully!")
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('user_profile', kwargs={"pk":self.request.user.id})

