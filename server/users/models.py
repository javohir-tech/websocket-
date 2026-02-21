import uuid
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True, max_length=128)

    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }

    def __str__(self):
        return self.username


# Create your models here.
