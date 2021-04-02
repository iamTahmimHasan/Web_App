from django.shortcuts import render
from django.http import HttpResponse
from .models import Admission

# Create your views here.
def home(request):
    if request.method == "POST":
        sur_name = request.POST['sur_name']
        given_name = request.POST['given_name']
        gender = request.POST['gender']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        email = request.POST['email']
        passport_no = request.POST['passport_no']
        mobile_number = request.POST['mobile_number']
        date_of_birth = request.POST['date_of_birth']
        nid_no = request.POST['nid_no']
        religion = request.POST['religion']
        marital_status = request.POST['marital_status']
        spouse_name = request.POST['spouse_name']
        spouse_mobile_no = request.POST['spouse_mobile_no']
        interested_country = request.POST['interested_country']
        interested_institute = request.POST['interested_institute']
        interested_program = request.POST['interested_program']
        present_address = request.POST['present_address']
        permanent_address = request.POST['permanent_address']
        father_occupation = request.POST['father_occupation']
        father_designation = request.POST['father_designation']
        father_mobile_no = request.POST['father_mobile_no']
        organization_name = request.POST['organization_name']
        organization_address = request.POST['organization_address']
        reference_name = request.POST['reference_name']
        reference_mobile_no = request.POST['reference_mobile_no']
        referecnce_address = request.POST['referecnce_address']
        ssc_degree = request.POST['ssc_degree']
        ssc_institute = request.POST['ssc_institute']
        ssc_group = request.POST['ssc_group']
        ssc_result = request.POST['ssc_result']
        ssc_year = request.POST['ssc_year']
        hsc_degree = request.POST['hsc_degree']
        hsc_institute = request.POST['hsc_institute']
        hsc_group = request.POST['hsc_group']
        hsc_result = request.POST['hsc_result']
        hsc_year = request.POST['hsc_year']
        bacholor_degree = request.POST['bacholor_degree']
        bacholor_institute = request.POST['bacholor_institute']
        bacholor_group = request.POST['bacholor_group']
        bacholor_result = request.POST['bacholor_result']
        bacholor_year = request.POST['bacholor_year']
        masters_degree = request.POST['masters_degree']
        masters_institute = request.POST['masters_institute']
        masters_group = request.POST['masters_group']
        masters_result = request.POST['masters_result']
        masters_year = request.POST['masters_year']
        language_skills = request.POST['language_skills']
        language_skills_score = request.POST['language_skills_score']
        language_skills_score_test_date = request.POST['language_skills_score_test_date']
        information_media = request.POST['information_media']
        phone_contact_by = request.POST['phone_contact_by']
        counselor_Name = request.POST['counselor_Name']
        visa_processed_by = request.POST['visa_processed_by']
        digital_sign = request.POST['digital_sign']
        photo_and_signeture = request.POST['photo_and_signeture']
        nid_and_passport = request.POST['nid_and_passport']
        master_certificate_and_transcript = request.POST['master_certificate_and_transcript']
        bachelor_certificate_and_transcript = request.POST['bachelor_certificate_and_transcript']
        hsc_certificate_and_transcript = request.POST['hsc_certificate_and_transcript']
        ssc_certificate_and_transcript  = request.POST['ssc_certificate_and_transcript ']

        ins = Admission(
            sur_name = sur_name, given_name = given_name, gender=gender, 
            father_name=father_name, mother_name=mother_name, email=email, 
            passport_no=passport_no, mobile_number=mobile_number, 
            date_of_birth=date_of_birth, nid_no=nid_no, religion=religion, 
            marital_status=marital_status, spouse_mobile_no=spouse_mobile_no, 
            interested_country= interested_country, interested_institute= interested_institute, 
            interested_program=interested_program, present_address=present_address, 
            permanent_address=permanent_address, father_occupation=father_occupation, 
            father_designation=father_designation, father_mobile_no=father_mobile_no,
            organization_name=organization_name, organization_address = organization_address,
            reference_name = reference_name, reference_mobile_no= reference_mobile_no, 
            referecnce_address= referecnce_address, ssc_degree=ssc_degree, 
            ssc_institute=ssc_institute, ssc_group =ssc_group, ssc_result = ssc_result, 
            ssc_year =ssc_year, hsc_degree = hsc_degree, hsc_institute=hsc_institute,
            hsc_group=hsc_group, hsc_year= hsc_year, hsc_result =hsc_result, bacholor_degree =bacholor_degree,
            bacholor_institute=bacholor_institute, bacholor_year =bacholor_year, bacholor_result=bacholor_result,
            masters_degree=masters_degree, masters_institute=masters_institute, masters_group=masters_group, 
            masters_result =masters_result, masters_year= masters_year, language_skills =language_skills,
            language_skills_score=language_skills_score, language_skills_score_test_date= language_skills_score_test_date,
            information_media=information_media, phone_contact_by = phone_contact_by, 
            counselor_Name=counselor_Name, visa_processed_by=visa_processed_by,
            digital_sign=digital_sign, photo_and_signeture = photo_and_signeture,
            nid_and_passport=nid_and_passport, master_certificate_and_transcript=master_certificate_and_transcript,
            hsc_certificate_and_transcript=hsc_certificate_and_transcript,
            ssc_certificate_and_transcript =ssc_certificate_and_transcript
            
            )
        ins = save()
        print ('From Submit Successfull')



    return render(request,'admission.html')