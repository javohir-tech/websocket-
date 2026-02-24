from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import ChatSerializer
from rest_framework.response import Response


class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, room_name):
        messages = Message.objects.filter(room=room_name).order_by("created_at")
        serializer = ChatSerializer(messages, many=True)
        return Response(serializer.data)


# Create your views here.
