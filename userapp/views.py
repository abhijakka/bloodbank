from ast import Pass
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from userapp.models import *
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.http import HttpResponseRedirect
import requests
import random
from django.db.models import Q

# Create your views here.




def home(request):
    
    return render(request,'user/index.html')

def home2(request):
    
    return render(request,'user/index2.html')


def ngo_home(request):
    
    return render(request,'user/ngo-index.html')
def ngo_about(request):
    
    return render(request,'user/ngo-about.html')
def user_about(request):
    
    return render(request,'user/user-about.html')

def about(request):
    
    return render(request,'user/About.html')

def contact(request):
    
    return render(request,'user/contact.html')
def ngo_contact(request):
    
    return render(request,'user/ngo-contact.html')
def user_contact(request):
    
    return render(request,'user/user-contact.html')

def user_profile(request):
    
    data = request.session['user_id']
    print(data)
    
   
    data2=UserRegistrationModel.objects.filter(user_id = data)
    
    print(data2)
     
    obj= get_object_or_404(UserRegistrationModel,user_id=data)
    
     
    if request.method =='POST' and  request.FILES['user_profile_update']:
      
        user_name=request.POST.get('name')
        user_email=request.POST.get('profile_email')
        user_upload_profile=request.FILES['user_profile_update']
        user_bloodgroup=request.POST.get('profile_blood_group')
        user_mobilenumber=request.POST.get('profile_mobile')
        user_address=request.POST.get('profile_address')
       
        
        
        obj.user_name=user_name
        obj.user_email=user_email
        obj.user_upload_profile=user_upload_profile
        obj.user_bloodgroup=user_bloodgroup
        obj.user_mobilenumber=user_mobilenumber
        obj.user_address=user_address
   
        
        
        obj.save(update_fields=['user_name','user_email','user_bloodgroup','user_mobilenumber','user_address','user_upload_profile'])
        
    return render(request,'user/donor-profile.html',{'data':data2, 'view':data})

def donateaction(request):
    
    data = request.session['user_id']
    
    
    data2=UserRegistrationModel.objects.filter(user_id = data)
    
    print(data2)
     
    print("function callll")
 
    if request.method == "POST":   
        print('post method')
        user_profile_name=request.POST.get('name')
        user_profile_email=request.POST.get('profile_email')
        user_upload=request.POST['upload_profile']
        user_profile_bloodgroup=request.POST.get('profile_blood_group')
        user_profile_mobilenumber=request.POST.get('profile_mobile')
        user_profile_donated_lastmonth=request.POST.get('profile_donated_lastmonth')
        user_profile_address=request.POST.get('profile_address')
        
        
        user=UserProfileModel.objects.create(user_profile_email=user_profile_email, user_profile_name=user_profile_name, user_profile_bloodgroup=user_profile_bloodgroup, user_profile_mobilenumber=user_profile_mobilenumber, user_profile_donated_lastmonth=user_profile_donated_lastmonth,user_profile_address=user_profile_address,user_upload=user_upload)
        user.save()
        if user:
            messages.success(request,"Your Request Form Is Successfully Uploaded")       
        else:
            
            Pass
        
    return render(request,'user/user-donate.html',{'data':data2,'view':data})
   
def ngo_request_new_camp(request):
    data2=request.session['ngo_id']
    data=NgoRegistrationModel.objects.all().filter(ngo_id=data2)
    
    if request.method == 'POST' :
        
      ngo_camp_name=request.POST.get('ngo_camp_name')
      ngo_camp_person_name=request.POST.get('ngo_camp_person_name')
      ngo_conduct_time=request.POST.get('ngo_conduct_time')
      ngo_conduct_end_time=request.POST.get('ngo_conduct_end_time')
      ngo_conduct_date=request.POST.get('ngo_conduct_date')
      ngo_email=request.POST.get('ngo_email')
      ngo_camp_location=request.POST.get('ngo_camp_location')
      ngo_camp_contact=request.POST.get('ngo_contact')

      ngo=NgoCampConductModel.objects.create(ngo_email=ngo_email,ngo_camp_contact=ngo_camp_contact,ngo_camp_name=ngo_camp_name,ngo_camp_person_name=ngo_camp_person_name,ngo_conduct_time=ngo_conduct_time,ngo_conduct_end_time=ngo_conduct_end_time,ngo_conduct_date=ngo_conduct_date,ngo_camp_location=ngo_camp_location)
      ngo.save()
      if ngo:
        messages.success(request,"Your Request Form Is Successfully Uploaded")       
      else:
        pass
    
    return render(request,'user/ngo-newcamp-request-form.html',{'data':data})







