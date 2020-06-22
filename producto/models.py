from django.db import models

# Create your models here.


class distribuidores(models.Model):
  nombre = models.CharField(max_length = 50)
  telefono = models.CharField(max_length = 100)
  email = models.CharField(max_length = 50)
  direccion = models.CharField(max_length = 100, default = 0)

  def __str__(self):
    return self.nombre


class productos(models.Model):
  codigo = models.IntegerField(unique = True)
  nombre = models.CharField(max_length=250)
  precio = models.CharField(max_length=150)
  precio_c_iva = models.CharField(max_length=250 ,default = 2)
  stock = models.IntegerField()
  distribuidor = models.ManyToManyField(distribuidores, help_text = 'seleccione su proveedor')
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)


  class Meta:
    db_table = 'Productos'

  def __str__(self):
    return self.nombre
