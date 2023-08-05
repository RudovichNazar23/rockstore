from django.urls import path
from .views import my_profile_view, CreateProfileView

urlpatterns = [
    path("my_profile/", my_profile_view, name="my_profile"),
    path("create_profile/", CreateProfileView.as_view(), name="create_profile"),
]
