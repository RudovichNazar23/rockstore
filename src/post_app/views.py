from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.edit import View, UpdateView, DeleteView
from django.contrib.auth.models import User

from .forms import CreatePostForm, CreateCommentForm
from .models import Post, Categorie, Comment, Repost

from common.services import create_object, get_queryset, get_object_data, check_is_anonymous_user, check_object_is_none
from common.permissions import AuthorPermissionsMixin


class CreatePostView(View):
    template_name = "post_app/create_post.html"

    def get(self, request):
        form = CreatePostForm()
        return render(request=request, template_name=self.template_name, context={"form": form})

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
        posts = get_queryset(self.model, user=request.user)
        return render(request, template_name=self.template_name, context={"posts": posts})


class UserPostsView(View):
    template_name = "post_app/user_posts.html"

    def get(self, request, username: str):
        user = get_object_data(model=User, username=username)
        user_posts = get_queryset(model=Post, user__username=username)
        return render(request=request, template_name=self.template_name, context={
            "posts": user_posts,
            "user": user,
        })


class PostView(View):
    template_name = "post_app/post.html"
    model = Post

    def get(self, request, pk: int):
        post = get_object_data(model=self.model, pk=pk)
        return render(request, template_name=self.template_name, context={"post": post})


class UpdatePostView(AuthorPermissionsMixin, UpdateView):
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
    success_url = "../../my_posts"
    permission_denied_message = "Error"


class DeletePostView(AuthorPermissionsMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = "../../my_posts"
    template_name = "post_app/delete_post.html"


class CategoryPostListView(View):
    template_name = "post_app/posts_by_category.html"

    def get(self, request, category: str):
        category = get_object_data(model=Categorie, name=category)
        posts = get_queryset(model=Post, category__name=category)
        return render(request, template_name=self.template_name, context={"posts": posts})


class CreateCommentView(View):
    template_name = "post_app/create_comment.html"

    def get(self, request, id: int):
        post = get_object_data(model=Post, id=id)
        post_comment = get_object_data(model=Comment, user=request.user, post=post)

        if check_object_is_none(obj=post_comment):
            form = CreateCommentForm()
            return render(request=request, template_name=self.template_name, context={
                "post": post,
                "form": form,
            })
        else:
            return redirect(f"../../update_comment/{post_comment.pk}/")

    def post(self, request, id: int):
        form = CreateCommentForm(request.POST)
        post = get_object_data(model=Post, id=id)

        if form.is_valid():
            create_object(model=Comment, user=request.user, post=post, **form.cleaned_data)
            return redirect(f"../../{post.id}/comments/")


class PostCommentsView(View):
    template_name = "post_app/post_comments.html"

    def get(self, request, id: int):
        post_comments = get_queryset(model=Comment, post=id)
        return render(request=request, template_name=self.template_name, context={"comments": post_comments})


class UpdateCommentView(AuthorPermissionsMixin, UpdateView):
    model = Comment
    template_name = "post_app/update_comment.html"
    fields = ["description"]
    context_object_name = "comment"
    success_url = "../../../my_comments/"


class DeleteCommentView(AuthorPermissionsMixin, DeleteView):
    model = Comment
    context_object_name = "comment"
    template_name = "post_app/delete_comment.html"
    success_url = "../../../my_comments/"


class MyCommentsView(View):
    template_name = "post_app/my_comments.html"

    def get(self, request):
        comments = get_queryset(Comment, user=request.user)
        return render(request=request, template_name=self.template_name, context={"comments": comments})


class UserCommentsView(View):
    template_name = "post_app/user_comments.html"

    def get(self, request, id: int):
        user = get_object_data(model=User, id=id)
        user_comments = get_queryset(model=Comment, user=id)
        if user == request.user:
            return redirect("../../my_comments/")
        else:
            return render(request=request, template_name=self.template_name, context={
                "comments": user_comments,
                "user": user,
            })


class CreateRepostView(View):
    def post(self, request, id: int):
        post = get_object_data(model=Post, id=id)
        create_object(model=Repost, user=request.user, post=post)
        return redirect("/")


class MyRepostsView(View):
    template_name = "post_app/my_reposts.html"

    def get(self, request):
        reposts = get_queryset(model=Repost, user=request.user)
        return render(request=request, template_name=self.template_name, context={"posts": reposts})


class UserRepostsView(View):
    template_name = "post_app/user_reposts.html"

    def get(self, request, id: int):
        user = get_object_data(model=User, id=id)
        reposts = get_queryset(model=Repost, user=id)
        return render(request=request, template_name=self.template_name, context={
            "reposts": reposts,
            "user": user,
        })


class DeleteRepostView(AuthorPermissionsMixin, DeleteView):
    model = Repost
    template_name = "post_app/delete_repost.html"
    context_object_name = "repost"
    success_url = ""
