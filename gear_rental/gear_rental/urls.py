from django.contrib import admin
from django.urls import path
from catalog.views import home, package_list, package_detail, gear_item_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('packages/', package_list, name='package_list'),
    path('packages/<int:package_id>/', package_detail, name='package_detail'),
    path('gear/<int:item_id>/', gear_item_detail, name='gear_item_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
