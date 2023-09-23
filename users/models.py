from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_ROLE_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    driver_licence = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=1, choices=USER_ROLE_CHOICES, blank=True)

    def __str__(self):
        return self.username
