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
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
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
        unique_together = ['number', 'row']
        ordering = ['row', 'number', ]

    # block = models.CharField(max_length=128)
    # gender = models.CharField(max_length=2, choices=[('f', 'female'), ('m', 'male')])
    # row = models.IntegerField()
    number = models.IntegerField()
    title = models.CharField(max_length=128)
    price = models.ForeignKey(Price, on_delete=models.PROTECT, related_name='seat')
    description = models.CharField(max_length=2048, null=True, blank=True)
    ad = models.ForeignKey(Ad, on_delete=models.PROTECT, null=True, blank=True, related_name='seat')
    row = models.ForeignKey('Row', on_delete=models.PROTECT)

    # owner = models.OneToOneField(Profile, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return str(self.title) + ' : ' + str(self.number) + ' -> ' + str(self.row)


class Row(models.Model):
    class Meta:
        ordering = ['block', 'number', ]
        unique_together = ['number', 'block']

    number = models.IntegerField()
    # seat = models.ForeignKey(Seat, on_delete=models.PROTECT)
    block = models.ForeignKey('Block', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.number) + ' -> ' + str(self.block)


class Block(models.Model):
    class Meta:
        # ordering = ['row__number']
        unique_together = ['name', 'gender', 'hall']

    name = models.CharField(max_length=127)
    gender = models.CharField(max_length=2, choices=[('f', 'female'), ('m', 'male')])
    # row = models.ForeignKey(Row, on_delete=models.PROTECT)
    hall = models.ForeignKey('Hall', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name) + ' : ' + str(self.gender) + ' : ' + str(self.hall)


class Hall(models.Model):
    name = models.CharField(max_length=128)

    # block = models.ForeignKey(Block, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class HallEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    hall = models.ForeignKey(Hall, on_delete=models.PROTECT)
