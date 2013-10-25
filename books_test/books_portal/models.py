from django.db import models
from django.forms import ModelForm


class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    pages = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class BooksForm(ModelForm):
    class Meta:
        model = Books