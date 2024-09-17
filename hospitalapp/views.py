from ast import Pass
from venv import create
from django.shortcuts import render, redirect, get_object_or_404
from hospitalapp.models import *
from userapp.models import *
from bloodbankapp.models import *
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.db.models import Count

from django.http import HttpResponseRedirect
from Blood_india_project.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
import requests
import random
# Create your views here.




# main

def hospital_dashboard(request):
    hospital_id=request.session['hospital_id']
    # data=UserProfileModel.objects.filter(hospital_id=hospital_id)
    totalcount=UserProfileModel.objects.filter(status='Pending').count()

    Apos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    total=Apos100+Apos150+Apos200+Apos250+Apos300+Apos350+Apos400+Apos450
    
   
    
    
    
    Bpos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    
    total1=Bpos100+Bpos150+Bpos200+Bpos250+Bpos300+Bpos350+Bpos400+Bpos450
    
    Opos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
   
    total2=Opos100+Opos150+Opos200+Opos250+Opos300+Opos350+Opos400+Opos450
   
   
   
    Aneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    
    total3=Aneg100+Aneg150+Aneg200+Aneg250+Aneg300+Aneg350+Aneg400+Aneg450
    
    
    
    
    Bneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
   
    total4=Bneg100+Bneg150+Bneg200+Bneg250+Bneg300+Bneg350+Bneg400+Bneg450
   
    
    
    
    Oneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    
    total5=Oneg100+Oneg150+Oneg200+Oneg250+Oneg300+Oneg350+Oneg400+Oneg450
    
    
    
    ABneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    
    total6=ABneg100+ABneg150+ABneg200+ABneg250+ABneg300+ABneg350+ABneg400+ABneg450
    
    
    
    ABpos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    total7= ABpos100+ABpos150+ABpos200+ABpos250+ABpos300+ABpos350+ABpos400+ABpos450
    
    data2=HospitalSendRequestModel.objects.filter(hospital_status='Pending').count()
    data3=BloodbankSendRequestModel.objects.filter(status='Pending').count()
    data4=UserReciptantModel.objects.filter(status='Pending').count()
    
    
    
    
    return render(request,'hospital/hospital-dashboard.html',{'apos':total,'bpos':total1,'opos':total2,'aneg':total3,'bneg':total4,'oneg':total5,'abpos':total7,'abneg':total6,'donars':totalcount,'hospitals':data2,'bloodbank':data3,'users':data4})

def hospital_profile(request):
    
    return render(request,'hospital/hospital-profile.html')

def hospital_registration(request):
    
    if request.method =='POST' and request.FILES['upload_hospital_profile']:
        hospital_name=request.POST.get('hosp_name')
        hpospital_email=request.POST.get('hosp_email')
        hospital_password=request.POST.get('hosp_password')
        hospital_upload_image=request.FILES['upload_hospital_profile']
        hospital_mobilenumber=request.POST.get('hosp_mobileno')
        hospital_address=request.POST.get('hosp_address')
       
        if HospitalRegistrationModel.objects.filter(hpospital_email=hpospital_email).exists():
            messages.error(request,"Email Already Existed")
            return redirect("hospital_registration")
        else:
            user=HospitalRegistrationModel.objects.create(hospital_name=hospital_name,hpospital_email=hpospital_email,hospital_password=hospital_password,hospital_mobilenumber=hospital_mobilenumber,hospital_address=hospital_address,hospital_upload_image=hospital_upload_image)
            user.save()
            messages.success(request,"Your Account Is Successfully Registered")  
    
    return render(request,'hospital/hospital-registration.html')

# views_details

def hospital_view_blood_donated_user_details(request):
 
    hospital_id=request.session['hospital_id']
    
   

    # user_profile_id=UserProfileModel.objects.filter(user_profile_id=hospital_id).count()
    user=UserProfileModel.objects.filter(hospital_id=hospital_id).all().order_by('user_profile_blood_donated_date')
  
    

    
    
    return render(request,'hospital/hospital-view-blood-donated-users.html',{'user':user})

