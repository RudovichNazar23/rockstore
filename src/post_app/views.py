from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.edit import View

from .forms import CreatePostForm
from .models import Post
from common.services import create_object, get_queryset


class CreatePostView(View):
    template_name = "post_app/create_post.html"

    def get(self, request):
        form = CreatePostForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CreatePostForm(request.POST, request.FILES)

        if form.is_valid():
            create_object(model=Post, user=request.user, **form.cleaned_data)
            return redirect("../create_post/")
        else:
            messages.error(request, message="Something goes wrong...")
            return redirect("../create_post/")


class MyPostsView(View):
    model = Post
    template_name = "post_app/my_posts.html"

    def get(self, request):
        posts = get_queryset(self.model, user=request.user)
        return render(request, self.template_name, {"posts": posts})
