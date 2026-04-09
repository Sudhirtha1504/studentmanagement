from django.contrib import admin
from django.urls import path, include

# ✅ ADD THIS IMPORT
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# ✅ MEDIA FILES (Images for events, etc.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)