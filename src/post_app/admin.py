from django.contrib import admin
from .models import Post, Comment, Repost, Category, Like

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Repost)
admin.site.register(Category)
