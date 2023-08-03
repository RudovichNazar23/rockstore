from django.shortcuts import render
from post_app.models import Categorie

from common import services


def home(request):
    categories = services.get_all_objects(Categorie)
    return render(request, "registration_app/home.html", {"categories": categories})

