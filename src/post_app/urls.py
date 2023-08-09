from django.urls import path

from .views import CreatePostView, MyPostsView

urlpatterns = [
    path("create_post/", CreatePostView.as_view(), name="create_post"),
    path("my_posts/", MyPostsView.as_view(), name="my_posts"),
]
