from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from django.contrib.auth.models import User
from .models import PostModel
from users.models import Profile


class BlogHomeView(ListView):
    template_name = 'blog/blog_home.html'
    model = PostModel
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create_post.html'
    model = PostModel
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogHomeListAndCreate(CreateView):
    template_name = 'blog/blog_home.html'
    model = PostModel
    fields = ['title', 'content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = PostModel.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'blog/update_post.html'
    model = PostModel
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'blog/delete_post.html'
    model = PostModel
    success_url = reverse_lazy('blog_home')

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

