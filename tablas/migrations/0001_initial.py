# Generated by Django 5.1.1 on 2024-11-03 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=10)),
                ('razon_social', models.CharField(max_length=20)),
                ('representante_legal', models.CharField(max_length=20)),
                ('direcion', models.CharField(max_length=10)),
                ('telefono', models.IntegerField()),
                ('vehiculo_asociado', models.CharField(max_length=20)),
            ],
        ),
    ]