def user_blood_request(request):
    
    data = request.session['user_id']
    
    
    data2=UserRegistrationModel.objects.filter(user_id = data)
    
    print(data2)
     
    print("function callll")
 
    if request.method == "POST" :  
        print('post method')
        user_reciptant_name=request.POST.get('name')
        user_reciptant_email=request.POST.get('profile_email')
        
        user_reciptant_mobilenumber=request.POST.get('profile_mobile')
        user_reciptant_requried_ml=request.POST.get('reciptant_blood_requried_ml')
        user_reciptant_requried_bloodgroup=request.POST.get('reciptant_blood_group_requried')
        
        user=UserReciptantModel.objects.create(user_reciptant_name=user_reciptant_name, user_reciptant_email=user_reciptant_email, user_reciptant_mobilenumber=user_reciptant_mobilenumber, user_reciptant_requried_ml=user_reciptant_requried_ml, user_reciptant_requried_bloodgroup=user_reciptant_requried_bloodgroup)
        user.save()
        
        if user:
            messages.success(request,"Your Request Form Is Successfully Uploaded")       
        else:
            
            Pass
    
      
    return render(request,'user/user-blood-request.html',{'data':data2,'view':data})  

def recipent_profile(request,):
     
    data = request.session['user_id']
    print(data)
    
   
    data2=UserRegistrationModel.objects.filter(user_id = data)
    
    print(data2)
     
    obj= get_object_or_404(UserRegistrationModel,user_id=data)
   
     
    if request.method =='POST':
       
        user_name=request.POST.get('name')
        user_email=request.POST.get('profile_email')
        
       
        user_mobilenumber=request.POST.get('profile_mobile')
      
       
        
        
        obj.user_name=user_name
        obj.user_email=user_email
        
       
        obj.user_mobilenumber=user_mobilenumber
        
   
        
        
        obj.save(update_fields=['user_name','user_email','user_mobilenumber'])
        
    
    
    return render(request,'user/reciptent-profile.html',{'data':data2})

def user_registration(request) :
     if request.method =='POST' and  request.FILES['upload_profile']:
        user_name=request.POST.get('yourname')
        user_email=request.POST.get('email')
        user_password=request.POST.get('user_password')
        user_bloodgroup=request.POST.get('bgroup')
        user_mobilenumber=request.POST.get('mobile')
        user_dateofbirth=request.POST.get('dob')
        user_address=request.POST.get('user_address')
        user_upload_profile=request.FILES['upload_profile']
        user_gender=request.POST.get('user_gender')
        if UserRegistrationModel.objects.filter(user_email=user_email).exists():
            messages.error(request,"Email Already Existed")
            return redirect("user_registration")
        else:
            user=UserRegistrationModel.objects.create(user_name=user_name,user_email=user_email,user_password=user_password,user_bloodgroup=user_bloodgroup,user_mobilenumber=user_mobilenumber,user_dateofbirth=user_dateofbirth,user_upload_profile=user_upload_profile,user_gender=user_gender,user_address=user_address)
            user.save()
            messages.success(request,"Your Account Is Successfully Registered")  
    
     return render(request,'user/user-registration-form.html')

def user_type(request):
    data = request.session['user_id']
    print(data)
    
    data2=UserRegistrationModel.objects.filter(user_id = data)
    
    print(data2)
    
    return render(request,'user/user-type.html',{'view':data2})

# def ngo(request):
#     if request.method=='POST':
        
#       email = request.POST.get('email')
#       password = request.POST.get('password') 
      
#       try:
#             check = NgoRegistrationModel.objects.get(ngo_email=email,ngo_password=password)
          
#             request.session['ngo_id'] = check.ngo_id
#             messages.success(request,"Your Are Successfully Logged")   
#             return redirect ('ngo_profile')
        
#       except:
#             messages.error(request,"Your Email or Password Given Worng")
#             return redirect ('ngo')
    
#     return render(request,'user/ngo-login.html')

def ngo(request):
     if request.method == 'POST': 
                email = request.POST.get('email') 
                password = request.POST.get('password') 
                try: 
                     check = NgoRegistrationModel.objects.get(ngo_email=email,ngo_password=password)   
                     request.session['ngo_id']=check.ngo_id  
                       
                     ngo_status = check.ngo_status 
                     if ngo_status =='Accepted': 
                         messages.success(request,'login success') 
                         return redirect('ngo_profile')  
                     elif ngo_status =='Rejected' :  
                         messages.error(request,'Your request is Rejected so you cannot login')   
                     elif ngo_status == 'Pending': 
                         messages.info(request,'Your request is Pending so cannot login')   
 
                      
                except: 
                     messages.warning(request,'invalid login') 
                                   
     return render(request,'user/ngo-login.html')








def ngo_signup(request): 
         if request.method =='POST'and request.FILES['ngo_upload']:
            ngo_name=request.POST.get('ngo_name')
            ngo_email=request.POST.get('ngo_email')
            ngo_password=request.POST.get('ngo_password')
            ngo_address=request.POST.get('ngo_address')
            ngo_mobilenumber=request.POST.get('ngo_mobilenumber')
            ngo_upload_image=request.FILES['ngo_upload']
            
            if NgoRegistrationModel.objects.filter(ngo_email=ngo_email).exists():
             messages.error(request,"Email Already Existed")
             return redirect("signup")
            else:
              user=NgoRegistrationModel.objects.create(ngo_name=ngo_name,ngo_email=ngo_email,ngo_password=ngo_password,ngo_address=ngo_address,ngo_mobilenumber=ngo_mobilenumber,ngo_upload_image=ngo_upload_image)
              user.save()
            messages.success(request,"Your Account Is Successfully Registered") 
    
         return render(request,'user/ngo-signup.html')

