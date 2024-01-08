from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('core/', include('core.urls')),
    path('chat/', include('chat.urls')),
    path('customuser/', include('customuser.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
