import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import ChatRoom, Message
from common.services import get_object_data, create_object


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_pk = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = 'chat_%s' % self.room_pk

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_message(username, room, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = get_object_data(model=User, username=username)
        room = get_object_data(model=ChatRoom, pk=room)

        create_object(model=Message, author=user, chatroom=room, content=message)

