from django.urls import path

from .views import CreateChatRoomView, ChatRoomView, MyChatroomListView, DeleteChatRoomView

urlpatterns = [
    path("create_chat_room/<int:pk>/", CreateChatRoomView.as_view(), name="create_chat_room"),
    path("room/<int:pk>/", ChatRoomView.as_view(), name="chat_room"),
    path("my_chat_rooms/", MyChatroomListView.as_view(), name="my_chat_rooms"),
    path("delete_chat_room/<int:pk>/", DeleteChatRoomView.as_view(), name="delete_chat_room"),
]
