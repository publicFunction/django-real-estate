from django.db import models

class searchLog(models.Model):
    searchType = models.CharField(max_length=100)
    address = models.TextField()
    no_of_bedrooms = models.IntegerField()
    price_from = models.CharField(max_length=100)
    price_to = models.CharField(max_length=100)
    

