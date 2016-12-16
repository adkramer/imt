from django.contrib import admin

# Register your models here.
from .models import Unitgroup, Unit

	
class UnitAdmin(admin.ModelAdmin):
	model = Unit
	
	
class UnitGroupAdmin(admin.ModelAdmin):
    model = Unitgroup
    filter_vertical =('unit',)


class CustomUnitAdmin(UnitGroupAdmin):
    save_on_top = True
    inlines = [UnitGroupAdmin]

admin.site.register(Unit) 
admin.site.register(Unitgroup, UnitGroupAdmin)
#admin.site.register(Unit, UnitAdmin)
