from django.contrib import admin
from .models import CompanyDetails

# Register your models here.

class FrontEndAdmin(admin.ModelAdmin):
    list_display = ("id", "company_keywords", "company_description", "company_logo")

admin.site.register(CompanyDetails, FrontEndAdmin)
