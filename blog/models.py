from django.db import models
from carmanager.models import CarManager
from datetime import datetime


class BlogList(models.Model):
    photo_list = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    name_list = models.CharField(max_length=300)
    blog_date = models.DateTimeField(default=datetime.now, blank=True)
    carmanager = models.ForeignKey(CarManager, on_delete=models.DO_NOTHING)
    text_list = models.TextField(blank=True)
    visible_list = models.BooleanField(blank=True)
    rating = models.IntegerField(default=True)

    def __str__(self):
        return self.name_list