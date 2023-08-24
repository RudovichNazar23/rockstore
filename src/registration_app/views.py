
from django.views.generic.list import ListView
from django.contrib.auth.views import LogoutView

from post_app.models import Category


class HomePageView(ListView):
    model = Category
    template_name = "registration_app/home.html"
    context_object_name = "categories"


class Logout(LogoutView):
    redirect_field_name = "/"

