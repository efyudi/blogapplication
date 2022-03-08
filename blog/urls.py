from django.urls import path

from .views import (
    BlogHomeView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    BlogHomeListAndCreate,
    CommentDeleteView,
    CommentUpdateView,
    like_post,
    post_comment,
)


urlpatterns = [
    #path('', BlogHomeView.as_view(), name='blog_home'),
    #path('create/', PostCreateView.as_view(), name='create_post'),
    path('', BlogHomeListAndCreate.as_view(), name='blog_home'),

    path('update/<int:pk>', PostUpdateView.as_view(), name='update_post'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path('like/<int:pk>', like_post, name="like_post"),

    path('comment/<int:pk>', post_comment, name="post_comment"),
    path('comment/delete/<int:pk>', CommentDeleteView.as_view(), name="delete_comment"),
    path('comment/update/<int:pk>', CommentUpdateView.as_view(), name="update_comment"),
]