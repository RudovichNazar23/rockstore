from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    name = models.CharField(max_length=155, default="")

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):

    CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # related_name --> post_creator
    title = models.CharField(max_length=100)
    item_photo = models.ImageField(upload_to="post_item_photos/")
    brand = models.CharField(max_length=100)
    item_model = models.CharField(max_length=100)
    date_of_manufacture = models.DateField()
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="category")
    price = models.IntegerField()
    possibility_of_exchange = models.CharField(choices=CHOICES)
    description = models.TextField()
    active = models.CharField(choices=CHOICES, default="Yes")
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.TextField()
    date_created = models.DateField(auto_now=True)

    class Meta:
        ordering = ("date_created", )

    def __str__(self):
        return f"{self.user} - {self.post.title}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)


class Repost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


