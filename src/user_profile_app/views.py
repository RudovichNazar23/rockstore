from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import View

from .models import UserProfile
from .forms import UserProfileForm

from common.services import get_object_data, create_object


@login_required
def my_profile_view(request):
    user_profile_data = get_object_data(model=UserProfile, user=request.user)
    return render(request, "user_profile_app/my_profile.html", {
        "user_profile_info": user_profile_data,
    })


class CreateProfileView(View):
    form = UserProfileForm()
    template_name = "user_profile_app/create_profile.html"
    success_url = "../my_profile/"

    def get(self, request):
        return render(request, self.template_name, {"form": self.form})

    def post(self, request):
        form = UserProfileForm(request.POST)

        if form.is_valid():
            create_object(UserProfile, user=request.user, **form.cleaned_data)
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {"form": self.form})

