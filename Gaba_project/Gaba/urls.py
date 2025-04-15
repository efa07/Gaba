
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from core.views import about 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('items/', include('items.urls')),
    path('about/', about, name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
