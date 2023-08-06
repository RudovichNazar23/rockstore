from django.urls import path
from .views import my_profile_view, CreateProfileView, UpdateProfileView

urlpatterns = [
    path("my_profile/", my_profile_view, name="my_profile"),
    path("create_profile/", CreateProfileView.as_view(), name="create_profile"),
    path("update_profile/<int:pk>", UpdateProfileView.as_view(), name="update_profile")
]
