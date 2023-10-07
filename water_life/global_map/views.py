from django.shortcuts import render, redirect

from .models import Animal
from .scrapper import get_animal_for_state


def home(request):
    animals = Animal.objects.all()[:30]

    return render(request, 'global_map/main.html', context={'animals': animals})


def fill_database(request):
    get_animal_for_state()
    return redirect('home')

