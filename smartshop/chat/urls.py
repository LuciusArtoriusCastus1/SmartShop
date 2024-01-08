from django.urls import path

from .views import *

urlpatterns = [
    path('new/<slug:product>/chat_room/', NewChatRoom.as_view(), name='new_chat_room'),
    path('detail/<int:room>/chat/', ChatRoomDetail.as_view(), name='chat_detail'),
    path('delete/<int:chat_id>/chat/', DeleteChatRoom.as_view(), name='delete_chat'),

]
