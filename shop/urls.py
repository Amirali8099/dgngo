from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    # اپ‌های بعدی که به‌مرور اضافه می‌شن:
    path('', include('account.urls')),
    path('', include('products.urls')),
    path('', include('article.urls')),
    path('', include('orders.urls')),
    path('', include('page.urls')),
    path('', include('about_us.urls')),
    path('',include('wishlist.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
