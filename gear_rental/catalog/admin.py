from django.contrib import admin
from .models import GearItem, GearItemImage, RentalPackage, Category, ContactInfo, DigitalAccessory


class GearItemImageInline(admin.TabularInline):
    model = GearItemImage
    extra = 1

@admin.register(GearItem)
class GearItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'available', 'deposit')
    inlines = [GearItemImageInline]

@admin.register(DigitalAccessory)
class DigitalAccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_day', 'deposit', 'available')

admin.site.register(GearItemImage)
admin.site.register(RentalPackage)
admin.site.register(Category)
admin.site.register(ContactInfo)
