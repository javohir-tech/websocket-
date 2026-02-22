from django.db import models
from users.models import User

class Message(models.Model):
    room = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.room} - {self.author}: {self.content}"


# Create your models here.
