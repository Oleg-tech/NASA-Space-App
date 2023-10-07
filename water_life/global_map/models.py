from django.db import models


class Animal(models.Model):
    animal_name = models.CharField(max_length=100, verbose_name="Name")                 # comname
    group_name = models.CharField(max_length=100, verbose_name="Group name")            # group_name
    animal_latin_name = models.CharField(max_length=100, verbose_name="Latin name")     # sciname
    region_name = models.CharField(max_length=100, verbose_name="Region name")          # region_desc
    status = models.CharField(max_length=100, verbose_name="Status")                    # status
    state_name = models.CharField(max_length=100, verbose_name="State name")            # ...
