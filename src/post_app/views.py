from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from django.views.generic.edit import View, UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import CreatePostForm, CreateCommentForm
from .models import Post, Comment, Repost, Like

from common.services import create_object, get_queryset, get_object_data, check_is_anonymous_user, check_object_is_none, get_or_create_object
from common.mixins import LikePostMixin

from common.context_data_mixins import UserContextDataMixin, ContextDataMixin
from common.redirect_mixins import RedirectMixin, IdentifyRequestUserMixin
from common.permission_mixins import AuthorPermissionsMixin


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "post_app/create_post.html"
    success_url = "/posts/my_posts/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MyPostsListView(LoginRequiredMixin, UserContextDataMixin, ListView):
    model = Post
    template_name = "post_app/my_posts.html"
    context_object_name = "posts"


class UserPostsView(LoginRequiredMixin, IdentifyRequestUserMixin, UserContextDataMixin, ListView):
    model = Post
    template_name = "post_app/user_posts.html"
    redirect_url = "/posts/my_posts/"
    context_object_name = "posts"


class PostView(DetailView):
    model = Post
    template_name = "post_app/post.html"
    context_object_name = "post"


class UpdatePostView(LoginRequiredMixin, AuthorPermissionsMixin, UpdateView):
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
    success_url = "/posts/my_posts/"
    permission_denied_message = "Error"


class DeletePostView(LoginRequiredMixin, AuthorPermissionsMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = "/posts/my_posts/"
    template_name = "post_app/delete_post.html"


class CategoryPostListView(LoginRequiredMixin, ContextDataMixin, ListView):
    model = Post
    template_name = "post_app/posts_by_category.html"
    context_object_name = "posts"

    def get_object(self):
        obj = get_queryset(model=self.model, category__name=self.kwargs["category"])
        return obj


class CreateCommentView(LoginRequiredMixin, RedirectMixin, View):
    model = Comment
    template_name = "post_app/create_comment.html"

    def get(self, request, id: int):
        form = CreateCommentForm()
        return render(request=request, template_name=self.template_name, context={
            "post": get_object_data(model=Post, id=self.kwargs["id"]),
            "form": form,
        })

    def post(self, request, id: int):
        form = CreateCommentForm(request.POST)
        post = get_object_data(model=Post, id=self.kwargs["id"])

        if form.is_valid():
            create_object(model=Comment, user=request.user, post=post, **form.cleaned_data)
            return redirect(f"../../{post.id}/comments/")

    def get_object(self):
        post = get_object_data(model=Post, id=self.kwargs["id"])
        post_comment = get_object_data(model=Comment, user=self.request.user, post=post)
        return post_comment

    def get_redirect_url(self):
        url = f"../../update_comment/{self.get_object().pk}/"
        return url


class PostCommentsView(LoginRequiredMixin, ContextDataMixin, ListView):
    model = Comment
    template_name = "post_app/post_comments.html"
    context_object_name = "comments"

    def get_object(self):
        obj = get_queryset(model=self.model, post=self.kwargs["pk"])
        return obj


class UpdateCommentView(LoginRequiredMixin, AuthorPermissionsMixin, UpdateView):
    model = Comment
    template_name = "post_app/update_comment.html"
    fields = ["description"]
    context_object_name = "comment"
    success_url = "/posts/my_comments/"


class DeleteCommentView(LoginRequiredMixin, AuthorPermissionsMixin, DeleteView):
    model = Comment
    context_object_name = "comment"
    template_name = "post_app/delete_comment.html"
    success_url = "/posts/my_comments/"


class MyCommentsView(LoginRequiredMixin, UserContextDataMixin, ListView):
    model = Comment
    template_name = "post_app/my_comments.html"
    context_object_name = "comments"


class UserCommentsView(LoginRequiredMixin, IdentifyRequestUserMixin, UserContextDataMixin, ListView):
    model = Comment
    template_name = "post_app/user_comments.html"
    context_object_name = "comments"
    redirect_url = "/posts/my_comments/"


class CreateRepostView(LoginRequiredMixin, RedirectMixin, View):
    model = Repost
    redirect_url = "/posts/my_reposts/"

    def post(self, request, id: int):
        post = get_object_data(model=Post, id=id)
        create_object(model=self.model, user=request.user, post=post)
        post.reposts.add(self.request.user)
        return redirect(self.request.META.get("HTTP_REFERER"))

    def get_object(self):
        repost = get_object_data(model=self.model, post=self.kwargs["id"], user=self.request.user)
        return repost


class MyRepostsView(LoginRequiredMixin, UserContextDataMixin, ListView):
    model = Repost
    template_name = "post_app/my_reposts.html"
    context_object_name = "posts"


class UserRepostsView(LoginRequiredMixin, IdentifyRequestUserMixin, UserContextDataMixin, ListView):
    model = Repost
    template_name = "post_app/user_reposts.html"
    context_object_name = "posts"
    redirect_url = "/posts/my_reposts/"


class DeleteRepostView(LoginRequiredMixin, AuthorPermissionsMixin, DeleteView):
    model = Repost
    template_name = "post_app/delete_repost.html"
    context_object_name = "repost"
    success_url = "/posts/my_reposts/"

    def form_valid(self, form):
        self.object.post.reposts.remove(self.request.user)
        self.object.delete()
        return HttpResponseRedirect(self.success_url)


class LikePostView(LoginRequiredMixin, LikePostMixin, View):
    model = Post

    def post(self, request, id: int):
        self.add_or_remove_user()
        self.change_like_value(model=Like)
        return redirect(self.get_redirect_url())

