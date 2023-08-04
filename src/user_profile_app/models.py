from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(null=True, blank=True, upload_to="users_profile_photos/")
    country = CountryField()
    about = models.TextField(max_length=155)

    def __str__(self):
        return f"{self.user}"

