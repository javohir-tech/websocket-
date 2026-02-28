from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.me = self.scope["user"]
        self.target_id = self.scope["url_route"]["kwargs"]["user_id"]

        if self.me.is_anonymous:
            await self.close()
            return

        self.room_name = self.get_room_name(self.me.id, self.target_id)
        self.group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        messages = await self.get_chat_history()

        for msg in messages:
            await self.send(text_data=json.dumps(msg))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        content = data.get("message", "").strip()

        if not content:
            return

        msg = await self.save_massage(content)

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_message",
                "message": content,
                "sender": self.me.username,
                "sender_id": str(self.me.id),
                "created_at": msg.created_at.strftime("%H:%M"),
            },
        )

        await self.channel_layer.group_send(
            f"unread_{self.target_id}",
            {
                "type": "send_unread",
                "message": content,
                "sender": self.me.username,
                "sender_id": str(self.me.id),
                "created_at": msg.created_at.strftime("%H:%M"),
            },
        )

    async def chat_message(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "message": event["message"],
                    "sender": event["sender"],
                    "sender_id": event["sender_id"],
                    "created_at": event["created_at"],
                }
            )
        )

    # ── Helpers ──────────────────────────────────────────────
    @staticmethod
    def get_room_name(id1, id2):
        ids = sorted([str(id1), str(id2)])
        return f"{ids[0]}_{ids[1]}"

    @database_sync_to_async
    def save_massage(self, content):
        return Message.objects.create(
            sender_id=self.me.id, receiver_id=self.target_id, content=content
        )

    @database_sync_to_async
    def get_chat_history(self):
        messages = (
            Message.objects.filter(
                sender_id__in=[self.me.id, self.target_id],
                receiver_id__in=[self.me.id, self.target_id],
            )
            .select_related("sender")
            .order_by("created_at")[:50]
        )

        for msg in messages:
            if msg.is_read == False:
                msg.is_read = True
                msg.save()

        return [
            {
                "message": m.content,
                "sender": m.sender.username,
                "sender_id": str(m.sender_id),
                "created_at": m.created_at.strftime("%H:%M"),
            }
            for m in messages
        ]


class UnReadChat(AsyncWebsocketConsumer):

    async def connect(self):
        self.me = self.scope["user"]

        if self.me.is_anonymous:
            await self.close()
            return

        self.room_name = self.me.id
        self.group_name = f"unread_{self.room_name}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        unread_messages = await self.get_unread_chats()

        for m in unread_messages:
            await self.send(text_data=json.dumps(m))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_unread(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "message": event["message"],
                    "sender": event["sender"],
                    "sender_id": event["sender_id"],
                    "created_at": event["created_at"],
                }
            )
        )

    @database_sync_to_async
    def get_unread_chats(self):
        messages = Message.objects.filter(receiver=self.me.id, is_read=False).order_by(
            "created_at"
        )

        return [
            {
                "message": m.content,
                "sender": m.sender.username,
                "sender_id": str(m.sender.id),
                "created_at": m.created_at.strftime("%H:%M"),
            }
            for m in messages
        ]
