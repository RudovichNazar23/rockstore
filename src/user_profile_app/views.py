from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import View, UpdateView, DeleteView

from .models import UserProfile
from .forms import UserProfileForm

from common.services import get_object_data, create_object, check_object_is_none
from common.mixins import AuthorPermissionsMixin, RedirectMixin, IdentifyRequestUserMixin


@login_required
def my_profile_view(request):
    user_profile_data = get_object_data(model=UserProfile, user=request.user)
    return render(request, "user_profile_app/my_profile.html", {
        "user_profile_info": user_profile_data,
    })


class UserProfileView(IdentifyRequestUserMixin, View):
    template_name = "user_profile_app/user_profile.html"
    model = UserProfile
    redirect_url = "../my_profile/"

    def get(self, request, id: int):
        profile = get_object_data(model=self.model, user=self.get_object())
        return render(request=request, template_name=self.template_name, context={
            "user": self.get_object(),
            "profile": profile
        })


class CreateProfileView(RedirectMixin, View):
    form = UserProfileForm()
    template_name = "user_profile_app/create_profile.html"
    success_url = "../my_profile/"
    model = UserProfile
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


class UpdateProfileView(AuthorPermissionsMixin, UpdateView):
    model = UserProfile
    template_name = "user_profile_app/update_profile.html"
    fields = ["profile_photo", "country", "about"]
    success_url = "../../my_profile"
    context_object_name = "user"


class DeleteProfileView(AuthorPermissionsMixin, DeleteView):
    model = UserProfile
    template_name = "user_profile_app/delete_profile.html"
    context_object_name = "profile"
    success_url = "../../my_profile"
