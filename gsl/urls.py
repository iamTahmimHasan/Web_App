"""gsl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', include('frontend.urls')),
    path('admission/', include('admission.urls')),
    path('user/', include('userregistration.urls')),
    path('study/', include('study.urls')),
    path('employment/', include('employment.urls')),
    path('form/', include('form.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title = "GSL Adminstrator"
admin.site.index_header = "Global Star Admin"
admin.site.site_title = "Global Star Admin"
admin.site.site_header = "Global Star Admin"