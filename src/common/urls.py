from django.urls import path

from .views import page_404


urlpatterns = [
    path("page_404", page_404, name="page_404"),
]
