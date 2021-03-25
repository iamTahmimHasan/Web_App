from django.db import models

# Create your models here.

class EmploymentClientList(models.Model):
        client_name =models.CharField(max_length=255, verbose_name="Client Name")
        client_logo = models.ImageField(upload_to='client_logo', verbose_name="Client Business Logo")
        client_profile_show_home_page = models.BooleanField(default=False , verbose_name="Show on Home Page")
        
        def __str__(self):
            return self.client_name
        
        class Meta:
                verbose_name = 'Employment Client'
                verbose_name_plural = 'Employment Clients'


class HomePageSlider(models.Model):

        slider_title = models.CharField(max_length=255, verbose_name="Slider Title")
        slider_image = models.ImageField(upload_to='slider_image', verbose_name="Slider Image")


        def __str__(self):
                        return self.id
                

        class Meta:
                verbose_name = 'Home Page Slider'
                verbose_name_plural = 'Home Page Sliders'