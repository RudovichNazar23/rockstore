from django.urls import path

from .views import CreateChatRoomView, ChatRoomView

urlpatterns = [
    path("create_chat_room/<int:pk>/", CreateChatRoomView.as_view(), name="create_chat_room"),
    path("room/<int:pk>/", ChatRoomView.as_view(), name="chat_room"),
]
