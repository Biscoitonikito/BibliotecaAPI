# Generated by Django 3.0.1 on 2020-01-01 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca_api', '0017_remove_livro_quantidade'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Multa',
        ),
    ]