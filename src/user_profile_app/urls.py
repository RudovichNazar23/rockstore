from django.urls import path
from .views import my_profile_view

urlpatterns = [
    path("my_profile/", my_profile_view, name="my_profile"),
]
