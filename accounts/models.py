from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('vendor', 'Vendor'),
        ('customer', 'Customer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.username


