# Generated by Django 3.1.7 on 2021-11-22 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AntartidaFront', '0002_auto_20211122_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='nombre_sensor',
            new_name='nombre',
        ),
    ]
