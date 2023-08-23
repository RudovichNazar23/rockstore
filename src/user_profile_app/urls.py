from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import my_profile_view, CreateProfileView, UpdateProfileView, UserProfileView, DeleteProfileView

urlpatterns = [
    path("my_profile/", my_profile_view, name="my_profile"),
    path("create_profile/", login_required(CreateProfileView.as_view()), name="create_profile"),
    path("update_profile/<int:pk>/", login_required(UpdateProfileView.as_view()), name="update_profile"),
    path("<int:id>/", login_required(UserProfileView.as_view()), name="user_profile"),
    path("delete_profile/<int:pk>/", login_required(DeleteProfileView.as_view()), name="delete_profile"),
]
