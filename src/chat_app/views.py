from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .models import ChatRoom, Message

from common.services import get_object_data, create_object, get_queryset


class CreateChatRoomView(View):
    def post(self, request, pk: int):
        member = get_object_data(model=User, pk=pk)
        create_object(model=ChatRoom, creator=self.request.user, member=member)
        return redirect("/")


class ChatRoomView(View):
    def get(self, request, pk: int):
        room = get_object_data(model=ChatRoom, pk=pk)
        messages = get_queryset(model=Message, chatroom=room)[:11]
        return render(request=request, template_name="chat_app/chat_room.html", context={
            "room": room,
            "messages": messages
        })


class DeleteChatRoomView:
    pass
