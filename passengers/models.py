from django.db import models
# from django.contrib.gis.db import models as gis_models


class PassengerGroup(models.Model):
    source_address = models.ForeignKey('trips.Address', on_delete=models.PROTECT, null=True, related_name="passenger_group_source_set")
    destination_address = models.ForeignKey('trips.Address', on_delete=models.PROTECT, null=True, related_name="passenger_group_destination_set")
    # source = gis_models.PointField(null=True)
    # destination = gis_models.PointField(null=True)
    departure_time = models.DateTimeField(null=True)
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.creator} {self.departure_time}"


class Passenger(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    group = models.ForeignKey(PassengerGroup, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
