from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile

from common.services import get_object_data


@login_required
def my_profile_view(request):
    user_profile_data = get_object_data(model=UserProfile, user=request.user)
    return render(request, "user_profile_app/my_profile.html", {
        "user_profile_info": user_profile_data,
    })