def hospital_view_blood_stock(request):
    
    hospital_id=request.session['hospital_id']
    # data=UserProfileModel.objects.filter(hospital_id=hospital_id)
    totalcount=UserProfileModel.objects.filter(hospital_id=hospital_id).count()

    Apos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Apos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='A+').filter(hospital_id=hospital_id).count()
    Bpos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Bpos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='B+').filter(hospital_id=hospital_id).count()
    Opos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Opos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='O+').filter(hospital_id=hospital_id).count()
    Aneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Aneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='A-').filter(hospital_id=hospital_id).count()
    Bneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Bneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='B-').filter(hospital_id=hospital_id).count()
    Oneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    Oneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='O-').filter(hospital_id=hospital_id).count()
    ABneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='AB-').filter(hospital_id=hospital_id).count()
    ABpos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    ABpos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='AB+').filter(hospital_id=hospital_id).count()
    
    return render(request,'hospital/hospital-blood-stock.html',{'count':totalcount,'Apos100':Apos100,'Apos150':Apos150,'Apos200':Apos200,'Apos250':Apos250,'Apos300':Apos300,'Apos350':Apos350,'Apos400':Apos400,'Apos450':Apos450,'Bpos100':Bpos100,'Bpos150':Bpos150,'Bpos200':Bpos200,'Bpos250':Bpos250,'Bpos300':Bpos300,'Bpos350':Bpos350,'Bpos400':Bpos400,'Bpos450':Bpos450,'Opos100':Opos100,'Opos150':Opos150,'Opos200':Opos200,'Opos250':Opos250,'Opos300':Opos300,'Opos350':Opos350,'Opos400':Opos400,'Opos450':Opos450,'Aneg100':Aneg100,'Aneg150':Aneg150,'Aneg200':Aneg200,'Aneg250':Aneg250,'Aneg300':Aneg300,'Aneg350':Aneg350,'Aneg400':Aneg400,'Aneg450':Aneg450,'Bneg100':Bneg100,'Bneg150':Bneg150,'Bneg200':Bneg200,'Bneg250':Bneg250,'Bneg300':Bneg300,'Bneg350':Bneg350,'Bneg400':Bneg400,'Bneg450':Bneg450,'Oneg100':Oneg100,'Oneg150':Oneg150,'Oneg200':Oneg200,'Oneg250':Oneg250,'Oneg300':Oneg300,'Oneg350':Oneg350,'Oneg400':Oneg400,'Oneg450':Oneg450,'ABpos100':ABpos100,'ABpos150':ABpos150,'ABpos200':ABpos200,'ABpos250':ABpos250,'ABpos300':ABpos300,'ABpos350':ABpos350,'ABpos400':ABpos400,'ABpos450':ABpos450,'ABneg100':ABneg100,'ABneg150':ABneg150,'ABneg200':ABneg200,'ABneg250':ABneg250,'ABneg300':ABneg300,'ABneg350':ABneg350,'ABneg400':ABneg400,'ABneg450':ABneg450 })

def hospital_view_donar_details_update_blood_details(request,id):
    # data = get_object_or_404(UserProfileModel)
    data= request.session['hospital_id']
    data2=get_object_or_404(UserProfileModel,user_profile_id=id)
    if request.method =='POST':
        
       user_profile_blood=request.POST.get('updateblood')
       user_profile_blood_donated_date=request.POST.get('donated_date')
       
       data2.user_profile_blood=user_profile_blood
       data2.user_profile_blood_donated_date=user_profile_blood_donated_date
       data2.hospital_id=data
       data2.save(update_fields=['user_profile_blood','user_profile_blood_donated_date','hospital_id'])
       
       
      
       
    return render(request,'hospital/hospital-view-donar-details-update-blood.html',{'data':data2})

def hospital_view_donatedblood_to_hospitals(request):
    data2= request.session['hospital_id']
    data=HospitalSendRequestModel.objects.all().filter(hospital_id=data2)
    
    return render(request,'hospital/view-donatedblood-hospitals.html',{'data':data})

def hospital_view_bloodbanks_details(request):
    data2= request.session['hospital_id']
    data=BloodbankSendRequestModel.objects.all().filter(hospital_id=data2)
    
    return render(request,'hospital/hospital-bloodbanks-view.html',{'data':data})


# send_request

