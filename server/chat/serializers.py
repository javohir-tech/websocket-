from rest_framework import serializers
from .models import Message

class ChatSerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField()
    
    class Meta:
        model = Message
        fields = '__all__'