from ast import Pass
from dataclasses import dataclass
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

def bloodbank_dashboard(request):
    blood=request.session['Bloodbank_id']
    # data=UserProfileModel.objects.filter(hospital_id=hospital_id)
    totalcount=UserProfileModel.objects.filter(status='Pending').filter(P_status='Rejected').count()

    Apos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    total=Apos100+Apos150+Apos200+Apos250+Apos300+Apos350+Apos400+Apos450
    
   
    
    
    
    Bpos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    
    total1=Bpos100+Bpos150+Bpos200+Bpos250+Bpos300+Bpos350+Bpos400+Bpos450
    
    Opos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
   
    total2=Opos100+Opos150+Opos200+Opos250+Opos300+Opos350+Opos400+Opos450
   
   
   
    Aneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    
    total3=Aneg100+Aneg150+Aneg200+Aneg250+Aneg300+Aneg350+Aneg400+Aneg450
    
    
    
    
    Bneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
   
    total4=Bneg100+Bneg150+Bneg200+Bneg250+Bneg300+Bneg350+Bneg400+Bneg450
   
    
    
    
    Oneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    
    total5=Oneg100+Oneg150+Oneg200+Oneg250+Oneg300+Oneg350+Oneg400+Oneg450
    
    
    
    ABneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    
    total6=ABneg100+ABneg150+ABneg200+ABneg250+ABneg300+ABneg350+ABneg400+ABneg450
    
    
    
    ABpos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    total7= ABpos100+ABpos150+ABpos200+ABpos250+ABpos300+ABpos350+ABpos400+ABpos450
    
    data2=HospitalSendRequestModel.objects.filter(hospital_status='Pending').count()
    data3=BloodbankSendRequestModel.objects.filter(status='Pending').count()
    data4=UserReciptantModel.objects.filter(status='Pending').count()
    
    
    
    return render(request,'bloodbank/bloodbank-dashboard.html',{'apos':total,'bpos':total1,'opos':total2,'aneg':total3,'bneg':total4,'oneg':total5,'abpos':total7,'abneg':total6,'donars':totalcount,'hospitals':data2,'bloodbank':data3,'users':data4})

def bloodbank_registration(request):
    if request.method =='POST' and  request.FILES['blood_upload'] :
        Bloodname=request.POST.get('blood_name')
        Bloodemail=request.POST.get('blood_email')
        Bloodpassword=request.POST.get('blood_password')
        bloodbank_upload_image=request.FILES['blood_upload']
        Bloodmobilenumber=request.POST.get('blood_mobileno')
        Bloodaddress=request.POST.get('blood_address')
       
        if BloodbankRegistrationModel.objects.filter(Bloodemail=Bloodemail).exists():
            messages.error(request,"Email Already Existed")
            return redirect("bloodbank_registration")
        else:
            user=BloodbankRegistrationModel.objects.create(Bloodname=Bloodname,Bloodaddress=Bloodaddress,Bloodmobilenumber=Bloodmobilenumber,Bloodemail=Bloodemail,Bloodpassword=Bloodpassword,bloodbank_upload_image=bloodbank_upload_image)
            user.save()
            messages.success(request,"Your Account Is Successfully Registered")  
    
    return render(request,'bloodbank/bloodbank-registration.html')

def bloodbank_profile(request):
    
    return render(request,'bloodbank/bloodbank-profile.html')


# view_details
def bloodbank_accepted_view_details(request):
    data2= request.session['Bloodbank_id']
    data=BloodbankSendRequestModel.objects.all().filter(bloodbank_id=data2)
    
    return render(request,'bloodbank/bloodbank-accepted-view-details.html',{'data':data})

