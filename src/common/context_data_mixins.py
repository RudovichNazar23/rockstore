from .services import get_queryset


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
