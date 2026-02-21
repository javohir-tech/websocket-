from django.shortcuts import render
# //////////////////////// REST FRAMEWORK ////////////////////////
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated , AllowAny
# ///////////////////////// Models ///////////////////////////////
from .models import User
# //////////////////////// Serializers ///////////////////////////
from .serializers import SingUpSerializer

class singUpView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SingUpSerializer


# Create your views here.
