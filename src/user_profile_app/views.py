from django.shortcuts import render, redirect

from django.views.generic.edit import View, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile
from .forms import UserProfileForm

from common.services import get_object_data, create_object, check_object_is_none

from common.mixins import AuthorPermissionsMixin
from common.redirect_mixins import RedirectMixin, IdentifyRequestUserMixin


class MyProfileView(LoginRequiredMixin, DetailView):
    template_name = "user_profile_app/my_profile.html"
    context_object_name = "user_profile_info"

    def get_object(self, queryset=None):
        obj = get_object_data(model=UserProfile, user=self.request.user)
        return obj


class UserProfileView(LoginRequiredMixin, IdentifyRequestUserMixin, DetailView):
    model = UserProfile
    template_name = "user_profile_app/user_profile.html"
    redirect_url = "../my_profile/"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.get_object()
        context["profile"] = get_object_data(model=self.model, user=context["user"])
        return context


class CreateProfileView(LoginRequiredMixin, RedirectMixin, View):
    model = UserProfile
    form = UserProfileForm()
    template_name = "user_profile_app/create_profile.html"
    success_url = "../my_profile/"
    redirect_url = "../my_profile/"

    def get(self, request):
        return render(request, self.template_name, {
            "form": self.form,
        })

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            create_object(UserProfile, user=request.user, **form.cleaned_data)
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {"form": self.form})

    def get_object(self):
        profile = get_object_data(model=self.model, user=self.request.user)
        return profile


class UpdateProfileView(LoginRequiredMixin, AuthorPermissionsMixin, UpdateView):
    model = UserProfile
    template_name = "user_profile_app/update_profile.html"
    fields = ["profile_photo", "country", "about"]
    success_url = "../../my_profile"
    context_object_name = "user"


class DeleteProfileView(LoginRequiredMixin, AuthorPermissionsMixin, DeleteView):
    model = UserProfile
    template_name = "user_profile_app/delete_profile.html"
    context_object_name = "profile"
    success_url = "../../my_profile"
