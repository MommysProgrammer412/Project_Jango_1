from django.db import models

class Order(models.Model):
    client_name = models.CharField(max_length=100)
    services = models.CharField(max_length=200)
    master_id = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=50)