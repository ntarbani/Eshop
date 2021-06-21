
from django.contrib import admin
from django.urls import path,include
from .import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('signup', include('store.urls')),
    path('login', include('store.urls')),
    path('logout', include('store.urls')),
    path('cart', include('store.urls')),
    path('checkout', include('store.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
