# Generated by Django 3.0.1 on 2019-12-27 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca_api', '0008_auto_20191226_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multa',
            name='aberta',
        ),
    ]
