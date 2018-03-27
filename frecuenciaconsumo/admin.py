from django.contrib import admin
from models import Unidad, Racion

# Register your models here.
class UnidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    ordering = ['nombre',]
    
class RacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'unidad', 'peso',)
    list_filter = ('nombre', 'cantidad', 'unidad', 'peso',)
    search_fields = ('nombre',)
    raw_id_fields = ('unidad',)
    ordering = ['nombre', 'peso',]
    
admin.site.register(Unidad, UnidadAdmin)
admin.site.register(Racion, RacionAdmin)

