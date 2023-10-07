from django.db import models


class Animal(models.Model):
    animal_name = models.CharField(max_length=100, verbose_name="Name")
    group_name = models.CharField(max_length=100, verbose_name="Group name")
    animal_latin_name = models.CharField(max_length=100, verbose_name="Latin name")
    region_name = models.CharField(max_length=100, verbose_name="Region name")
    status = models.CharField(max_length=100, verbose_name="Status")
    state_name = models.CharField(max_length=100, verbose_name="State name")
    # picture = ...
