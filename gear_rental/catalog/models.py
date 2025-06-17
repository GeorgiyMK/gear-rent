from django.db import models
from django.shortcuts import render
from decimal import Decimal

class ContactInfo(models.Model):
    name = models.CharField(max_length=100, help_text="Имя контактного лица")
    phone = models.CharField(max_length=20, help_text="Номер телефона")
    whatsapp_link = models.URLField("Ссылка на WhatsApp", blank=True, null=True)
    telegram_link = models.URLField("Ссылка на Telegram", blank=True, null=True)
    vk_group_link = models.URLField("Ссылка на группу ВКонтакте", blank=True, null=True)

    def __str__(self):
        return f"{self.name} — {self.phone}"

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class GearItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gear_images/')  # основное фото
    available = models.BooleanField(default=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class GearItemImage(models.Model):
    gear_item = models.ForeignKey(GearItem, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gear_images/')

    def __str__(self):
        return f"Доп. фото для {self.gear_item.name}"

class DigitalAccessory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='digital_accessories/')
    price_per_day = models.DecimalField(max_digits=7, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class RentalPackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    gear_items = models.ManyToManyField(GearItem, related_name='packages')
    price_weekday = models.DecimalField(max_digits=6, decimal_places=2)
    price_weekend = models.DecimalField(max_digits=6, decimal_places=2)
    min_days_required = models.PositiveIntegerField(default=1)
    requires_prebooking = models.BooleanField(default=False)
    # deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    @property
    def calculated_deposit(self):
        total_deposit = sum(item.deposit for item in self.gear_items.all())
        return round(Decimal(total_deposit) * Decimal('0.7'), 2)

    def __str__(self):
        return self.name