from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User

from .services import check_object_is_none, get_object_data


class BaseRedirectMixin:
    redirect_url = "/"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_redirect_url(self):
        return self.redirect_url

    def get_object(self):
        user = get_object_data(model=User, id=self.kwargs["id"])
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

