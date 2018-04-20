# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sensor(models.Model):
    position = models.IntegerField()
    name = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    noise = models.IntegerField()

    def __str__(self):
        return (self.name)