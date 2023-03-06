import datetime

from django.db import models
from django.utils import timezone

class Testart(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    mutetext = models.CharField('Подзаголовок', max_length=50)
    img = models.CharField('Картинка', max_length=250)
    full_text = models.TextField('Статья')

    def __str__(self):
        return self.title
    
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)