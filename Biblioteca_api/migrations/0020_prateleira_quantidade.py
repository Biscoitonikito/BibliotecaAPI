# Generated by Django 3.0.1 on 2020-01-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca_api', '0019_auto_20200107_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='prateleira',
            name='quantidade',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]