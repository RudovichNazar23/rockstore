from django.urls import path

from .views import CreatePostView, MyPostsListView, PostView

urlpatterns = [
    path("create_post/", CreatePostView.as_view(), name="create_post"),
    path("my_posts/", MyPostsListView.as_view(), name="my_posts"),
    path("post/<int:pk>/", PostView.as_view(), name="post"),
]
