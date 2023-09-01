from django.http import Http404
from .services import get_object_data, get_or_create_object


class AuthorPermissionsMixin:
    def has_permissions(self):
        return self.get_object().user == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


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
