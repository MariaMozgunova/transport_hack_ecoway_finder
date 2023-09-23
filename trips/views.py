from rest_framework import generics

from .models import Trip, Address
from .serializers import TripSerializer, AddressSerializer


class TripApiView(
    generics.RetrieveUpdateAPIView,
):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()


class TripChangeApiView(
    generics.ListCreateAPIView,
):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()


class AddressApiView(
    generics.RetrieveUpdateAPIView,
):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class AddressChangeApiView(
    generics.ListCreateAPIView,
):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
