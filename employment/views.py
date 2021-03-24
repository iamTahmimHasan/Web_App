from django.shortcuts import render
from django.http import HttpResponse
from .models import HomePageSlider
# Create your views here.

def employment(request):
    home_slides = HomePageSlider.objects.all()
    return render(request, 'employment.html',{'home_slides' : home_slides})
