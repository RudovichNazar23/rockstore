from django.urls import path

from .views import CreatePostView

urlpatterns = [
    path("create_post/", CreatePostView.as_view(), name="create_post"),
]
