from django.urls import path

# //////////////////// VIEWS /////////////////////
from .views import singUpView

urlpatterns = [
    path("singup/", singUpView.as_view()),
]
