from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    qr = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    # service = m


# class Ticket(models.Model):
#     name = models.CharField(max_length=1000)
#     price = models.IntegerField()
#     description = models.CharField(max_length=2048, null=True, blank=True)
#     ad = models.CharField(max_length=1024, null=True, blank=True)
#     ad_pic = models.ImageField(null=True, blank=True)


class UserService(models.Model):
    # class Meta:
    #     unique_together = ()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.service) + ' --> ' + str(self.user)


class Price(models.Model):
    title = models.CharField(max_length=127)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Ad(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=10000)
    pic = models.ImageField()

    def __str__(self):
        return self.title


class Seat(models.Model):
    class Meta:
        unique_together = ('block', 'gender', 'row', 'number')
        ordering = ['block', 'row', 'number']

    block = models.CharField(max_length=128)
    gender = models.CharField(max_length=2, choices=[('f', 'female'), ('m', 'male')])
    row = models.IntegerField()
    number = models.IntegerField()
    title = models.CharField(max_length=128)
    price = models.ForeignKey(Price, on_delete=models.PROTECT)
    description = models.CharField(max_length=2048, null=True, blank=True)
    ad = models.ForeignKey(Ad, on_delete=models.PROTECT, null=True, blank=True)
    owner = models.OneToOneField(Profile, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return str(self.title) + ': ' + str(self.number) + ' in ' + str(self.row) + ' in ' + str(self.block)
