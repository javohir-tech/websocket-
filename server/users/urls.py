from django.urls import path

# //////////////////// VIEWS /////////////////////
from .views import SingUpView, SingInView, LogoutView, GetAllUsersView

urlpatterns = [
    path("singup/", SingUpView.as_view()),
    path("singin/", SingInView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("users/", GetAllUsersView.as_view()),
]
    