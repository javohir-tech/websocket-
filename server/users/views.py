from django.shortcuts import render

# //////////////////////// REST FRAMEWORK ////////////////////////
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

# ///////////////////////// Models ///////////////////////////////
from .models import User

# //////////////////////// Serializers ///////////////////////////
from .serializers import SingUpSerializer, SingInSerializer


class SingUpView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SingUpSerializer


class SingInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SingInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        tokens = user.token()
        return Response(
            {
                "success": True,
                "message": "you are have been login",
                "data": {
                    "id": user.id,
                    "username": user.username,
                    "last_login": user.last_login,
                    "created": user.created,
                    "tokens ": {
                        "access": str(tokens.get("access_token")),
                        "refresh_token": str(tokens.get("refresh_token")),
                    },
                },
            },
            status=status.HTTP_200_OK,  
        )


# Create your views here.
