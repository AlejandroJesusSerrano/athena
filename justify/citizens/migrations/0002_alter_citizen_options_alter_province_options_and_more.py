# Generated by Django 4.2.6 on 2023-10-10 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citizens', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citizen',
            options={'ordering': ['names'], 'verbose_name': 'Ciudadano', 'verbose_name_plural': 'Ciudadanos'},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'ordering': ['province'], 'verbose_name': 'Provincia', 'verbose_name_plural': 'Provincias'},
        ),
        migrations.AlterModelTable(
            name='citizen',
            table='ciudadano',
        ),
        migrations.AlterModelTable(
            name='province',
            table='provincia',
        ),
    ]
