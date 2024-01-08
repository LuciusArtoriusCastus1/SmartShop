import time

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import *


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room']
        self.room_group_name = 'chat_%s' % self.room_name
        print(self.room_group_name, '---------------------', self.room_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json, '================================')
        message_scope = text_data_json['message']
        creator_scope = self.scope['user']
        message = Message.objects.create(text=message_scope, creator=creator_scope, chat_room=ChatRoom.objects.get(id=self.scope['url_route']['kwargs']['room']))
        text = str(message.text)
        creator = str(message.creator)
        created_at = str(message.created_at)
        creator_name = str(message.creator.display_name)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'text': text,
                'creator': creator,
                'created_at': created_at,
                'creator_name': creator_name,
            },
        )

    def chat_message(self, event):
        text = event['text']
        creator = event['creator']
        created_at = event['created_at']
        creator_name = event['creator_name']
        print('================', text, creator, creator_name, created_at)

        self.send(text_data=json.dumps({
            'event': "Send",
            'text': text,
            'creator': creator,
            'created_at': created_at,
            'creator_name': creator_name,
        }))

