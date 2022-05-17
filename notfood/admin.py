from django.contrib import admin

# Register your models here.
from . import models 

@admin.register(models.Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'tipo',)
    search_fields = ('nombre',)