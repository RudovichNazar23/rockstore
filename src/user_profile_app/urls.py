from django.urls import path

from .views import MyProfileView, CreateProfileView, UpdateProfileView, UserProfileView, DeleteProfileView

app_name = "user_profile_app"

urlpatterns = [
    path("my_profile/", MyProfileView.as_view(), name="my_profile"),
    path("create_profile/", CreateProfileView.as_view(), name="create_profile"),
    path("update_profile/<int:pk>/", UpdateProfileView.as_view(), name="update_profile"),
    path("<int:pk>/", UserProfileView.as_view(), name="user_profile"),
    path("delete_profile/<int:pk>/", DeleteProfileView.as_view(), name="delete_profile"),
]
