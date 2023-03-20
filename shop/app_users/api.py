from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    fields = ['fullName', 'email', 'phone', 'avatar']
    serializer_class = UserSerializer
