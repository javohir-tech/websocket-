from django.urls import path
from .views import ChatView

urlpatterns = [
    path("chat/<str:room_name>/history/", ChatView.as_view()),
]
