from django.db import models
from datetime import datetime


class CarManager(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    phone_1 = models.CharField(max_length=20, blank=True)
    phone_2 = models.CharField(max_length=20, blank=True) 
    emaile = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200, blank=True)
    age_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    rating = models.IntegerField(default=True)

    def __str__(self):
        return self.name
