from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('global_map.urls')),
    path('admin/', admin.site.urls),
]
