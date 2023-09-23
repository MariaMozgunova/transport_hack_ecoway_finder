from rest_framework import generics

from .models import Passenger, PassengerGroup
from .serializers import PassengerSerializer, PassengerGroupSerializer


class PassengerApiView(
    generics.RetrieveUpdateAPIView,
):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()


class PassengerChangeApiView(
    generics.ListCreateAPIView,
):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()


class PassengerGroupApiView(
    generics.RetrieveUpdateAPIView,
):
    serializer_class = PassengerGroupSerializer
    queryset = PassengerGroup.objects.all()


class PassengerGroupChangeApiView(
    generics.ListCreateAPIView,
):
    serializer_class = PassengerGroupSerializer
    queryset = PassengerGroup.objects.all()
