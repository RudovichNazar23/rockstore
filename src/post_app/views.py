from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.edit import View

from .forms import CreatePostForm
from .models import Post
from common.services import create_object, get_queryset, get_object_data, check_is_anonymous_user, check_object_is_none


class CreatePostView(View):
    template_name = "post_app/create_post.html"

    def get(self, request):
        form = CreatePostForm()
        return render(request, template_name=self.template_name, context={"form": form})

    def post(self, request):
        form = CreatePostForm(request.POST, request.FILES)

        if form.is_valid():
            create_object(model=Post, user=request.user, **form.cleaned_data)
            return redirect("../create_post/")
        else:
            messages.error(request, message="Something goes wrong...")
            return redirect("../create_post/")


class MyPostsListView(View):
    model = Post
    template_name = "post_app/my_posts.html"

    def get(self, request):
        if check_is_anonymous_user(request.user):
            return redirect("../../common/page_404")
        posts = get_queryset(self.model, user=request.user)
        return render(request, template_name=self.template_name, context={"posts": posts})


class PostView(View):
    template_name = "post_app/post.html"
    model = Post

    def get(self, request, pk: int):
        post = get_object_data(model=self.model, pk=pk)
        if check_object_is_none(obj=post):
            return redirect("../../../common/page_404")
        return render(request, template_name=self.template_name, context={"post": post})
