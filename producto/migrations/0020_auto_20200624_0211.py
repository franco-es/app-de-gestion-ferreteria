# Generated by Django 3.0.6 on 2020-06-24 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0019_auto_20200624_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
