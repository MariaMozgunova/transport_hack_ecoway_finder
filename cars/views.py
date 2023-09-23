from rest_framework import generics

from .models import Car
from.serializers import CarSerializer


class CarApiView(
    generics.RetrieveUpdateAPIView,
):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarChangeApiView(
    generics.ListCreateAPIView,
):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
