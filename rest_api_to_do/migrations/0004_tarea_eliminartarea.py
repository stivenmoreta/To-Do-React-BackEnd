# Generated by Django 3.2.9 on 2022-01-30 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_to_do', '0003_auto_20220130_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='eliminarTarea',
            field=models.BooleanField(default=False, verbose_name='Tarea Eliminada o no'),
        ),
    ]