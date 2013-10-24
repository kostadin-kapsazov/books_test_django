import datetime
from django.utils import timezone
from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    pages = models.IntegerField(default=0)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title
