from django.urls import path

from .views import CreatePostView, MyPostsListView, PostView, UpdatePostView, DeletePostView

urlpatterns = [
    path("create_post/", CreatePostView.as_view(), name="create_post"),
    path("my_posts/", MyPostsListView.as_view(), name="my_posts"),
    path("post/<int:pk>/", PostView.as_view(), name="post"),
    path("update_post/<int:pk>", UpdatePostView.as_view(), name="update_post"),
    path("delete_post/<int:pk>", DeletePostView.as_view(), name="delete_post"),
]
