from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
import json


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.group_name = f"chat_{self.room_name}"

        if self.scope["user"].is_anonymous:
            await self.close()
            return

        await self.channel_layer.group_add(self.group_name, self.room_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.room_name)

    async def receive(self, text_data=None, bytes_data=None):
        data = json.load(text_data)
        message = data["message"]

        await self.save_message(self.room_name, message)
        await self.channel_layer.send(
            self.group_name,
            {
                "type": "chat_message",
                "message": message,
                "author": self.scope["user"].username,
            },
        )

    async def chat_message(self, event):
        await self.send(
            text_data=json.dumps(
                {"message": event["message"], "author": event["author"]}
            )
        )

    @database_sync_to_async
    def save_message(self, room_name, content):
        Message.objects.create(
            room=room_name, author=self.scope["user"], content=content
        )
