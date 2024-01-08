from django.urls import re_path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'chat/detail/(?P<room>\w+)/chat/', ChatConsumer.as_asgi()),
]
