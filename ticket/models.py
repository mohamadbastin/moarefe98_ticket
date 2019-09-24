from django.db import models


# Create your models here.

class Profile(models.Model):
    pass


class Ticket(models.Model):
    name = models.CharField(max_length=1000)
    price = models.IntegerField()
    description = models.CharField(max_length=2048)
    ad = models.CharField(max_length=1024)
    ad_pic = models.ImageField()


