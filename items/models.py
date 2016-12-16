from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel

class Unit(models.Model):
    name  = models.CharField("Unit Name", max_length=25, help_text="Enter Unit Name")
    abbrev  = models.CharField("Unit Abbreviation", max_length=10, help_text="Enter Unit Abbreviation")
    
    def __str__(self):
        return str(self.name)

class Unitgroup(models.Model):
    unitgroup = models.CharField(max_length=25)
    description = models.TextField
    unit = models.ManyToManyField(Unit)
    
    class Meta:
        verbose_name_plural = "Unit Groups"
    
    def get_units(self):
        return ", ".join([str(u) for u in self.unit.all().order_by('name')])
        
    def __str__(self):
        return str("{} : {}".format(self.unitgroup, self.get_units()))
        
