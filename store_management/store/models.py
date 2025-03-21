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

    def __str__(self):
        return self.name