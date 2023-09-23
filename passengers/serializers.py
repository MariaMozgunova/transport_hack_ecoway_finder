from rest_framework import serializers
from .models import Passenger, PassengerGroup


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = [
            'id',
            'first_name',
            'last_name',
            'group',
        ]


class PassengerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerGroup
        fields = [
            'id',
            'source_address',
            'destination_address',
            'departure_time',
            'creator',
            'passenger_set',
        ]
