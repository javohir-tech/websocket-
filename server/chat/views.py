from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import ChatSerializer, AllChatsSerializer
from rest_framework.response import Response
from django.db.models import Q, Count, Subquery, OuterRef, Max
from users.models import User


class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        messages = Message.objects.filter(
            receiver_id__in=[self.request.user.id, pk],
            sender_id__in=[self.request.user.id, pk],
        ).order_by("created_at")
        serializer = ChatSerializer(messages, many=True)
        return Response(serializer.data)


class ConversationListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        me = self.request.user

        sent = (
            Message.objects.filter(sender=me)
            .values("receiver_id")
            .annotate(last_time=Max("created_at"))
        )
        receivered = (
            Message.objects.filter(receiver=me)
            .values("sender_id")
            .annotate(last_time=Max("created_at"))
        )

        partners_time = {}
        for row in sent:
            pid = row["receiver_id"]
            partners_time[pid] = max(
                partners_time.get(pid, row["last_time"]), row["last_time"]
            )
        for row in receivered:
            pid = row["sender_id"]
            partners_time[pid] = max(
                partners_time.get(pid, row["last_time"]), row["last_time"]
            )

        partners_time.pop(me.id, None)

        partner_ids = list(partners_time.keys())

        partners = {u.id: u for u in User.objects.filter(id__in=partner_ids)}

        messages = Message.objects.filter(
            Q(sender=me, receiver_id__in=partner_ids)
            | Q(sender_id__in=partner_ids, receiver=me)
        ).order_by("-created_at")

        last_messages = {}

        for msg in messages:
            pid = msg.receiver_id if msg.sender_id == me.id else msg.sender_id

            if pid not in last_messages:
                last_messages[pid] = msg

            if len(last_messages) == len(partner_ids):
                break

        unread_count = dict(
            Message.objects.filter(receiver=me, is_read=False)
            .values("sender_id")
            .annotate(c=Count("id"))
            .values_list("sender_id", "c")
        )

        conversitions = []

        for partner_id, last_msg in last_messages.items():

            partner = partners.get(partner_id, None)

            if not partner:
                continue

            conversitions.append(
                {
                    "partner": partner.username,
                    "partner_id": partner_id,
                    "last_message_time": last_msg.content,
                    "created_at": last_msg.created_at.isoformat(),
                    "unread_count": unread_count.get(partner_id, 0),
                    "last_message_me": last_msg.sender == me,
                }
            )

        conversitions.sort(key=lambda x: x["last_message_time"], reverse=True)

        return Response(conversitions)
