from django.urls import path

# //////////////////// VIEWS /////////////////////
from .views import SingUpView, SingInView

urlpatterns = [
    path("singup/", SingUpView.as_view()),
    path("singin/", SingInView.as_view()),
]
