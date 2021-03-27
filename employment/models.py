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


        
                
        class Meta:
                verbose_name = 'Home Page Slider'
                verbose_name_plural = 'Home Page Sliders'


class HomePageLeftSide(models.Model):
        external_video_Url = models.CharField(max_length=255, verbose_name="Upload Video Url Via (Youtube/Others)", blank=True, null=True)
        rightsidebaner1 = models.ImageField(upload_to='Banner', verbose_name="Right Side Baner 1", blank=True, null=True)
        rightsidebaner2 = models.ImageField(upload_to='Banner', verbose_name="Right Side Baner 2", blank=True, null=True)
        quotes = models.CharField(max_length=150, verbose_name="quotes", blank=True, null=True)
        quotes_writter = models.CharField(max_length=50, verbose_name="quotes_writter", blank=True, null=True)
        
        
        class Meta:
                verbose_name = 'Home Page Left Side Media'
                verbose_name_plural = 'Home Page Side Medias'


class BlockQuote(models.Model):
        quote = models.TextField(max_length=150, verbose_name="Quote", blank=True, null=True)
        quote_writter = models.CharField(max_length=50, verbose_name="Quote Writter", blank=True, null=True)
        show_multipul_pages = models.BooleanField(default=False , verbose_name="Show Multipul Pages")
        home_page = models.BooleanField(default=False , verbose_name="Home Page")
        about_page = models.BooleanField(default=False , verbose_name="About Page")
        team_page = models.BooleanField(default=False , verbose_name="Team Page")

        class Meta:
                verbose_name = 'Block Quote'
                verbose_name_plural = 'Block Quotes'


class ManageTeams(models.Model):
        name = models.CharField(max_length=250, verbose_name="Name")
        designation = models.CharField(max_length=150, verbose_name="Designation", blank=True, null=True)
        department = models.CharField(max_length=150, verbose_name="Department", blank=True, null=True)
        short_description = models.TextField(max_length=150, verbose_name="Short Description", blank=True, null=True)


        class Meta:
                verbose_name = 'Team Member'
                verbose_name_plural = 'Team Members'

        def __str__(self):
                        return self.name

