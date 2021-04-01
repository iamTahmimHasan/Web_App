from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('base', views.base, name ='base'),
    path('about_us', views.about_us, name ='about_us'),
    path('faq', views.faq, name ='faq'),
]