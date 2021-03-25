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


class HomePageLeftSide(models.Model):
        External_video_Url = models.CharField(max_length=255, verbose_name="Upload Video Url Via (Youtube/Others)", blank=True, null=True)
        rightsidebaner1 = models.ImageField(upload_to='Banner', verbose_name="Right Side Baner 1", blank=True, null=True)
        rightsidebaner2 = models.ImageField(upload_to='Banner', verbose_name="Right Side Baner 2", blank=True, null=True)
        quotes = models.CharField(max_length=150, verbose_name="quotes", blank=True, null=True)
        quotes_writter = models.CharField(max_length=50, verbose_name="quotes_writter", blank=True, null=True)
        
        class Meta:
                verbose_name = 'Home Page Left Side Media'
                verbose_name_plural = 'Home Page Side Medias'