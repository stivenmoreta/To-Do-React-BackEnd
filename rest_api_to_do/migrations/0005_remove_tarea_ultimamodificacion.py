# Generated by Django 3.2.9 on 2022-01-31 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_to_do', '0004_tarea_eliminartarea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='ultimaModificacion',
        ),
    ]
