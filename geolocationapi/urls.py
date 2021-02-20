from django.contrib import admin
from django.urls import path, include
import locationapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('locationapi.urls')),
]
