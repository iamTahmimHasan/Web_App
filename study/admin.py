from django.contrib import admin
from .models import University

# Register your models here.
class UniversityAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Top University", {
            "fields" :( 
                'university_logo', 'university_name', 'university_rank', 'university_country' 

            ),
        }),
    )

    list_display =("university_name", "university_rank", "university_country", "university_logo")

        

admin.site.register(University, UniversityAdmin)