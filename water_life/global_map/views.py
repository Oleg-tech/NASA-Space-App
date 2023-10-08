from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .models import Animal
from .scrapper import get_animal_for_state
from .utils import get_all_unique_group_names, get_danger_level, state_codes


def get_number_of_animals_by_state():
    list_of_animals = dict()

    for state_name in state_codes.keys():
        state_animals = Animal.objects.filter(state_name=state_name)
        list_of_animals[state_name] = len(state_animals)

    return list_of_animals


def home(request):
    animals = Animal.objects.all()[:30]

    context = {
        'animals': animals,
        'total_number_of_animals': Animal.objects.count(),
        'groups': get_all_unique_group_names(),
        'danger_level': get_danger_level(),
        'state_animals': get_number_of_animals_by_state(),
    }

    return render(request=request, template_name='global_map/main.html', context=context)


def fill_database(request):
    get_animal_for_state()
    return redirect('home')


#   Endpoints for dynamical update

# Filter list of animals
def filter_data(request):
    state = request.GET.get('state')
    if state:
        print(state)
        filtered_animals = Animal.objects.all().filter(state_name=state)
    else:
        filtered_classes = request.GET.getlist('group_name[]')
        filtered_danger_levels = request.GET.getlist('danger_level[]')

        filtered_animals = Animal.objects.all()
        if len(filtered_classes) > 0:
            filtered_animals = filtered_animals.filter(group_name__in=filtered_classes)
        if len(filtered_danger_levels) > 0:
            filtered_animals = filtered_animals.filter(status__in=filtered_danger_levels)

    limiter = True if len(filtered_animals[:30]) == 30 else False

    filtered_part = render_to_string('global_map/ajax_templates/animals_block.html', {
        'animals': filtered_animals,
        'lent': len(filtered_animals),
        'csrf_token': (request.GET.get('csrfmiddlewaretoken')),
        'limiter': limiter
    })

    return JsonResponse({
        'animals': filtered_part,
        'amount': len(filtered_animals),
        'limiter': limiter,
    })


def get_number_of_animals_by_state_view(request):
    list_of_animals = get_number_of_animals_by_state()
    return JsonResponse(list_of_animals)
