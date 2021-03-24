from django.db import models

# Create your models here.

class HomePageSlider(models.Model):
    
    slider_title = models.CharField(max_length=255, verbose_name="Slider Title")
    slider_image = models.ImageField(upload_to='slider_image', verbose_name="Slider Image")


    def __str__(self):
            return self.id
   

    class Meta:
            verbose_name = 'Home Page Slider'
            verbose_name_plural = 'Home Page Sliders'