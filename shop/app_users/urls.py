from django.urls import path
from .views import ProfileView, PasswordView


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/password', PasswordView.as_view(), name='password'),
]

