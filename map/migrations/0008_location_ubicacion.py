# Generated by Django 4.2.5 on 2023-09-19 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_alter_location_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='ubicacion',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
