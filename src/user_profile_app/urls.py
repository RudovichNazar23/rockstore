from django.urls import path
from .views import my_profile_view, CreateProfileView, UpdateProfileView, user_profile_view, DeleteProfileView

urlpatterns = [
    path("my_profile/", my_profile_view, name="my_profile"),
    path("create_profile/", CreateProfileView.as_view(), name="create_profile"),
    path("update_profile/<int:pk>", UpdateProfileView.as_view(), name="update_profile"),
    path("<int:id>", user_profile_view, name="user_profile"),
    path("delete_profile/<int:pk>/", DeleteProfileView.as_view(), name="delete_profile"),
]
