
from django.views.generic.list import ListView
from django.contrib.auth.views import LogoutView

from post_app.models import Category, Post
from common.services import get_queryset, get_all_objects


class HomePageView(ListView):
    model = Category
    template_name = "registration_app/home.html"
    context_object_name = "categories"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["popular_posts"] = get_all_objects(model=Post)
        return context


class Logout(LogoutView):
    redirect_field_name = "/"

