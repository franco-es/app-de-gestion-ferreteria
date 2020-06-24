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
  precio = models.DecimalField(decimal_places=4, max_digits=10)
  iva = models.DecimalField(decimal_places=4, max_digits=7, default=1.21)
  remarcado = models.DecimalField(decimal_places=4, max_digits=7, help_text = "colocar 1, antes del valor remarcado")
  precio_c_iva = models.CharField(max_length=250, blank=True)
  precio_venta = models.CharField(max_length=250, blank=True)
  stock = models.IntegerField()
  distribuidor = models.ManyToManyField(distribuidores)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)


  class Meta:
    db_table = 'Productos'

  def __str__(self):
    return self.nombre

  def save(self, *args, **kwargs):
    self.precio_c_iva = (float(self.precio)*float(self.iva))
    self.precio_venta = (float(self.precio_c_iva)*float(self.remarcado))
    super(productos, self).save(*args, **kwargs)
