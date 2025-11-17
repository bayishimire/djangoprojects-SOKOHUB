from django.db import models
from accounts.models import CustomUser

class Product(models.Model):
    STATUS_CHOICES = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('out_of_stock', 'Out of Stock'),
)
    
    vendor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')
    status = models.CharField(max_length=19, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
