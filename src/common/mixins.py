from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User

from .services import check_object_is_none, get_object_data, get_or_create_object, get_queryset


class BaseRedirectMixin:
    redirect_url = "/"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_redirect_url(self):
        return self.redirect_url

    def get_object(self):
        user = get_object_data(model=User, id=self.kwargs["pk"])
        return user


class AuthorPermissionsMixin:
    def has_permissions(self):
        return self.get_object().user == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


class RedirectMixin(BaseRedirectMixin):

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not check_object_is_none(obj):
            return HttpResponseRedirect(redirect_to=self.get_redirect_url())
        else:
            return super().dispatch(request, *args, **kwargs)


class IdentifyRequestUserMixin(BaseRedirectMixin):

    def dispatch(self, request, *args, **kwargs):
        if self.user_is_request_user():
            return HttpResponseRedirect(redirect_to=self.get_redirect_url())
        else:
            return super().dispatch(request, *args, **kwargs)

    def user_is_request_user(self):
        return self.request.user == self.get_object()


class LikePostMixin:
    redirect_url = "/"
    model = None

    def add_or_remove_user(self):
        post_obj = self.get_object()

        if self.request.user in post_obj.liked.all():
            post_obj.liked.remove(self.request.user)
        else:
            post_obj.liked.add(self.request.user)

    def change_like_value(self, model):
        like, created = get_or_create_object(model=model, user=self.request.user, post_id=self.kwargs["id"])

        if not created:
            if like.value == "Like":
                like.value = "Unlike"
            else:
                like.value = "Like"
        like.save()

    def get_object(self):
        obj = get_object_data(model=self.model, id=self.kwargs["id"])
        return obj

    def get_redirect_url(self):
        self.redirect_url = self.request.META.get("HTTP_REFERER")
        return self.redirect_url


class UserContextDataMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.get_user()
        context[self.context_object_name] = self.get_data()
        return context

    def get_user(self):
        if not self.kwargs:
            user = self.request.user
        else:
            user = self.get_object()
        return user

    def get_data(self):
        return get_queryset(model=self.model, user=self.get_user())


class ContextDataMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = self.get_object()
        return context

    def get_object(self):
        return self
