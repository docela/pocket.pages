from django.db import models
from datetime import datetime

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=150)
    genres = models.CharField(max_length=100)
    year_published = models.IntegerField(blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    date_added = models.DateTimeField(default=datetime.now, auto_now_add=True)
    last_edited = models.DateTimeField(default=datetime.now, auto_now=True)
    cover = models.ImageField(upload_to='covers/%Y/%m/%d/')

    def __str__(self):
        return f'{self.title} by {self.authors}.'
