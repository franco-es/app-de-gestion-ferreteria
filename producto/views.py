from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import productos

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class ProductosListado(ListView):
  model = productos

class ProductosDetalle(DetailView):
  model = productos

class ProductoCrear(CreateView):
  model = productos
  form = productos
  fields = ['codigo', 'nombre', 'precio', 'remarcado',  'stock', 'distribuidor']
  success_message = 'Producto creado correctamente!'

  def get_success_url(self):
    return reverse('productos')

class ProductosActualizar(SuccessMessageMixin, UpdateView):
  model = productos
  form = productos
  fields = "__all__"
  success_message = 'Producto actualizado correctamente'

  def get_success_message(self):
    return reverse('productos')

class ProductosEliminar(SuccessMessageMixin, DeleteView):
  model = productos
  form = productos
  fields = "__all__"

  def get_success_message(self):
    success_message = 'Producto eliminado correctamente'
    messages.success(self.request, (success_message))
    
  def get_success_url(self):
    return reverse('productos')