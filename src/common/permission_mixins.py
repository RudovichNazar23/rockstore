from django.http import Http404


class AuthorPermissionsMixin:
    def has_permissions(self):
        return self.get_object().user == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


class ChatMemberMixin(AuthorPermissionsMixin):
    def has_permissions(self):
        return self.request.user in (self.get_object().creator, self.get_object().member)
