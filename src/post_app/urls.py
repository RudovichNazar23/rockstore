from django.urls import path

from django.contrib.auth.decorators import login_required


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
)

urlpatterns = [
    path("create_post/", login_required(CreatePostView.as_view()), name="create_post"),
    path("my_posts/", login_required(MyPostsListView.as_view()), name="my_posts"),
    path("user_posts/<int:id>/", login_required(UserPostsView.as_view()), name="user_posts"),
    path("post/<int:pk>/", login_required(PostView.as_view()), name="post"),
    path("update_post/<int:pk>/", login_required(UpdatePostView.as_view()), name="update_post"),
    path("delete_post/<int:pk>/", login_required(DeletePostView.as_view()), name="delete_post"),
    path("category/<str:category>/", login_required(CategoryPostListView.as_view()), name="posts_by_category"),
    path("post/<int:id>/create_comment/", login_required(CreateCommentView.as_view()), name="create_comment"),
    path("post/<int:id>/comments/", login_required(PostCommentsView.as_view()), name="post_comments"),
    path("post/update_comment/<int:pk>/", login_required(UpdateCommentView.as_view()), name="update_comment"),
    path("post/delete_comment/<int:pk>/", login_required(DeleteCommentView.as_view()), name="delete_comment"),
    path("my_comments/", login_required(MyCommentsView.as_view()), name="my_comments"),
    path("user_comments/<int:id>/", login_required(UserCommentsView.as_view()), name="user_comments"),
    path("post/<int:id>/create_repost/", login_required(CreateRepostView.as_view()), name="create_repost"),
    path("my_reposts/", login_required(MyRepostsView.as_view()), name="my_reposts"),
    path("user_reposts/<int:id>/", login_required(UserRepostsView.as_view()), name="user_reposts"),
    path("delete_repost/<int:pk>/", login_required(DeleteRepostView.as_view()), name="delete_repost"),
]
