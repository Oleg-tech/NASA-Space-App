from django.shortcuts import render


def home(request):
    return render(request, 'global_map/main.html', {})
