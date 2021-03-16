from django.shortcuts import render
from django.http import HttpResponse
from .models import University

# Create your views here.
def home(request):
    hot_universitys = University.objects.all()
    return render(request,'study.html', {'hot_universitys': hot_universitys})