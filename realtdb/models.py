#-*- coding:utf-8 -*-

from django.db import models


class Realtor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class House(models.Model):
    realtor = models.ForeignKey(Realtor)
    address = models.CharField(max_length=100)
    area = models.FloatField(help_text=u"In square meters")
    price = models.DecimalField(max_digits=11, decimal_places=2)
