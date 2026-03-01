from django.urls import path
from .views import ChatView, ConversationListView

urlpatterns = [
    path("chat/<uuid:pk>/history/", ChatView.as_view()),
    path("chats/", ConversationListView.as_view()),
]
