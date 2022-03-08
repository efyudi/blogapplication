from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    profile_pic = models.ImageField(default="default.jpg", upload_to="profile_pics")
    bio = models.TextField(max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} Profile"

