from .views import home, fill_database, load_more_animals, filter_data
from django.urls import path, include


urlpatterns = [
    path('', home, name='home'),
    path('fill-database', fill_database, name='fill_database'),

    #   Endpoints for dynamical update
    path('filter-data', filter_data, name='filter_data'),
    path('load-more-data', load_more_animals, name='load_more_data'),
]
