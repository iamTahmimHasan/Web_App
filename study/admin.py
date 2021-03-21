from django.contrib import admin
from .models import University

# Register your models here.
class UniversityAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Top University", {
            "fields" :( 
                'university_logo', 'university_name', 'university_rank', 'university_country' , 'international_students', 
                'established_year', 'total_students', 'university_website', 'university_address'

            ),
        }),
    )

    list_display =("university_name", "university_rank", "university_country", "university_logo")

        

admin.site.register(University, UniversityAdmin)