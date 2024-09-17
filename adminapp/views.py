from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from userapp.models import *
from hospitalapp.models import *
from bloodbankapp.models import *
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.http import HttpResponseRedirect
from Blood_india_project.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
import requests
import random

# Create your views here.

# main


def admin_dashboard(request):
    Apos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='A+').count()
    Apos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='A+').count()
    Apos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='A+').count()
    Apos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='A+').count()
    Apos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='A+').count()
    Apos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='A+').count()
    Apos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='A+').count()
    Apos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='A+').count()
    total=Apos100+Apos150+Apos200+Apos250+Apos300+Apos350+Apos400+Apos450
    
   
    
    
    
    Bpos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='B+').count()
    Bpos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='B+').count()
    Bpos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='B+').count()
    Bpos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='B+').count()
    Bpos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='B+').count()
    Bpos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='B+').count()
    Bpos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='B+').count()
    Bpos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='B+').count()
    
    total1=Bpos100+Bpos150+Bpos200+Bpos250+Bpos300+Bpos350+Bpos400+Bpos450
    
    Opos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='O+').count()
    Opos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='O+').count()
    Opos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='O+').count()
    Opos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='O+').count()
    Opos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='O+').count()
    Opos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='O+').count()
    Opos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='O+').count()
    Opos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='O+').count()
   
    total2=Opos100+Opos150+Opos200+Opos250+Opos300+Opos350+Opos400+Opos450
   
   
   
    Aneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='A-').count()
    Aneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='A-').count()
    Aneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='A-').count()
    Aneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='A-').count()
    Aneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='A-').count()
    Aneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='A-').count()
    Aneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='A-').count()
    Aneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='A-').count()
    
    total3=Aneg100+Aneg150+Aneg200+Aneg250+Aneg300+Aneg350+Aneg400+Aneg450
    
    
    
    
    Bneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='B-').count()
    Bneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='B-').count()
    Bneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='B-').count()
    Bneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='B-').count()
    Bneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='B-').count()
    Bneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='B-').count()
    Bneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='B-').count()
    Bneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='B-').count()
   
    total4=Bneg100+Bneg150+Bneg200+Bneg250+Bneg300+Bneg350+Bneg400+Bneg450
   
    
    
    
    Oneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='O-').count()
    Oneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='O-').count()
    Oneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='O-').count()
    Oneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='O-').count()
    Oneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='O-').count()
    Oneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='O-').count()
    Oneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='O-').count()
    Oneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='O-').count()
    
    total5=Oneg100+Oneg150+Oneg200+Oneg250+Oneg300+Oneg350+Oneg400+Oneg450
    
    
    
    ABneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='AB-').count()
    
    total6=ABneg100+ABneg150+ABneg200+ABneg250+ABneg300+ABneg350+ABneg400+ABneg450
    
    
    
    ABpos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='AB+').count()
    total7= ABpos100+ABpos150+ABpos200+ABpos250+ABpos300+ABpos350+ABpos400+ABpos450
    
    data2=HospitalRegistrationModel.objects.filter(hospital_status="Pending").count()
    data3=BloodbankRegistrationModel.objects.filter(bloodbank_status="Pending").count()
    data4=UserRegistrationModel.objects.filter(user_status="Pending").count()
    data5=NgoRegistrationModel.objects.filter(ngo_status="Pending").count()
    
    
    
    return render(request,'admin/admin-dashboard.html',{'ngo':data5,'apos':total,'bpos':total1,'opos':total2,'aneg':total3,'bneg':total4,'oneg':total5,'abpos':total7,'abneg':total6,'hospitals':data2,'bloodbank':data3,'users':data4})


# registrationform request


def admin_bloodbank_registration_form_request(request):
    bloodbankregistration=BloodbankRegistrationModel.objects.all().order_by('-Bloodreg_date')
    return render(request,'admin/admin-bloodbank-registrationform-request.html',{'data':bloodbankregistration})

def admin_hospital_registration_form_request(request):
    HospitalRegistration=HospitalRegistrationModel.objects.all().order_by('-hospital_reg_date')
    return render(request,'admin/admin-hospital-registrationform-request.html',{'data':HospitalRegistration})

def admin_user_registration_form_request(request):
    userregistration=UserRegistrationModel.objects.all().order_by('-user_reg_date')
    return render(request,'admin/user-registrationform-request.html',{'data':userregistration})

# views_details

