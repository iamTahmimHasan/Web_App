from django.urls import path
from . import views

urlpatterns = [
    path('', views.employment, name ='employment'),
    path('about', views.about, name ='about'),
    
]