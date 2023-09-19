# Generated by Django 4.2.5 on 2023-09-14 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitud', models.DecimalField(decimal_places=6, max_digits=9)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
