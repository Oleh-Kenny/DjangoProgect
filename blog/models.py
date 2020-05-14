from django.db import models
from carmanager.models import CarManager
from datetime import datetime


class BlogList(models.Model):
    #фото на сторінку блог
    photo_list = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    #назва заголовка
    name_list = models.CharField(max_length=300)
    #дата публікації
    blog_date = models.DateTimeField(default=datetime.now, blank=True)
    #імя публікації карменеджера
    carmanager = models.ForeignKey(CarManager, on_delete=models.DO_NOTHING)
    #текст публікації(в блозі)
    short_textlist = models.TextField(blank=True)
    #текст публікації(в сінгл блозі)
    text_list = models.TextField(blank=True)
    #показ публікації
    visible_list = models.BooleanField(blank=True)
     #рейтинг публікації
    rating = models.IntegerField(default=True)

    def __str__(self):
        return self.name_list