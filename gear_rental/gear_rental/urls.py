from django.contrib import admin
from django.urls import path
from catalog.views import home, package_list, package_detail, gear_item_detail
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import rental_terms
from catalog.views import digital_accessories_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('packages/', package_list, name='package_list'),
    path('packages/<int:package_id>/', package_detail, name='package_detail'),
    path('gear/<int:item_id>/', gear_item_detail, name='gear_item_detail'),
    path('rental-terms/', rental_terms, name='rental_terms'),
    path('digital-accessories/', digital_accessories_view, name='digital_accessories'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])