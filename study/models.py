from django.db import models

# Create your models here.

#class Destination(models.Model):
    #name = models.CharField(max_length=100)
    #img = models.ImageField(upload_to='pics')
    #desc = models.TextField()
    #price = models.IntegerField()
    #offer = models.BooleanField(default=False)
 
class University (models.Model):
        university_logo = models.ImageField(upload_to='pics')
        university_name = models.CharField(max_length=255)
        university_rank = models.CharField(max_length=50)
        university_country = models.CharField(max_length=100)
    