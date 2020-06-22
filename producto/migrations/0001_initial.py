# Generated by Django 3.0.6 on 2020-06-22 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=250)),
                ('precio', models.CharField(max_length=150)),
                ('stock', models.IntegerField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Productos',
            },
        ),
    ]