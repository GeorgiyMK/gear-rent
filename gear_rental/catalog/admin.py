from django.contrib import admin
from .models import GearItem, RentalPackage

@admin.register(GearItem)
class GearItemAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(RentalPackage)
class RentalPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_weekday', 'price_weekend', 'requires_prebooking', 'min_days_required')
    filter_horizontal = ('gear_items',)  # Добавляет удобный выбор предметов