def admin_view_hospitals_details(request):
    Hospitaldetails=HospitalRegistrationModel.objects.all().order_by('-hospital_reg_date').filter(hospital_status='Accepted')
    return render(request,'admin/admin-view-all-hospitals.html',{'data':Hospitaldetails})

def admin_view_bloodbanks_details(request):
    
    bloodbankdetails=BloodbankRegistrationModel.objects.all().order_by('-Bloodreg_date').filter(bloodbank_status='Accepted')

    return render(request,'admin/admin-view-bloodbanks.html',{'data':bloodbankdetails})

def admin_view_user_details(request):
    userregistration=UserRegistrationModel.objects.all().order_by('-user_reg_date').filter(user_status='Accepted')
    return render(request,'admin/admin-view-all-users2.html',{'data':userregistration})

def admin_view_bloodstock_details(request):
    Apos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='A+').count()
    Apos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='A+').count()
    Apos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='A+').count()
    Apos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='A+').count()
    Apos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='A+').count()
    Apos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='A+').count()
    Apos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='A+').count()
    Apos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='A+').count()
    Bpos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='B+').count()
    Bpos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='B+').count()
    Bpos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='B+').count()
    Bpos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='B+').count()
    Bpos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='B+').count()
    Bpos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='B+').count()
    Bpos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='B+').count()
    Bpos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='B+').count()
    Opos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='O+').count()
    Opos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='O+').count()
    Opos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='O+').count()
    Opos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='O+').count()
    Opos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='O+').count()
    Opos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='O+').count()
    Opos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='O+').count()
    Opos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='O+').count()
    Aneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='A-').count()
    Aneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='A-').count()
    Aneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='A-').count()
    Aneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='A-').count()
    Aneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='A-').count()
    Aneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='A-').count()
    Aneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='A-').count()
    Aneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='A-').count()
    Bneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='B-').count()
    Bneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='B-').count()
    Bneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='B-').count()
    Bneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='B-').count()
    Bneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='B-').count()
    Bneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='B-').count()
    Bneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='B-').count()
    Bneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='B-').count()
    Oneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='O-').count()
    Oneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='O-').count()
    Oneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='O-').count()
    Oneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='O-').count()
    Oneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='O-').count()
    Oneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='O-').count()
    Oneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='O-').count()
    Oneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='O-').count()
    ABneg100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='AB-').count()
    ABneg450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='AB-').count()
    ABpos100=UserProfileModel.objects.filter(user_profile_blood='100ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos150=UserProfileModel.objects.filter(user_profile_blood='150ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos200=UserProfileModel.objects.filter(user_profile_blood='200ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos250=UserProfileModel.objects.filter(user_profile_blood='250ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos300=UserProfileModel.objects.filter(user_profile_blood='300ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos350=UserProfileModel.objects.filter(user_profile_blood='350ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos400=UserProfileModel.objects.filter(user_profile_blood='400ml').filter(user_profile_bloodgroup='AB+').count()
    ABpos450=UserProfileModel.objects.filter(user_profile_blood='450ml').filter(user_profile_bloodgroup='AB+').count()
    
    return render(request,'admin/admin-view-all-bloodstock.html',{'Apos100':Apos100,'Apos150':Apos150,'Apos200':Apos200,'Apos250':Apos250,'Apos300':Apos300,'Apos350':Apos350,'Apos400':Apos400,'Apos450':Apos450,'Bpos100':Bpos100,'Bpos150':Bpos150,'Bpos200':Bpos200,'Bpos250':Bpos250,'Bpos300':Bpos300,'Bpos350':Bpos350,'Bpos400':Bpos400,'Bpos450':Bpos450,'Opos100':Opos100,'Opos150':Opos150,'Opos200':Opos200,'Opos250':Opos250,'Opos300':Opos300,'Opos350':Opos350,'Opos400':Opos400,'Opos450':Opos450,'Aneg100':Aneg100,'Aneg150':Aneg150,'Aneg200':Aneg200,'Aneg250':Aneg250,'Aneg300':Aneg300,'Aneg350':Aneg350,'Aneg400':Aneg400,'Aneg450':Aneg450,'Bneg100':Bneg100,'Bneg150':Bneg150,'Bneg200':Bneg200,'Bneg250':Bneg250,'Bneg300':Bneg300,'Bneg350':Bneg350,'Bneg400':Bneg400,'Bneg450':Bneg450,'Oneg100':Oneg100,'Oneg150':Oneg150,'Oneg200':Oneg200,'Oneg250':Oneg250,'Oneg300':Oneg300,'Oneg350':Oneg350,'Oneg400':Oneg400,'Oneg450':Oneg450,'ABpos100':ABpos100,'ABpos150':ABpos150,'ABpos200':ABpos200,'ABpos250':ABpos250,'ABpos300':ABpos300,'ABpos350':ABpos350,'ABpos400':ABpos400,'ABpos450':ABpos450,'ABneg100':ABneg100,'ABneg150':ABneg150,'ABneg200':ABneg200,'ABneg250':ABneg250,'ABneg300':ABneg300,'ABneg350':ABneg350,'ABneg400':ABneg400,'ABneg450':ABneg450 })

def admin_view_ngo_conducts_camps(request):
    data=NgoRegistrationModel.objects.all()
    return render(request,'admin/admin-view-ngo-conduct-camps.html',{'data':data})

# admin_login

def admin_login(request):
    if request.method=='POST':
        name=request.POST.get('username') 
        password=request.POST.get('password') 
        if name=='admin@gmail.com' and password=='cloud123':
           return redirect('admin_dashboard')
    
    return render(request,'admin/admin-login.html')

def admin_ngo_recevice_request(request):
    data=NgoRegistrationModel.objects.all()
    return render(request,'admin/ngo-recevice-request-form.html',{'data':data})



#actions
def ngo_register_accept(request,id):
    
    accept = get_object_or_404(NgoRegistrationModel,ngo_id=id)
    accept.ngo_status = 'Accepted'
    accept.save(update_fields=['ngo_status'])
    accept.save()
    
    #email message
    html_content = "<br/> <p> Blood_India application has been Accepted.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.ngo_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    return redirect('admin_ngo_recevice_request')


def ngo_register_reject(request,id):
    
    accept = get_object_or_404(NgoRegistrationModel,ngo_id=id)
    accept.ngo_status = 'Rejected'
    accept.save(update_fields=['ngo_status'])
    accept.save()
    
    #email message
    html_content = "<br/> <p> Blood_India application has been Rejected so please Reapply it.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.ngo_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    return redirect('admin_ngo_recevice_request')


def bloodbank_register_accept(request,id):
    
    accept = get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=id)
    accept.bloodbank_status = 'Accepted'
    accept.save(update_fields=['bloodbank_status'])
    accept.save()
    
    #email message
    html_content = "<br/> <p>  Blood_India application has been Accepted.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.Bloodemail]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    return redirect('admin_bloodbank_registration_form_request')


def bloodbank_register_reject(request,id):
    
    accept = get_object_or_404(BloodbankRegistrationModel,Bloodbank_id=id)
    accept.bloodbank_status = 'Rejected'
    accept.save(update_fields=['bloodbank_status'])
    accept.save()
    
    #email message
    html_content = "<br/> <p> Blood_India application has been Rejected so please Reapply it.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.Bloodemail]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    return redirect('admin_bloodbank_registration_form_request')

def use_register_accept(request,id):
    
    accept = get_object_or_404(UserRegistrationModel,user_id=id)
    accept.user_status = 'Accepted'
    accept.save(update_fields=['user_status'])
    accept.save()
    
    #email message
    html_content = "<br/> <p> Blood_India application has been Accepted.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.user_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    return redirect('admin_user_registration_form_request')



def use_register_rejected(request,id):
    
    accept = get_object_or_404(UserRegistrationModel,user_id=id)
    accept.user_status = 'Rejected'
    accept.save(update_fields=['user_status'])
    accept.save()
    
    #email message
    html_content = "<br/> <p> Blood_India application has been Rejected so please Reapply it.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.user_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    return redirect('admin_user_registration_form_request')



def hospital_register_accept(request,id):
    
    accept = get_object_or_404(HospitalRegistrationModel,hospital_id=id)
    accept.hospital_status = 'Accepted'
    accept.save(update_fields=['hospital_status'])
    accept.save()
    
    #email message
    html_content = "<br/> <p> Blood_India application has been Accepted.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.hpospital_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    return redirect('admin_hospital_registration_form_request')

def hospital_register_rejected(request,id):
    
    accept = get_object_or_404(HospitalRegistrationModel,hospital_id=id)
    accept.hospital_status = 'Rejected'
    accept.save(update_fields=['hospital_status'])
    accept.save()
    
    #email message
    html_content = "<br/> <p> Blood_India application has been Rejected so please Reapply it.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.hpospital_email]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Blood_India Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
       print(msg)
    return redirect('admin_hospital_registration_form_request')





# def user_delete(requset,id):
#     user=get_object_or_404(UserRegistrationModel,user_id=id)
#     return redirect()