def bloodbank_view_bloodstock(request):
    
    blood=request.session['Bloodbank_id']
    # data=UserProfileModel.objects.filter(hospital_id=hospital_id)
    totalcount=UserProfileModel.objects.filter(bloodbank_id=blood).count()

    Apos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Apos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='A+').filter(bloodbank_id=blood).count()
    Bpos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Bpos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='B+').filter(bloodbank_id=blood).count()
    Opos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Opos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='O+').filter(bloodbank_id=blood).count()
    Aneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Aneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='A-').filter(bloodbank_id=blood).count()
    Bneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Bneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='B-').filter(bloodbank_id=blood).count()
    Oneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    Oneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='O-').filter(bloodbank_id=blood).count()
    ABneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='AB-').filter(bloodbank_id=blood).count()
    ABpos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
    ABpos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='AB+').filter(bloodbank_id=blood).count()
 
    
    return render(request,'bloodbank/bloodbank-blood-stock.html',{'count':totalcount,'Apos100':Apos100,'Apos150':Apos150,'Apos200':Apos200,'Apos250':Apos250,'Apos300':Apos300,'Apos350':Apos350,'Apos400':Apos400,'Apos450':Apos450,'Bpos100':Bpos100,'Bpos150':Bpos150,'Bpos200':Bpos200,'Bpos250':Bpos250,'Bpos300':Bpos300,'Bpos350':Bpos350,'Bpos400':Bpos400,'Bpos450':Bpos450,'Opos100':Opos100,'Opos150':Opos150,'Opos200':Opos200,'Opos250':Opos250,'Opos300':Opos300,'Opos350':Opos350,'Opos400':Opos400,'Opos450':Opos450,'Aneg100':Aneg100,'Aneg150':Aneg150,'Aneg200':Aneg200,'Aneg250':Aneg250,'Aneg300':Aneg300,'Aneg350':Aneg350,'Aneg400':Aneg400,'Aneg450':Aneg450,'Bneg100':Bneg100,'Bneg150':Bneg150,'Bneg200':Bneg200,'Bneg250':Bneg250,'Bneg300':Bneg300,'Bneg350':Bneg350,'Bneg400':Bneg400,'Bneg450':Bneg450,'Oneg100':Oneg100,'Oneg150':Oneg150,'Oneg200':Oneg200,'Oneg250':Oneg250,'Oneg300':Oneg300,'Oneg350':Oneg350,'Oneg400':Oneg400,'Oneg450':Oneg450,'ABpos100':ABpos100,'ABpos150':ABpos150,'ABpos200':ABpos200,'ABpos250':ABpos250,'ABpos300':ABpos300,'ABpos350':ABpos350,'ABpos400':ABpos400,'ABpos450':ABpos450,'ABneg100':ABneg100,'ABneg150':ABneg150,'ABneg200':ABneg200,'ABneg250':ABneg250,'ABneg300':ABneg300,'ABneg350':ABneg350,'ABneg400':ABneg400,'ABneg450':ABneg450 })

def bloodbank_view_blood_donated_hospitals(request):
    data2= request.session['Bloodbank_id']
    data=HospitalSendRequestModel.objects.all().filter(bloodbank_id=data2)
    
    
    return render(request,'bloodbank/bloodbank-blood-issued-to-hospitals-details.html',{'data':data})


def bloodbank_view_blood_donar_details(request):
    
    data2= request.session['Bloodbank_id']
    
   

    # user_profile_id=UserProfileModel.objects.filter(user_profile_id=hospital_id).count()
    user=UserProfileModel.objects.filter(bloodbank_id=data2).all().order_by('user_profile_blood_donated_date')
    
    return render(request,'bloodbank/bloodbank-donar-view-details.html',{'user':user})


def bloodbank_update_donation_blood_details(request,id):
    
    data= request.session['Bloodbank_id']
    data2=get_object_or_404(UserProfileModel,user_profile_id=id)
    if request.method =='POST':
        
       user_profile_blood=request.POST.get('updateblood')
       user_profile_blood_donated_date=request.POST.get('donated_date')
       
       data2.user_profile_blood=user_profile_blood
       data2.user_profile_blood_donated_date=user_profile_blood_donated_date
       data2.bloodbank_id=data
       data2.save(update_fields=['user_profile_blood','user_profile_blood_donated_date','bloodbank_id'])
    
    
    return render(request,'bloodbank/bloodbank-blood-donated-update-details.html',{'data':data2})



