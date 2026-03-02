from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
import json
from django.db.models import Q


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

        await self.mark_unread_as_read()

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
                "is_read": msg.is_read,
                "created_at": msg.created_at.isoformat(),
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
    def mark_unread_as_read(self):
        Message.objects.filter(receiver=self.me.id, sender_id = self.target_id, is_read=False).update(is_read=True)


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

        self.known_partner_ids = await self.get_known_partner_ids()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_unread(self, event):
        sender_id = event["sender_id"]
        is_new_partner = sender_id not in self.known_partner_ids

        if is_new_partner:
            self.known_partner_ids.add(sender_id)

        await self.send(
            text_data=json.dumps(
                {
                    "last_message": event["message"],
                    "partner": event["sender"],
                    "partner_id": event["sender_id"],
                    "is_read": event["is_read"],
                    "last_message_time": event["created_at"],
                    "is_new_partner": is_new_partner,
                }
            )
        )

    @database_sync_to_async
    def get_known_partner_ids(self):
        messages = Message.objects.filter(
            Q(sender=self.me) | Q(receiver=self.me)
        ).values_list("sender_id", "receiver_id")

        ids = set()

        for sender_id, reveiver_id in messages:
            ids.add(sender_id)
            ids.add(reveiver_id)
        ids.discard(self.me.id)
        return ids

