from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.edit import View, UpdateView, DeleteView

from .forms import CreatePostForm, CreateCommentForm
from .models import Post, Categorie, Comment
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
            return redirect("../my_posts/")
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


class UpdatePostView(UpdateView):
    model = Post
    fields = [
        "title",
        "item_photo",
        "brand",
        "item_model",
        "date_of_manufacture",
        "category",
        "price",
        "possibility_of_exchange",
        "description",
        "active"
    ]
    template_name = "post_app/update_post.html"
    context_object_name = "post"
    success_url = "../my_posts"


class DeletePostView(DeleteView):
    model = Post
    context_object_name = "post"
    success_url = "../my_posts"
    template_name = "post_app/delete_post.html"


class CategoryPostListView(View):
    template_name = "post_app/posts_by_category.html"

    def get(self, request, category: str):
        category = get_object_data(model=Categorie, name=category)

        if check_object_is_none(obj=category):
            return redirect("../../../common/page_404")
        else:
            posts = get_queryset(model=Post, category__name=category)
            return render(request, template_name=self.template_name, context={"posts": posts})


class CreateCommentView(View):
    template_name = "post_app/create_comment.html"

    def get(self, request, id: int):
        post = self.__get_post_by_id(post_id=id)
        form = CreateCommentForm()
        return render(request=request, template_name=self.template_name, context={
            "post": post,
            "form": form,
        })

    def post(self, request, id: int):
        form = CreateCommentForm(request.POST)
        post = self.__get_post_by_id(post_id=id)

        if form.is_valid():
            create_object(model=Comment, user=request.user, post=post, **form.cleaned_data)
            return redirect(f"../../post/comments/{post.id}")

    @staticmethod
    def __get_post_by_id(post_id: int):
        post = get_object_data(model=Post, id=post_id)
        if post is None:
            return redirect("../../common/page_404")
        else:
            return post


class PostCommentsView(View):
    template_name = "post_app/post_comments.html"

    def get(self, request, id: int):
        post_comments = get_queryset(model=Comment, post=id)
        return render(request=request, template_name=self.template_name, context={"post_comments": post_comments})


class UpdateCommentView(UpdateView):
    model = Comment
    template_name = "post_app/update_comment.html"
    fields = ["description"]
    context_object_name = "comment"
    success_url = "/"


class DeleteCommentView(DeleteView):
    model = Comment
    context_object_name = "comment"
    template_name = "post_app/delete_comment.html"
    success_url = "/"
