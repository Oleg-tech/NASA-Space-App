import requests
from bs4 import BeautifulSoup

from .models import Animal
from .utils import state_codes


all_animals_list: list = []


def get_picture(animal_name):
    search_query = f"Google Image {animal_name}"
    search_url = f"https://www.google.com.ua/search?q={search_query}&tbm=isch"

    response = requests.get(search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all("img")
        image_links = []
        for img in img_tags:
            if len(image_links) < 3:
                return image_links[1]
            image_links.append(img['src'])

    return None


def fill_database(state_name, response):
    for animal in response:
        new_product = Animal(
            animal_name=animal['comname'],
            group_name=animal['group_name'],
            animal_latin_name=animal['sciname'],
            region_name=animal['region_desc'],
            status=animal['status'],
            state_name=state_name,
            picture=get_picture(animal['sciname']),
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