# send_request

def bloodbank_blood_send_request(request):
    data2= request.session['Bloodbank_id']
    data=BloodbankRegistrationModel.objects.all().filter(Bloodbank_id=data2)
    
    if request.method =='POST':
          
        bloodbank_name=request.POST.get('hosp_name')
        bloodbank_mobilenumber=request.POST.get('hosp_mobileno')
        
        bloodbank_bloodgroup_requried=request.POST.get('hosp_blood_group_requried')
        bloodbank_blood_requried_ml=request.POST.get('hosp_blood_requried_ml')
        Bloodemail=request.POST.get('blood_email')
        user=BloodbankSendRequestModel.objects.create(bloodbank_name=bloodbank_name, bloodbank_mobilenumber=bloodbank_mobilenumber, bloodbank_bloodgroup_requried=bloodbank_bloodgroup_requried, bloodbank_blood_requried_ml=bloodbank_blood_requried_ml,Bloodemail=Bloodemail)
        user.save()
        if user:
             messages.success(request,"Your Request Form Is Successfully Uploaded")       
        else:
            
            Pass
    
    return render(request,'bloodbank/bloodbank-blood-request-form.html',{'data':data})



# receive request


def bloodbank_user_blood_donating_receivce_requset(request):
    data2 = request.session['Bloodbank_id']
    data=UserProfileModel.objects.all()
    return render(request,'bloodbank/user-blood-donating-receivce-requset.html',{'data2':data2,'data':data})

def bloodbank_blood_request_receive_from_bloodbanks(request):
    data2 = request.session['Bloodbank_id']
    data=BloodbankSendRequestModel.objects.all()
    return render(request,'bloodbank/bloodbank-bloodrequest-from-bloodbanks.html',{'data2':data2,'data':data})

def bloodbank_user_bloodrequesting_receive_request(request):
    data2 = request.session['Bloodbank_id']
    data=UserReciptantModel.objects.all()
    return render(request,'bloodbank/user-blood-request-to-bloodbank.html',{'data2':data2,'data':data})

def bloodbank_blood_receive_request_hospitals(request):
    data2 = request.session['Bloodbank_id']
    data=HospitalSendRequestModel.objects.all()
    
    return render(request,'bloodbank/bloodbank-hospital-blood-request-to-bloodbank.html',{'data2':data2,'data':data})

def bloodbank_ngo_conduct_camp_recevie_request(request):
    data2 = request.session['Bloodbank_id']
    data=NgoCampConductModel.objects.all()
    return render(request,'bloodbank/bloodbank-ngo-conduct-camp-requset-form.html',{'data2':data2,'data':data})
 


#accept actions
def Bhospital_accept(request,id):
    
    data2 = request.session['Bloodbank_id']
    data = get_object_or_404(HospitalSendRequestModel,h_id=id)
    data3= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.Bloodname
    print(price_1)
    data.hospital_status = data3.Bloodname  + ' Is Accepted'
    print(data.hospital_status)
    data.h_status = 'Accepted'
    data.bloodbank_id = data2
     
    data.save(update_fields=['h_status','hospital_status','bloodbank_id',])
    data.save()
    #email message
    html_content = "Bloodbank Name :" + data3.Bloodname +"<br/>" +"Bloodbank Mobile No :" + str(data3.Bloodmobilenumber) +"<br/>" + "Bloodbank Address :" + data3.Bloodaddress + "<br/> <p>   Your Application has been  Accepted .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.hospital_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
   
    return redirect('bloodbank_blood_receive_request_hospitals')
def Bhospital_rejected(request,id):
    
    data2 = request.session['Bloodbank_id']
    data = get_object_or_404(HospitalSendRequestModel,h_id=id)
    data3= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.Bloodname
    print(price_1)
    data.hospital_status = 'Rejected'
    data.h_status =  'Rejected'
    print(data.hospital_status)
    data.bloodbank_id = '0'
     
    data.save(update_fields=['h_status','hospital_status','bloodbank_id',])
    data.save()
    #email message
    html_content = "BloodBank Name :" +data3.Bloodname +"<br/> <p>   Your Application has been rejected. Please wait until it is approved .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.hospital_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
   
    return redirect('bloodbank_blood_receive_request_hospitals')

