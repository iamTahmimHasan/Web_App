from django.shortcuts import render
from django.http import HttpResponse
from .models import TravelCountry, EmploymentCountry, StudyCountry

# Create your views here.
def home(request):
    travels= TravelCountry.objects.all()
    employments= EmploymentCountry.objects.all()
    studys= StudyCountry.objects.all()
    return render(request, 'home.html',
    {
        'travels':travels,
        'employments' : employments,
         'studys' :studys,
    })