from global_map.views import home, fill_database
from django.urls import path, include


urlpatterns = [
    path('', home, name='home'),
    path('fill-database', fill_database, name='fill_database')
]