def Bbloodbank_accept(request,id):
    
    data2 = request.session['Bloodbank_id']
    data = get_object_or_404(BloodbankSendRequestModel,b_id=id)
    data3= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    # data4= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.Bloodname 
    print(price_1)
    data.status = price_1 + ' Is Accepted'
    print(data.status)
    data.bloodbank_id = data2
    data.b_status='Accepted'
    data.save(update_fields=['b_status','status','bloodbank_id'])
    data.save()
     #email message
    html_content = "Bloodbank Name :" + data3.Bloodname +"<br/>" +"Bloodbank Mobile No :" + str(data3.Bloodmobilenumber) +"<br/>" + "Bloodbank Address :" + data3.Bloodaddress + "<br/> <p>   Your Application has been  Accepted .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.Bloodemail]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    
    return redirect('bloodbank_blood_request_receive_from_bloodbanks')

def Bbloodbank_Rejected(request,id):
    
    data2 = request.session['Bloodbank_id']
    data = get_object_or_404(BloodbankSendRequestModel,b_id=id)
    data3= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    # data4= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.Bloodname 
    print(price_1)
    data.status = 'Rejected'
    data.b_status='Rejected'
    print(data.status)
    data.bloodbank_id = '0'
    data.save(update_fields=['b_status','status','bloodbank_id'])
    data.save()
      #email message
    html_content = "BloodBank Name :" +data3.Bloodname +"<br/> <p>   Your Application has been rejected. Please wait until it is approved .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.Bloodemail]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    
    return redirect('bloodbank_blood_request_receive_from_bloodbanks')

def Breciptant_accept(request,id):
    
    data2 = request.session['Bloodbank_id']
    data = get_object_or_404(UserReciptantModel,user_reciptant_id=id)
    data3= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.Bloodname
    print(price_1)
    data.status = price_1  + ' Is Accepted'
    print(data.status)
    data.u_status='Accepted'
    data.bloodbank_id = data2
     
    data.save(update_fields=['u_status','status','bloodbank_id',])
    data.save()
         #email message
    html_content = "Bloodbank Name :" + data3.Bloodname +"<br/>" +"Bloodbank Mobile No :" + str(data3.Bloodmobilenumber) +"<br/>" + "Bloodbank Address :" + data3.Bloodaddress + "<br/> <p>   Your Application has been  Accepted .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.user_reciptant_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
   
    return redirect('bloodbank_user_bloodrequesting_receive_request')


def Breciptant_Rejected(request,id):
    
    data2 = request.session['Bloodbank_id']
    data = get_object_or_404(UserReciptantModel,user_reciptant_id=id)
    data3= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.Bloodname
    print(price_1)
    data.status = 'Rejected'
    data.u_status='Rejected'
    print(data.status)
    data.bloodbank_id = '0'
     
    data.save(update_fields=['u_status','status','bloodbank_id',])
    data.save()
      #email message
    html_content = "BloodBank Name :" +data3.Bloodname +"<br/> <p>   Your Application has been rejected. Please wait until it is approved .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.user_reciptant_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
   
    return redirect('bloodbank_user_bloodrequesting_receive_request')

def Buserdonate_accept(request,id):
    
    data2 = request.session['Bloodbank_id']
    data = get_object_or_404(UserProfileModel,user_profile_id=id)
    data3= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.Bloodname
    print(price_1)
    data.status = price_1  + ' Is Accepted'
    data.P_status='Accepted'
    print(data.status)
    data.bloodbank_id = data2
    data.P_status='Accepted'
    data.save(update_fields=['P_status','status','bloodbank_id',])
    data.save()
        #email message
    html_content = "Bloodbank Name :" + data3.Bloodname +"<br/>" +"Bloodbank Mobile No :" + str(data3.Bloodmobilenumber) +"<br/>" + "Bloodbank Address :" + data3.Bloodaddress + "<br/> <p>   Your Application has been  Accepted .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.user_profile_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
   
    return redirect('bloodbank_user_blood_donating_receivce_requset')

