# Generated by Django 4.0.2 on 2022-02-10 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='provincia',
        ),
    ]
