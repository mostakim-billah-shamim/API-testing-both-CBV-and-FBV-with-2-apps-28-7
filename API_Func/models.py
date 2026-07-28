from django.db import models


class BookModel(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    price = models.FloatField( null=True)
    published = models.DateField( auto_now_add=True)

    def __str__(self):
        return self.title



class StoreModel(models.Model):
    name = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=200, null=True)
    established = models.PositiveIntegerField( null=True)

    def __str__(self):
        return self.name



# Create your models here.
