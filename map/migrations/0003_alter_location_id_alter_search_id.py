# Generated by Django 4.2.5 on 2023-09-12 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='search',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]