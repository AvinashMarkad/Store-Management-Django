from django.contrib import admin
from .models import Product

# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')  # Fields to display in the list view
    list_filter = ('category',)  # Add filters for the category field
    search_fields = ('name', 'description')  # Add search functionality for name and description