from django.http import HttpResponseRedirect, Http404
from .services import get_object_data, check_object_is_none

from django.contrib.auth.models import User


class BaseRedirectMixin:
    redirect_url = "/"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_redirect_url(self):
        return self.redirect_url

    def get_object(self):
        user = get_object_data(model=User, id=self.kwargs["pk"])
        return user


class RedirectMixin(BaseRedirectMixin):

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not check_object_is_none(obj):
            return HttpResponseRedirect(redirect_to=self.get_redirect_url())
        else:
            return super().dispatch(request, *args, **kwargs)


class ChatRedirectMixin(BaseRedirectMixin):
    def dispatch(self, request, *args, **kwargs):
        if get_object_data(model=self.model, creator=self.request.user, member=self.get_object()) or \
                get_object_data(model=self.model, creator=self.get_object(), member=self.request.user):
            return HttpResponseRedirect(redirect_to="/chat_rooms/my_chat_rooms/")
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


