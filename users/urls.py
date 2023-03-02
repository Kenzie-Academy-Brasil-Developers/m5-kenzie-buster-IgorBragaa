from django.urls import path
from .views import UserView, UserRetriverView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("users/", UserView.as_view()),
]
