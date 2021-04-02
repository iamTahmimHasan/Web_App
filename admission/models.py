from django.db import models

# Create your models here.

class Admission(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sur_name = models.CharField(max_length=50, verbose_name= "Sur Name")
    given_name = models.CharField(max_length=50, verbose_name= "Given Name")
    gender = models.CharField(max_length=50, blank=True, null=True, verbose_name= "Gender")
    father_name = models.CharField(max_length=50, verbose_name= "Father Name")
    mother_name = models.CharField(max_length=50, blank=True, null=True, verbose_name= "Mother Name")
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name= "Email")
    passport_no = models.IntegerField(null= True, blank=True, verbose_name= "Passport Number")
    mobile_number = models.CharField(max_length=50, blank=True, null=True, verbose_name= "Mobile Number")
    date_of_birth = models.CharField(max_length=50, blank=True, null=True, verbose_name= "Date Of Birth")
    nid_no = models.IntegerField(null=True, blank= True, verbose_name= "Nid No")
    religion = models.CharField(max_length=50, blank=True, null=True, verbose_name= "Religion")
    marital_status = models.CharField(max_length=50, blank=True, null=True, verbose_name= "Marital Status")
    spouse_name = models.CharField(max_length=50, blank=True, null=True, verbose_name= "Spouse Name")
    spouse_mobile_no = models.CharField(max_length=50, blank=True, null=True, verbose_name= "Spouse Mobile Name")
    interested_country = models.CharField(max_length=50, blank=True, null=True, verbose_name= "Interested Country Name")
    interested_institute = models.CharField(max_length=50, blank = True, null= True, verbose_name= "Interested Instituted Name")
    interested_program = models.CharField(max_length=50, verbose_name= "Intersted Program ")
    present_address = models.CharField(max_length=50, blank = True, null= True, verbose_name= "Present Address")
    permanent_address = models.CharField(max_length=50, blank = True, null= True, verbose_name= "Parmanent Address")
    father_occupation = models.CharField(max_length=50, blank = True, null= True, verbose_name= "Father Ocopation")
    father_designation = models.CharField(max_length=50, blank = True, null= True, verbose_name= "Father Desigantion")
    father_mobile_no = models.CharField(max_length=50, blank = True, null= True, verbose_name= "Father Mobile Number")
    organization_name = models.CharField(max_length=50, blank = True, null= True, verbose_name= "Organiazation Name")
    organization_address= models.CharField(max_length=50, blank = True, null= True, verbose_name= " Organization Address")
    reference_name = models.CharField(max_length=50, blank = True, null= True, verbose_name= "Reference Name")
    reference_mobile_no = models.CharField(max_length=50, blank = True, null= True, verbose_name= "Reference Address")
    referecnce_address = models.CharField(max_length=50,blank = True, null= True, verbose_name= "SSC Digree")
    ssc_degree = models.CharField(max_length=50, blank = True, null= True, verbose_name= "SSC Digree")
    ssc_institute = models.CharField(max_length=50,blank = True, null= True, verbose_name="SSC Instute")
    ssc_group = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "ssc_group")
    ssc_result = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "ssc_result")
    ssc_year = models.CharField(max_length=50, blank = True, null= True, verbose_name= "ssc_year")
    hsc_degree = models.CharField(max_length=50, blank = True, null= True, verbose_name= "hsc_degree")
    hsc_institute = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "hsc_institute")
    hsc_group = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "hsc_group")
    hsc_result = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "hsc_result")
    hsc_year = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "hsc_year")
    bacholor_degree = models.CharField(max_length=50, blank = True, null= True, verbose_name= "bacholor_degree")
    bacholor_institute = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "bacholor_institute")
    bacholor_group = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "bacholor_group")
    bacholor_result = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "bacholor_result")
    bacholor_year = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "bacholor_year")
    masters_degree = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "masters_degree")
    masters_institute = models.CharField(max_length=50, blank = True, null= True,  verbose_name="masters_institute")
    masters_group = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "masters_group")
    masters_result = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "masters_result")
    masters_year = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "masters_year")
    language_skills = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "language_skills")
    language_skills_score = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "language_skills_score")
    language_skills_score_test_date = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "language_skills_score_test_date")
    information_media = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "information_media")
    phone_contact_by = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "phone_contact_by")
    counselor_Name = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "counselor_Name")
    visa_processed_by = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "visa_processed_by")
    digital_sign = models.CharField(max_length=250, blank = True, null= True,  verbose_name= "digital_sign")
    photo_and_signeture = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "photo_and_signeture")
    nid_and_passport = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "nid_and_passport ")
    master_certificate_and_transcript = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "master_certificate_and_transcript")
    bachelor_certificate_and_transcript = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "bachelor_certificate_and_transcript")
    hsc_certificate_and_transcript = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "hsc_certificate_and_transcript")
    ssc_certificate_and_transcript  = models.CharField(max_length=50, blank = True, null= True,  verbose_name= "ssc_certificate_and_transcript")
    

