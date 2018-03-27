from django.contrib import admin
from models import Unidad, Racion

# Register your models here.
class UnidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    
class RacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'unidad', 'peso',)
    
admin.site.register(Unidad, UnidadAdmin)
admin.site.register(Racion, RacionAdmin)

