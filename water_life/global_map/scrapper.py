import requests

from .models import Animal
from .utils import state_codes


all_animals_list: list = []


def fill_database(state_name, response):
    for animal in response:
        new_product = Animal(
            animal_name=animal['comname'],
            group_name=animal['group_name'],
            animal_latin_name=animal['sciname'],
            region_name=animal['region_desc'],
            status=animal['status'],
            state_name=state_name
        )

        all_animals_list.append(new_product)


# Species for every state
def get_animal_for_state():
    Animal.objects.all().delete()

    for state_name, state_code in state_codes.items():
        url = f'https://ecos.fws.gov/ecp/report/speciesListingsByState?&statusCategory=Listed&stateAbbrev={state_code}&format=json'
        response = requests.get(url=url).json()['data']

        fill_database(state_name, response)

    Animal.objects.bulk_create(all_animals_list)

    all_animals_list.clear()

