from django.shortcuts import render


def page_404(request, *args, **kwargs):
    return render(request, "page_404.html", {}, status=404)