def ngo_profile(request):
    data=request.session['ngo_id']
    ngo_profile1=NgoRegistrationModel.objects.all().filter(ngo_id=data)
    obj= get_object_or_404(NgoRegistrationModel,ngo_id=data)
   
     
    if request.method =='POST'and request.FILES['ngo_update_image']:
       
        ngo_name=request.POST.get('ngo_name')
        ngo_address=request.POST.get('ngo_address')
        ngo_email=request.POST.get('ngo_email')
        ngo_upload_image=request.FILES['ngo_update_image']
        ngo_mobilenumber=request.POST.get('ngo_mobilenumber')
      
       
        
        
        obj.ngo_name=ngo_name
        obj.ngo_address=ngo_address
        obj.ngo_upload_image=ngo_upload_image
        obj.ngo_mobilenumber=ngo_mobilenumber
        obj.ngo_email=ngo_email
        
   
        
        
        obj.save(update_fields=['ngo_name','ngo_address','ngo_upload_image','ngo_mobilenumber','ngo_email'])
    
    return render(request,'user/ngo-profile.html',{'ngo_profile':ngo_profile1})



def user_show_conduct_camp(request):
    
    ngo_profile2=NgoCampConductModel.objects.all().filter(n_status='Accepted')
    
    return render(request,'user/user-shows-camp-conduct.html',{'ngo_profile':ngo_profile2})

def user_show_after_login_conduct_camp(request):
    
    data=NgoCampConductModel.objects.all().filter(n_status='Accepted')
    
    return render(request,'user/user-after-login-shows-camp-conduct.html',{'data':data})


def ngo_show_after_login_conduct_camp(request):
    
    data=NgoCampConductModel.objects.all().filter(n_status='Accepted')
    
    return render(request,'user/ngo-after-login-shows-camp-conduct.html',{'data':data})



def users_shows_after_login_bloodgroups(request):
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='A+').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='A-').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='B+').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='B-').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='AB+').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='AB-').order_by('-user_profile_reg_date')
    if request.method=='POST':
        search=request.POST.get('search')
        BloodgroupApos=UserProfileModel.objects.filter(Q(user_profile_bloodgroup__exact=search ))
    else:
        pass
    
    return render(request,'user/user-after-login-shows-bloodgroups.html',{'data':BloodgroupApos})

def ngo_shows_after_login_bloodgroups(request):
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='A+').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='A-').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='B+').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='B-').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='AB+').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='AB-').order_by('-user_profile_reg_date')
    if request.method=='POST':
        search=request.POST.get('search')
        BloodgroupApos=UserProfileModel.objects.filter(Q(user_profile_bloodgroup__exact=search ))
    else:
        pass
    
    return render(request,'user/ngo-after-login-shows-bloodgroups.html',{'c':BloodgroupApos})



def users_shows_bloodgroups(request):
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='A+').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='A-').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='B+').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='B-').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='AB+').order_by('-user_profile_reg_date')
    BloodgroupApos=UserProfileModel.objects.all().filter(user_profile_bloodgroup='AB-').order_by('-user_profile_reg_date')
    if request.method=='POST':
        search=request.POST.get('search')
        BloodgroupApos=UserProfileModel.objects.filter(Q(user_profile_bloodgroup__exact=search ))
    else:
        pass
    
    return render(request,'user/user-shows-bloodgroups.html',{'a':BloodgroupApos})


# def user_login(request):
#      if request.method=='POST':
        
#       email = request.POST.get('email')
#       password = request.POST.get('password') 
#       print(email)
#       try:
#             check = UserRegistrationModel.objects.get(user_email=email,user_password=password)
          
#             request.session['user_id'] = check.user_id
#             messages.success(request,"Your Are Successfully Logged")   
#             return redirect ('user_type')
        
#       except:
#             messages.error(request,"Your Email or Password Given Worng")
#             return redirect ('user_login')
    
#      return render(request,'user/user-login.html')
 
def user_login(request):
     if request.method == 'POST': 
                email = request.POST.get('email') 
                password = request.POST.get('password') 
                try: 
                     check = UserRegistrationModel.objects.get(user_email=email,user_password=password)   
                     request.session['user_id']=check.user_id  
                       
                     user_status = check.user_status 
                     if user_status =='Accepted': 
                         messages.success(request,'login success') 
                         return redirect('user_type')  
                     elif user_status =='Rejected' :  
                         messages.error(request,'Your request is Rejected so you cannot login')   
                     elif user_status == 'Pending': 
                         messages.info(request,'Your request is Pending so cannot login')   
 
                      
                except: 
                     messages.warning(request,'invalid login') 
                                   
     return render(request,'user/user-login.html')