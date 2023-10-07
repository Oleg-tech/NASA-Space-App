from django.contrib import admin

from .models import Animal


class AnimalAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'animal_name', 'group_name', 'animal_latin_name',
        'region_name', 'status', 'state_name',
    ]
    list_display_links = ['animal_name']


admin.site.register(Animal, AnimalAdmin)