def hospital_blood_send_request_hospitals(request):
    
    data2 = request.session['hospital_id']
    print(data2)
    data=HospitalRegistrationModel.objects.all().filter(hospital_id=data2)
    
    if request.method =='POST':
      
        hospital_name=request.POST.get('hosp_name')
        hospital_mobilenumber=request.POST.get('hosp_mobileno')
        hospital_email=request.POST.get('hosp_email')
        hospital_bloodgroup_requried=request.POST.get('hosp_blood_group_requried')
        hospital_blood_requried_ml=request.POST.get('hosp_blood_requried_ml')
        
        user=HospitalSendRequestModel.objects.create(hospital_name=hospital_name, hospital_mobilenumber=hospital_mobilenumber, hospital_bloodgroup_requried=hospital_bloodgroup_requried, hospital_blood_requried_ml=hospital_blood_requried_ml,hospital_email=hospital_email)
        user.save()
        
        if user:
            messages.success(request,"Your Request Form Is Successfully Uploaded")       
        else:
            pass
       
        
        
       
    
    return render(request,'hospital/hospital-blood-send-request-form.html',{'data':data})

# receive_requests

def hospital_blood_receive_request_hospitals(request):
    data2=request.session['hospital_id']
    print(data2)
    data=HospitalSendRequestModel.objects.all()
    
    # for x in data:
    #      print(type(x.hospital_id))
    #      print(type(data2))
    #     if int(x.hospital_id)== data2:
    #         print('ok')

    
    
    return render(request,'hospital/hospital-blood-request-recevice-hospitals.html',{'data':data,'data3':data2})

def hospital_blood_receive_request_bloodbanks(request):
    data2=request.session['hospital_id']
    data=BloodbankSendRequestModel.objects.all()
    
    return render(request,'hospital/blood-bank-request.html',{'data2':data2,'data':data})

def hospital_user_blood_recpitant_receive_request(request):
    data2=request.session['hospital_id']
    
    data=UserReciptantModel.objects.all()
    
    return render(request,'hospital/user-blood-requesting.html',{'data2':data2,'data':data})

def hospital_ngo_camp_condut_receive_request(request):
    data2=request.session['hospital_id']
    data=NgoCampConductModel.objects.all()
    return render(request,'hospital/ngo-camp-conduct-requesting.html',{'data2':data2,'data':data})

def hospital_user_blood_donating_receive_request(request):
    data2=request.session['hospital_id']
    data=UserProfileModel.objects.all()
    for i in data:
        
        i.hospital_id
        
    print(type(i.hospital_id))
    
    return render(request,'hospital/user-blood-donating-request.html',{'data2':data2,'data':data})


#accept actions
def hospital_accept(request,id):
    
    data2 = request.session['hospital_id']
    data = get_object_or_404(HospitalSendRequestModel,h_id=id)
    data3= get_object_or_404(HospitalRegistrationModel,hospital_id=data2)
    price_1 = data3.hospital_name
    print(price_1)
    data.hospital_status = data3.hospital_name  + ' Is Accepted'
    print(data.hospital_status)
    data.h_status = 'Accepted'
    data.hospital_id = data2
     
    data.save(update_fields=['h_status','hospital_status','hospital_id',])
    data.save()
     
    #email message
    html_content = "Hospital Name :" + data3.hospital_name +"<br/>" +"Hospital Mobile No :" + str(data3.hospital_mobilenumber) +"<br/>" + "Hospital Address :" + data3.hospital_address + "<br/> <p>   Your Application has been  Accepted .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.hospital_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
   
    return redirect('hospital_blood_receive_request_hospitals')
def hospital_rejected(request,id):
    
    data2 = request.session['hospital_id']
    data = get_object_or_404(HospitalSendRequestModel,h_id=id)
    data3= get_object_or_404(HospitalRegistrationModel,hospital_id=data2)
    price_1 = data3.hospital_name
    print(price_1)
    data.hospital_status =  'Rejected'
    print(data.hospital_status)
    data.hospital_id = '0'
    data.h_status =  'Rejected'
    data.save(update_fields=['h_status','hospital_status','hospital_id',])
    data.save()
    #email message
    html_content = "Hospital Name :" +data3.hospital_name +"<br/> <p>   Your Application has been rejected. Please wait until it is approved .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.hospital_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
   
    return redirect('hospital_blood_receive_request_hospitals')

