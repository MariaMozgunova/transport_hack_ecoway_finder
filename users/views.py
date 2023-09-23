from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics, mixins

from .models import User
from .serializers import UserSerializer, LoginSerializer


class UserApiView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateApiView(
    generics.CreateAPIView,
):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data)
