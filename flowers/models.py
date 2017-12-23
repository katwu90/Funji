# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    picture = models.CharField(max_length=1000)

    def __str__(self):
    	return self.name + ' - ' + self.description
 