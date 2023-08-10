from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import View, UpdateView
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import UserProfileForm

from common.services import get_object_data, create_object, check_object_is_none


@login_required
def my_profile_view(request):
    user_profile_data = get_object_data(model=UserProfile, user=request.user)
    return render(request, "user_profile_app/my_profile.html", {
        "user_profile_info": user_profile_data,
    })


@login_required
def user_profile_view(request, id: int):
    user = get_object_data(model=User, id=id)
    profile = get_object_data(model=UserProfile, user=user)

    if request.user == user:
        return my_profile_view(request)
    elif check_object_is_none(user):
        return redirect("../common/page_404")
    else:
        return render(request, "user_profile_app/user_profile.html", {
            "user": user,
            "profile": profile
        })


class CreateProfileView(View):
    form = UserProfileForm()
    template_name = "user_profile_app/create_profile.html"
    success_url = "../my_profile/"

    def get(self, request):
        user_profile = get_object_data(UserProfile, user=request.user)
        return render(request, self.template_name, {
            "form": self.form,
            "user_profile": user_profile
        })

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            create_object(UserProfile, user=request.user, **form.cleaned_data)
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {"form": self.form})


class UpdateProfileView(UpdateView):
    model = UserProfile
    template_name = "user_profile_app/update_profile.html"
    fields = ["profile_photo", "country", "about"]
    success_url = "../my_profile"
    context_object_name = "user"

