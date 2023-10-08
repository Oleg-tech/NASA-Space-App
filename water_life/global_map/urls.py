from .views import home, fill_database, filter_data, get_number_of_animals_by_state_view
from django.urls import path, include


urlpatterns = [
    path('', home, name='home'),
    path('fill-database', fill_database, name='fill_database'),

    #   Endpoints for dynamical update
    path('filter-data', filter_data, name='filter_data'),
    path('get-number-of-animals-by-state', get_number_of_animals_by_state_view, name='get_number_of_animals_by_state'),
]
