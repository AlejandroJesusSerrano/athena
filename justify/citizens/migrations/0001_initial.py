# Generated by Django 4.2.6 on 2023-10-10 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=50, verbose_name='Provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=75, verbose_name='Nombres')),
                ('last_names', models.CharField(max_length=75, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=80, unique=True, verbose_name='Email')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('cuil', models.CharField(max_length=11, unique=True, verbose_name='CUIL')),
                ('location', models.CharField(max_length=50, verbose_name='Localidad')),
                ('address', models.CharField(max_length=300, verbose_name='Domicilio')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Registro')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citizens.province', verbose_name='Provincia')),
            ],
        ),
    ]
