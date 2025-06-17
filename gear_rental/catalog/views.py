from django.shortcuts import render, get_object_or_404
from .models import GearItem, RentalPackage, ContactInfo, DigitalAccessory


def home(request):
    contacts = ContactInfo.objects.all()
    return render(request, 'catalog/home.html', {'contacts': contacts})

def package_list(request):
    packages = RentalPackage.objects.all()
    return render(request, 'catalog/packages.html', {'packages': packages})

def package_detail(request, package_id):
    package = get_object_or_404(RentalPackage, pk=package_id)
    return render(request, 'catalog/package_detail.html', {'package': package})

def gear_item_detail(request, item_id):
    item = get_object_or_404(GearItem, pk=item_id)
    return render(request, 'catalog/item_detail.html', {'item': item})

def rental_terms(request):
    return render(request, 'catalog/rental_terms.html')

def digital_accessories_view(request):
    accessories = DigitalAccessory.objects.filter(available=True)
    return render(request, 'catalog/digital_accessories.html', {'accessories': accessories})
