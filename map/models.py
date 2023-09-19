from django.db import models

# Create your models here.


class Search(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=15)  # Campo para la dirección IP


