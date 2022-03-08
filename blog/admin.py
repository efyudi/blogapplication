from django.contrib import admin
from .models import PostModel, Comments
# Register your models here.

admin.site.register(PostModel)
admin.site.register(Comments)