# Generated by Django 3.0.1 on 2020-01-08 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca_api', '0021_auto_20200107_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prateleira',
            old_name='espaço_sobrando',
            new_name='espaco_sobrando',
        ),
    ]