from django.contrib import admin
from .models import Post, Comment, Like, Repost, Categorie

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Repost)
admin.site.register(Categorie)
