from django.db import models

# Create your models here.

#class Destination(models.Model):
    #name = models.CharField(max_length=100)
    #img = models.ImageField(upload_to='pics')
    #desc = models.TextField()
    #price = models.IntegerField()
    #offer = models.BooleanField(default=False)
 
class University (models.Model):
        university_logo = models.ImageField(upload_to='pics', verbose_name="University Logo")
        university_name = models.CharField(max_length=255, verbose_name="Name")
        university_rank = models.CharField(max_length=50, verbose_name="Rank", default="0")
        university_country = models.CharField(max_length=100, verbose_name="Country")

        def __str__(self):
            return self.university_name
        
        class Meta:
            verbose_name = 'Top University'
            verbose_name_plural = 'Top Universitys'
    