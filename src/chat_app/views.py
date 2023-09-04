from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse

from itertools import chain

from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import ChatRoom, Message

from common.services import get_object_data, create_object, get_queryset
from common.redirect_mixins import ChatRedirectMixin
from common.mixins import ChatMemberMixin
from common.context_data_mixins import UserContextDataMixin


class CreateChatRoomView(LoginRequiredMixin, ChatRedirectMixin, View):
    model = ChatRoom

    def get(self, request, pk: int):
        return HttpResponse(status=404)

    def post(self, request, pk: int):
        member = get_object_data(model=User, pk=pk)
        create_object(model=self.model, creator=self.request.user, member=member)
        return redirect("/")


class ChatRoomView(LoginRequiredMixin, ChatMemberMixin, DetailView):
    model = ChatRoom
    template_name = "chat_app/chat_room.html"
    context_object_name = "room"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = get_queryset(model=Message, chatroom=context["room"])
        return context


class MyChatroomListView(LoginRequiredMixin, UserContextDataMixin, ListView):
    model = ChatRoom
    context_object_name = "chats"
    template_name = "chat_app/my_chat_list.html"

    def get_data(self):
        chats = chain(get_queryset(model=self.model, creator=self.request.user),
                      get_queryset(model=self.model, member=self.request.user)
                      )
        return chats


class DeleteChatRoomView(LoginRequiredMixin, ChatMemberMixin, DeleteView):
    model = ChatRoom
    template_name = "chat_app/delete_chat.html"
    context_object_name = "chat"
    success_url = "/"
