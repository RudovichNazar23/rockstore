from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from post_app.models import Categorie

from common import services


def home(request):
    categories = services.get_all_objects(Categorie)
    return render(request, "registration_app/home.html", {"categories": categories})


def logout_view(request):
    logout(request)
    return redirect("/")
