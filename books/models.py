from django.db import models


class Book(models.Model):
    title = models.CharField(max_length= 255)
    author= models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    publication_date = models.DateField()
    availability = models.CharField(max_length=255)
    edition = models.IntegerField()
    summary= models.CharField(max_length=255) 
    
