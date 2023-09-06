from django.db import models
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_creator")
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_member")

    def __str__(self):
        return f"{self.creator} - {self.member}"


class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} - {self.chatroom}"

    class Meta:
        ordering = ("date_created",)


