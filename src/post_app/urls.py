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
    UserPostsView,
    CreateRepostView,
    MyRepostsView,
    UserRepostsView,
    DeleteRepostView,
    LikePostView,
)

app_name = "post_app"

urlpatterns = [
    path("create_post/", CreatePostView.as_view(), name="create_post"),
    path("my_posts/", MyPostsListView.as_view(), name="my_posts"),
    path("user_posts/<int:pk>/", UserPostsView.as_view(), name="user_posts"),
    path("post/<int:pk>/", PostView.as_view(), name="post"),
    path("update_post/<int:pk>/", UpdatePostView.as_view(), name="update_post"),
    path("delete_post/<int:pk>/", DeletePostView.as_view(), name="delete_post"),
    path("category/<str:category>/", CategoryPostListView.as_view(), name="posts_by_category"),
    path("post/<int:id>/create_comment/", CreateCommentView.as_view(), name="create_comment"),
    path("post/<int:pk>/comments/", PostCommentsView.as_view(), name="post_comments"),
    path("post/update_comment/<int:pk>/", UpdateCommentView.as_view(), name="update_comment"),
    path("post/delete_comment/<int:pk>/", DeleteCommentView.as_view(), name="delete_comment"),
    path("my_comments/", MyCommentsView.as_view(), name="my_comments"),
    path("user_comments/<int:pk>/", UserCommentsView.as_view(), name="user_comments"),
    path("post/<int:id>/create_repost/", CreateRepostView.as_view(), name="create_repost"),
    path("my_reposts/", MyRepostsView.as_view(), name="my_reposts"),
    path("user_reposts/<int:pk>/", UserRepostsView.as_view(), name="user_reposts"),
    path("delete_repost/<int:pk>/", DeleteRepostView.as_view(), name="delete_repost"),
    path("like_post/<int:id>/", LikePostView.as_view(), name="like_post"),
]
