from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class CompanyDetails(models.Model):
        company_logo = models.ImageField(upload_to='company_logo', verbose_name="Company Logo")
        company_description = models.TextField(max_length=155, verbose_name="Company Description For Meta Details (Max Length 155)")
        company_keywords = models.TextField(max_length=160, verbose_name="Company keywords For Meta Details (Max Length 160)", default="abc, xyz, alpha,")
        
        

        class Meta:
            verbose_name = 'Company Detail'
            verbose_name_plural = 'Company Details'


class EmploymentCountry(models.Model):
        country_image = models.ImageField(upload_to='Employment_Country')
        country_name = models.CharField(max_length=50)
        country_short_description = models.CharField(max_length=50)

        class Meta:
            verbose_name = 'Employment Country'
            verbose_name_plural = 'Employment Countrys'

class TravelCountry(models.Model):
        country_image = models.ImageField(upload_to='Travel_Country')
        country_name = models.CharField(max_length=50)
        country_short_description = models.CharField(max_length=50)

        class Meta:
            verbose_name = 'Travel Country'
            verbose_name_plural = 'Travel Countrys'

class StudyCountry(models.Model):
        country_image = models.ImageField(upload_to='Study_Country')
        country_name = models.CharField(max_length=50)
        country_short_description = models.CharField(max_length=50)

        class Meta:
            verbose_name = 'Study Country'
            verbose_name_plural = 'Study Countrys'