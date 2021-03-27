from django.shortcuts import render
from django.http import HttpResponse
from .models import HomePageSlider, EmploymentClientList, HomePageLeftSide
from frontend.models import CompanyDetails
# Create your views here.

def employment(request):

    entrys = EmploymentClientList.objects.all().filter(client_profile_show_home_page= 1)
    home_slides = HomePageSlider.objects.all()
    gsl_logos = CompanyDetails.objects.all()
    leftside_medias= HomePageLeftSide.objects.all()


    return render(request, 'employment.html', {
        'home_slides' : home_slides,
        'gsl_logos' : gsl_logos,
        'entrys' : entrys,
        'leftside_medias' : leftside_medias
        })



def about(request):
    gsl_logos = CompanyDetails.objects.all()
    return render(request, 'about.html',{
            'gsl_logos' : gsl_logos,

    })
    