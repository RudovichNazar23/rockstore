from django.urls import path

from .views import HomePageView, Logout

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("logout", Logout.as_view(), name="logout"),
]
