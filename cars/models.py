from django.db import models


class Car(models.Model):
    color = models.CharField(max_length=100)
    plate_id = models.CharField(max_length=100)
    owner = models.ForeignKey('users.User', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.color} {self.plate_id}"
