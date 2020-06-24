# Generated by Django 3.0.6 on 2020-06-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_distribuidores_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=1.21, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio_c_iva',
            field=models.CharField(max_length=250),
        ),
    ]
