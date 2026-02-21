from rest_framework import serializers
from .models import User

class SingUpSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only= True)
    
    class Meta :
        model = User
        fields = '__all__'
        
