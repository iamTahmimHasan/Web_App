from django.urls import path
from . import views

urlpatterns = [
    path('', views.employment, name ='employment'),
    path('about', views.about, name ='about'),
    path('team', views.team, name ='team'),
    path('form', views.form, name ='form'),
    path('profile', views.profile, name ='profile'),
    path('gallery', views.gallery, name ='gallery'),
    path('client', views.client, name ='client'),
    path('visa', views.visa, name ='visa'),
    path('visa_success', views.visa_success, name ='visa_success'),
    path('contact', views.contact, name ='contact'),
]