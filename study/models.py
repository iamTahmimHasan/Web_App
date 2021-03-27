from django.db import models
from django_countries.fields import CountryField


class University (models.Model):

        ESTABLISHED_YEAR_CHOICES = [(x, str(x)) for x in range(1088, 2021, 1)]
        university_logo = models.ImageField(upload_to='pics', verbose_name="University Logo")
        university_name = models.CharField(max_length=255, verbose_name="Name")
        university_rank = models.IntegerField(verbose_name="Rank", default="0")
        university_country = CountryField()
        international_students = models.IntegerField( blank=True, null=True, verbose_name="International Students")
        established_year = models.IntegerField( choices=ESTABLISHED_YEAR_CHOICES, blank=True, null=True, verbose_name="Established Year")
        total_students = models.IntegerField(blank=True, null=True, verbose_name="University Total Student")
        university_website= models.CharField(max_length=255, blank=True, null=True, default="https://www", verbose_name="University Website")
        university_address= models.CharField(max_length=255, blank=True, null=True, verbose_name="University Address")

        
        def __str__(self):
            return self.university_name
        
        class Meta:
            verbose_name = 'Top University'
            verbose_name_plural = 'Top Universitys'


            

    