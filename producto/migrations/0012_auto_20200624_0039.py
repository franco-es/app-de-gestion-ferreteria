# Generated by Django 3.0.6 on 2020-06-24 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0011_auto_20200623_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='iva',
            field=models.FloatField(default=1.21),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio_c_iva',
            field=models.FloatField(blank=True),
        ),
    ]
