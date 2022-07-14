from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('', include('app.urls')),
    path(settings.ADMIN_URL, admin.site.urls),
]