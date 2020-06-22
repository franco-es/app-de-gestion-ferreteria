from django.db import models

# Create your models here.
class productos(models.Model):
  codigo = models.IntegerField(max_length=50, unique = True)
  nombre = models.CharField(max_length=250)
  precio = models.CharField(max_length=150)
  stock = models.IntegerField(max_length=250)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)


  class Meta:
    db_table = 'Productos'