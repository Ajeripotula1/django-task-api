from django.urls import path
from .views import UserRegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # issue JWT token (acc and ref) when user logs in w/ cred
    TokenRefreshView # Get a new access Token w/ refresh token
)

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='user-register'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh')
]
