from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=30)
    isbn = models.IntegerField()
    authors = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    ReleaseDate = models.DateField()

    def __str__(self):
        return self.name
