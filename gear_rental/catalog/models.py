from django.db import models
from django.shortcuts import render

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def home(request):
    return render(request, 'catalog/home.html')

class GearItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gear_images/')  # основное фото
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class GearItemImage(models.Model):
    gear_item = models.ForeignKey(GearItem, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gear_images/')

    def __str__(self):
        return f"Доп. фото для {self.gear_item.name}"

class RentalPackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    gear_items = models.ManyToManyField(GearItem, related_name='packages')
    price_weekday = models.DecimalField(max_digits=6, decimal_places=2)
    price_weekend = models.DecimalField(max_digits=6, decimal_places=2)
    min_days_required = models.PositiveIntegerField(default=1)
    requires_prebooking = models.BooleanField(default=False)

    def __str__(self):
        return self.name