def bloodbank_accept(request,id):
    
    data2 = request.session['hospital_id']
    data = get_object_or_404(BloodbankSendRequestModel,b_id=id)
    data3= get_object_or_404(HospitalRegistrationModel,hospital_id=data2)
    # data4= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.hospital_name 
    print(price_1)
    data.status = price_1 + ' Is Accepted'
    print(data.status)
    data.b_status='Accepted'
    data.hospital_id = data2
    data.save(update_fields=['b_status','status','hospital_id'])
    data.save()
    #email message
    html_content = "Hospital Name :" + data3.hospital_name +"<br/>" +"Hospital Mobile No :" + str(data3.hospital_mobilenumber) +"<br/>" + "Hospital Address :" + data3.hospital_address + "<br/> <p>   Your Application has been  Accepted .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.Bloodemail]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    
    return redirect('hospital_blood_receive_request_bloodbanks')

def bloodbank_rejected(request,id):
    
    data2 = request.session['hospital_id']
    data = get_object_or_404(BloodbankSendRequestModel,b_id=id)
    data3= get_object_or_404(HospitalRegistrationModel,hospital_id=data2)
    # data4= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.hospital_name 
    print(price_1)
    data.status =  'Rejected'
    data.b_status='Rejected'
    print(data.status)
    data.hospital_id = '0'
    data.save(update_fields=['b_status','status','hospital_id'])
    data.save()
      #email message
    html_content = "Hospital Name :" +data3.hospital_name +"<br/> <p>   Your Application has been rejected. Please wait until it is approved .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.Bloodemail]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    
    return redirect('hospital_blood_receive_request_bloodbanks')




def user_donate_accept(request,id):
    
    data2 = request.session['hospital_id']
    data = get_object_or_404(UserProfileModel,user_profile_id=id)
    data3= get_object_or_404(HospitalRegistrationModel,hospital_id=data2)
    # data4= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.hospital_name 
    print(price_1)
    data.status = price_1 + ' Is Accepted'
    print(data.status)
    data.P_status='Accepted'
    data.hospital_id = data2
    data.save(update_fields=['P_status','status','hospital_id'])
    data.save()
    
       #email message
    html_content = "Hospital Name :" + data3.hospital_name +"<br/>" +"Hospital Mobile No :" + str(data3.hospital_mobilenumber) +"<br/>" + "Hospital Address :" + data3.hospital_address + "<br/> <p>   Your Application has been  Accepted .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.user_profile_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    
    return redirect('hospital_user_blood_donating_receive_request')

def user_donate_rejected(request,id):
    
    data2 = request.session['hospital_id']
    data = get_object_or_404(UserProfileModel,user_profile_id=id)
    data3= get_object_or_404(HospitalRegistrationModel,hospital_id=data2)
    # data4= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.hospital_name 
    print(price_1)
    data.status =  'Rejected'
    data.P_status='Rejected'
    print(data.status)
    data.hospital_id = '0'
    data.save(update_fields=['P_status','status','hospital_id'])
    data.save()
      #email message
    html_content = "Hospital Name :" +data3.hospital_name +"<br/> <p>   Your Application has been rejected. Please wait until it is approved .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.user_profile_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    
    return redirect('hospital_user_blood_donating_receive_request')

def reciptant_accept(request,id):
    
    data2 = request.session['hospital_id']
    data = get_object_or_404(UserReciptantModel,user_reciptant_id=id)
    data3= get_object_or_404(HospitalRegistrationModel,hospital_id=data2)
    price_1 = data3.hospital_name
    print(price_1)
    data.status = data3.hospital_name  + ' Is Accepted'
    data.u_status='Accepted'
    print(data.status)
    data.hospital_id = data2
     
    data.save(update_fields=['u_status','status','hospital_id',])
    data.save()
       #email message
    html_content = "Hospital Name :" + data3.hospital_name +"<br/>" +"Hospital Mobile No :" + str(data3.hospital_mobilenumber) +"<br/>" + "Hospital Address :" + data3.hospital_address + "<br/> <p>   Your Application has been  Accepted .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.user_reciptant_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
   
    return redirect('hospital_user_blood_recpitant_receive_request')

