from django.urls import path

from .views import (
    CreatePostView,
    MyPostsListView,
    PostView,
    UpdatePostView,
    DeletePostView,
    CategoryPostListView,
    CreateCommentView,
    PostCommentsView,
    UpdateCommentView,
    DeleteCommentView,
    MyCommentsView,
    UserCommentsView,
)

urlpatterns = [
    path("create_post/", CreatePostView.as_view(), name="create_post"),
    path("my_posts/", MyPostsListView.as_view(), name="my_posts"),
    path("post/<int:pk>/", PostView.as_view(), name="post"),
    path("update_post/<int:pk>", UpdatePostView.as_view(), name="update_post"),
    path("delete_post/<int:pk>", DeletePostView.as_view(), name="delete_post"),
    path("category/<str:category>/", CategoryPostListView.as_view(), name="posts_by_category"),
    path("create_comment/<int:id>/", CreateCommentView.as_view(), name="create_comment"),
    path("post/comments/<int:id>/", PostCommentsView.as_view(), name="post_comments"),
    path("post/update_comment/<int:pk>/", UpdateCommentView.as_view(), name="update_comment"),
    path("post/delete_comment/<int:pk>/", DeleteCommentView.as_view(), name="delete_comment"),
    path("my_comments/", MyCommentsView.as_view(), name="my_comments"),
    path("user_comments/<int:id>/", UserCommentsView.as_view(), name="user_comments"),
]
