from django.db import models


class Book(models.Model):
    title = models.CharField(max_length= 255)
    author= models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now=True)
    availability = models.CharField(max_length=255)
    edition = models.CharField(max_length=100)
    summary= models.CharField(max_length=255) 
    
