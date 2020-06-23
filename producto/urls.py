from django.urls import path
from .views import ProductosDetalle, ProductosListado, ProductoCrear, ProductosActualizar, ProductosEliminar

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ProductosListado.as_view(template_name = "producto/productos.html"), name ='productos'),
    path('detalle/<int:pk>', ProductosDetalle.as_view(template_name = "producto/detalle.html"), name = 'detailproducto'),
    path('crear/', ProductoCrear.as_view(template_name = "producto/crear.html"), name = 'addproducto'),
    path('actualizar/<int:pk>', ProductosActualizar.as_view(template_name = "producto/actualizar.html"), name = 'updateproducto'),
    path('eliminar/<int:pk>', ProductosEliminar.as_view(), name = 'deleteproducto')
]