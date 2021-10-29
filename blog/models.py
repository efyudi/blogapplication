from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.shortcuts import reverse


class PostModel(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name="liked_by")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_home')
    
    def total_likes(self):
        return self.liked_by.count()


class Comments(models.Model):
    body = models.TextField()
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.body
