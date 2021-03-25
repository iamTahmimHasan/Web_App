from django.db import models

# Create your models here.

class CompanyDetails(models.Model):
        company_logo = models.ImageField(upload_to='company_logo', verbose_name="Company Logo")
        company_description = models.TextField(max_length=155, verbose_name="Company Description For Meta Details (Max Length 155)")
        company_keywords = models.TextField(max_length=160, verbose_name="Company keywords For Meta Details (Max Length 160)", default="abc, xyz, alpha,")
        
        

        class Meta:
            verbose_name = 'Company Detail'
            verbose_name_plural = 'Company Details'