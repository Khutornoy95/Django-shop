from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer


class ProfileView(APIView):
    def get(self, request):
        user = CustomUser.objects.filter(email=self.request.user.email).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
