from django.shortcuts import render
from django.http import HttpResponse
from .models import HomePageSlider, EmploymentClientList, HomePageLeftSide, BlockQuote, ManageTeams
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

def team(request):
    gsl_logos = CompanyDetails.objects.all()
    teams = ManageTeams.objects.all()
    quotes = BlockQuote.objects.all().filter(team_page= 1)
    return render(request, 'team.html', {
            'gsl_logos' : gsl_logos,
            'quotes' : quotes,
            'teams' : teams,

    })


def form(request):
    return render(request, 'form.html')



def profile(request):
    gsl_logos = CompanyDetails.objects.all()
    return render(request, 'profile.html',{
            'gsl_logos' : gsl_logos,

    })
  
def gallery(request):
    gsl_logos = CompanyDetails.objects.all()
    return render(request, 'gallery.html',{
            'gsl_logos' : gsl_logos,

    })

def client(request):
    gsl_logos = CompanyDetails.objects.all()
    return render(request, 'client.html',{
            'gsl_logos' : gsl_logos,

    })


def visa(request):
    gsl_logos = CompanyDetails.objects.all()
    return render(request, 'visa.html',{
            'gsl_logos' : gsl_logos,

    })

def visa_success(request):
    gsl_logos = CompanyDetails.objects.all()
    return render(request, 'visa_success.html',{
            'gsl_logos' : gsl_logos,

    })


def contact(request):
    gsl_logos = CompanyDetails.objects.all()
    return render(request, 'contact.html',{
            'gsl_logos' : gsl_logos,

    })