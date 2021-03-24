from django.urls import path
from . import views

urlpatterns = [
    path('', views.employment, name ='employment'),
    
]