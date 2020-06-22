from django.contrib import admin

from .models import productos, distribuidores
# Register your models here.

class productosAdmin(admin.ModelAdmin):
  list_display = ( 'codigo',
                    'nombre',
                    'precio',
                    'stock')

class distribuidoresAdmin(admin.ModelAdmin):
  list_display = (
    'nombre',
    'telefono',
    'email',
    'direccion'
  )

admin.site.register(productos, productosAdmin)
admin.site.register(distribuidores, distribuidoresAdmin)