from django.db import models
# from django.contrib.gis.db import models as gis_models


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.street} {self.city} {self.country}"


class Trip(models.Model):
    source_address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True, related_name="trip_source_set")
    destination_address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True, related_name="trip_destination_set")
    # source = gis_models.PointField(null=True)
    # destination = gis_models.PointField(null=True)
    departure_time = models.DateTimeField(null=True)
    car = models.ForeignKey('cars.Car', on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey('users.User', on_delete=models.PROTECT, null=True)
    passengers = models.ForeignKey('passengers.PassengerGroup', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.driver} {self.car} {self.departure_time}"
