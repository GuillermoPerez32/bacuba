# Generated by Django 4.0.2 on 2022-02-10 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0003_user_municipio_user_provincia'),
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