def reciptant_rejected(request,id):
    
    data2 = request.session['hospital_id']
    data = get_object_or_404(UserReciptantModel,user_reciptant_id=id)
    data3= get_object_or_404(HospitalRegistrationModel,hospital_id=data2)
    price_1 = data3.hospital_name
    print(price_1)
    data.status =  'Rejected'
    data.u_status='Rejected'
    print(data.status)
    data.hospital_id = '0'
     
    data.save(update_fields=['u_status','status','hospital_id',])
    data.save()
       #email message
    html_content = "Hospital Name :" +data3.hospital_name +"<br/> <p>   Your Application has been rejected. Please wait until it is approved .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.user_reciptant_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
       
   
    return redirect('hospital_user_blood_recpitant_receive_request')

      



def hospital_ngo_accept(request,id):
    
    data2 = request.session['hospital_id']
    data = get_object_or_404(NgoCampConductModel,ngo_camp_id=id)
    data3= get_object_or_404(HospitalRegistrationModel,hospital_id=data2)
    price_1 = data3.hospital_name
    print(price_1)
    data.status = data3.hospital_name  + ' Is Accepted'
    data.n_status='Accepted'
    print(data.status)
    data.hospital_id = data2
     
    data.save(update_fields=['n_status','status','hospital_id',])
    data.save()
         #email message
    html_content = "Hospital Name :" + data3.hospital_name +"<br/>" +"Hospital Mobile No :" + str(data3.hospital_mobilenumber) +"<br/>" + "Hospital Address :" + data3.hospital_address + "<br/> <p>   Your Application has been  Accepted .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.ngo_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
   
    return redirect('hospital_ngo_camp_condut_receive_request')

def hospital_ngo_rejected(request,id):
    
    data2 = request.session['hospital_id']
    data = get_object_or_404(NgoCampConductModel,ngo_camp_id=id)
    data3= get_object_or_404(HospitalRegistrationModel,hospital_id=data2)
    price_1 = data3.hospital_name
    print(price_1)
    data.status =  'Rejected'
    data.n_status =  'Rejected'
    print(data.status)
    data.hospital_id = '0'
     
    data.save(update_fields=['n_status','status','hospital_id',])
    data.save()
   
      #email message
    html_content = "Hospital Name :" +data3.hospital_name +"<br/> <p>   Your Application has been rejected. Please wait until it is approved .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.ngo_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
   
   
   
    return redirect('hospital_ngo_camp_condut_receive_request')



#hospital_login

# def hospital_login(request):
#     if request.method=='POST':
        
#       email = request.POST.get('hosp_email')
#       password = request.POST.get('hosp_password') 
#       print(email)
#       try:
#             check = HospitalRegistrationModel.objects.get(hpospital_email=email,hospital_password=password)
          
#             request.session['hospital_id'] = check.hospital_id
#             print(request.session['hospital_id'] )
#             messages.success(request,"Your Are Successfully Logged")   
#             return redirect ('hospital_dashboard')
        
#       except:
#             messages.error(request,"Your Email or Password Given Worng")
#             return redirect ('hospital_login')
    
#     return render(request,'hospital/hospital-login.html')


def hospital_login(request):
     if request.method == 'POST': 
                email = request.POST.get('hosp_email') 
                password = request.POST.get('hosp_password') 
                try: 
                     check = HospitalRegistrationModel.objects.get(hpospital_email=email,hospital_password=password)   
                     request.session['hospital_id']=check.hospital_id  
                       
                     hospital_status = check.hospital_status 
                     if hospital_status =='Accepted': 
                         messages.success(request,'login success') 
                         return redirect('hospital_dashboard')  
                     elif hospital_status =='Rejected' :  
                         messages.error(request,'Your request is Rejected so you cannot login')   
                     elif hospital_status == 'Pending': 
                         messages.info(request,'Your request is Pending so cannot login')   
 
                      
                except: 
                     messages.warning(request,'invalid login') 
                                   
     return render(request,'hospital/hospital-login.html')


