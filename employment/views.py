from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def employment(request):
    return render(request, 'employment.html')
