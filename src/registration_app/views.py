from django.shortcuts import render


def home(request):
    return render(request, "registration_app/home.html", {})
