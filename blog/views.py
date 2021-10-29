from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls.base import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import PostModel, Comments
from .forms import CommentsForm


def like_post(request, pk):
    post = get_object_or_404(PostModel, id=pk)
    liked_by = post.liked_by.all()
    
    if request.user not in liked_by:
        post.liked_by.add(request.user)
    else:
        post.liked_by.remove(request.user)
    
    
    return HttpResponseRedirect(reverse("blog_home"))


def post_comment(request, pk):
    if request.method == "POST":
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            post = get_object_or_404(PostModel, id=pk)
            user = get_object_or_404(User, id=request.user.pk)
            comment = Comments(body=request.POST["body"], commented_by= user, post=post)
            comment.save()
    
    return HttpResponseRedirect(reverse("blog_home"))


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


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comments
    fields = ['body']

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
        context['comments'] = Comments.objects.all()
        context['comment_form'] = CommentsForm()
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

