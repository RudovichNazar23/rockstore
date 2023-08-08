from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    name = models.CharField(max_length=155, default="")

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):

    POSSIBILITY_OF_EXCHANGE_CHOICES = [
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
    possibility_of_exchange = models.CharField(choices=POSSIBILITY_OF_EXCHANGE_CHOICES)
    description = models.TextField()
    rating = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # the person who leaves the comment
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # under what post
    description = models.TextField()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)


class Repost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


