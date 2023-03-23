from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer, PasswordSerializer
from rest_framework import status


class ProfileView(APIView):
    def get(self, request):
        user = CustomUser.objects.filter(email=self.request.user.email).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request):
        user = CustomUser.objects.filter(email=self.request.user.email).first()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            user.email = serializer.validated_data['email']
            user.fullName = serializer.validated_data['fullName']
            user.phone = serializer.validated_data['phone']
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PasswordView(APIView):

    def post(self, request):
        user = CustomUser.objects.filter(email=self.request.user.email).first()
        serializer = PasswordSerializer(user, data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AvatarView(APIView):

    def post(self, request):
        user = CustomUser.objects.filter(email=self.request.user.email).first()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            user.avatar = serializer.validated_data['avatar']
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
