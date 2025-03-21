from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('fridge', 'Fridge'),
        ('freezer', 'Freezer'),
        ('ac', 'Air Conditioner'),
        ('cooler', 'Cooler'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # Add this line

    def __str__(self):
        return self.name