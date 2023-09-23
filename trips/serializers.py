from rest_framework import serializers

from .models import Trip, Address


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            'id',
            'source_address',
            'destination_address',
            "departure_time",
            "car",
            "driver",
            "passengers",
        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            "street",
            "city",
            "country",
        ]