def Buserdonate_Rejected(request,id):
    
    data2 = request.session['Bloodbank_id']
    data = get_object_or_404(UserProfileModel,user_profile_id=id)
    data3= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.Bloodname
    print(price_1)
    data.status =  'Rejected'
    print(data.status)
    data.bloodbank_id = '0'
    data.P_status='Rejected'
    data.save(update_fields=['P_status','status','bloodbank_id',])
    data.save()
     #email message
    html_content = "BloodBank Name :" +data3.Bloodname +"<br/> <p>   Your Application has been rejected. Please wait until it is approved .</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.user_profile_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    return redirect('bloodbank_user_blood_donating_receivce_requset')


def Bloodbank_ngo_accept(request,id):
    
    data2 = request.session['Bloodbank_id']
    data = get_object_or_404(NgoCampConductModel,user_profile_id=id)
    data3= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.Bloodname
    print(price_1)
    data.status = price_1  + ' Is Accepted'
    print(data.status)
    data.bloodbank_id = data2
     
    data.save(update_fields=['','status','bloodbank_id',])
    data.save()
        #email message
    html_content = "Bloodbank Name :" + data3.Bloodname +"<br/>" +"Bloodbank Mobile No :" + str(data3.Bloodmobilenumber) +"<br/>" + "Bloodbank Address :" + data3.Bloodaddress + "<br/> <p>   Your Application has been  Accepted .</p>"

    
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.ngo_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
   
    return redirect('bloodbank_ngo_conduct_camp_recevie_request')

def Bloodbank_ngo_Rejected(request,id):
    
    data2 = request.session['Bloodbank_id']
    data = get_object_or_404(NgoCampConductModel,user_profile_id=id)
    data3= get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=data2)
    price_1 = data3.Bloodname
    print(price_1)
    data.status =  'Rejected'
    print(data.status)
    data.bloodbank_id = '0'
     
    data.save(update_fields=['','status','bloodbank_id',])
    data.save()
      #email message
    html_content = "BloodBank Name :" +data3.Bloodname +"<br/> <p>   Your Application has been rejected. Please wait until it is approved .</p>"

   
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.ngo_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
   
    return redirect('bloodbank_ngo_conduct_camp_recevie_request')

      



#bloodbank_login

# def bloodbank_login(request):
#     if request.method=='POST':
            
#       email = request.POST.get('blood_email')
#       password = request.POST.get('blood_password') 
#       print(email)
#       try:
#             check = BloodbankRegistrationModel.objects.get(Bloodemail=email,Bloodpassword=password)
          
#             request.session['Bloodbank_id'] = check.Bloodbank_id
#             messages.success(request,"Your Are Successfully Logged")   
#             return redirect ('bloodbank_dashboard')
        
#       except:
#             messages.error(request,"Your Email or Password Given Worng")
#             return redirect ('bloodbank_login')
    
#     return render(request,'bloodbank/bloodbank-login.html')


def bloodbank_login(request):
     if request.method == 'POST': 
                email = request.POST.get('blood_email') 
                password = request.POST.get('blood_password') 
                try: 
                     check = BloodbankRegistrationModel.objects.get(Bloodemail=email,Bloodpassword=password)   
                     request.session['Bloodbank_id']=check.Bloodbank_id  
                       
                     bloodbank_status = check.bloodbank_status 
                     if bloodbank_status =='Accepted': 
                         messages.success(request,'login success') 
                         return redirect('bloodbank_dashboard')  
                     elif bloodbank_status =='Rejected' :  
                         messages.error(request,'Your request is Rejected so you cannot login')   
                     elif bloodbank_status == 'Pending': 
                         messages.info(request,'Your request is Pending so cannot login')   
 
                      
                except: 
                     messages.warning(request,'invalid login') 
                                   
     return render(request,'bloodbank/bloodbank-login.html')


