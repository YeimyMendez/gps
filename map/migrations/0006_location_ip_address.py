# Generated by Django 4.2.5 on 2023-09-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_remove_search_latitude_remove_search_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='ip_address',
            field=models.CharField(default='127.0.0.1', max_length=15),
        ),
    ]