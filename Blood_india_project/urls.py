"""Blood_india_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from userapp import views as user_views
from adminapp import views as admin_views
from bloodbankapp import views as bloodbank_views
from ngoapp import views as ngo_views
from hospitalapp import views as hospital_views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',user_views.home,name='home'),
    path('home2',user_views.home2,name='home2'),
    path('ngo_home',user_views.ngo_home,name='ngo_home'),
    path('about',user_views.about,name='about'),
    path('ngo_about',user_views.ngo_about,name='ngo_about'),
    path('user_about',user_views.user_about,name='user_about'),
    path('ngo_contact',user_views.ngo_contact,name='ngo_contact'),
    path('user_contact',user_views.user_contact,name='user_contact'),
    path('contact',user_views.contact,name='contact'),
    path('user_profile',user_views.user_profile,name='user_profile'),
    path('donateaction',user_views.donateaction,name='donateaction'),
    path('users_shows_bloodgroups',user_views.users_shows_bloodgroups,name='users_shows_bloodgroups'),
    path('user_blood_request',user_views.user_blood_request,name='user_blood_request'),
    path('ngo_request_new_camp',user_views.ngo_request_new_camp,name='ngo_request_new_camp'),
    path('recipent_profile',user_views.recipent_profile,name='recipent_profile'),
    path('user_registration',user_views.user_registration,name='user_registration'),
    path('user_type',user_views.user_type,name='user_type'),
    path('user_login',user_views.user_login,name='user_login'),
    # path('ngo_camp_request_form',user_views.ngo_camp_request_form,name='ngo_camp_request_form'),
    path('ngo_profile',user_views.ngo_profile,name='ngo_profile'),
    path('ngo_signup',user_views.ngo_signup,name='ngo_signup'),
    path('ngo_login',user_views.ngo,name='ngo'),
    path('user_show_conduct_camp',user_views.user_show_conduct_camp,name='user_show_conduct_camp'),
    path('user_show_after_login_conduct_camp',user_views.user_show_after_login_conduct_camp,name='user_show_after_login_conduct_camp'),
    path('users_shows_after_login_bloodgroups',user_views.users_shows_after_login_bloodgroups,name='users_shows_after_login_bloodgroups'),
    path('ngo_show_after_login_conduct_camp',user_views.ngo_show_after_login_conduct_camp,name='ngo_show_after_login_conduct_camp'),
    path('ngo_shows_after_login_bloodgroups',user_views.ngo_shows_after_login_bloodgroups,name='ngo_shows_after_login_bloodgroups'),
    # adminviews
    
    path('admin_dashboard',admin_views.admin_dashboard,name='admin_dashboard'),
    path('admin_bloodbank_registration_form_request',admin_views.admin_bloodbank_registration_form_request,name='admin_bloodbank_registration_form_request'),
    path('admin_hospital_registration_form_request',admin_views.admin_hospital_registration_form_request,name='admin_hospital_registration_form_request'),
    path('admin_user_registration_form_request',admin_views.admin_user_registration_form_request,name='admin_user_registration_form_request'),
    path('admin_view_hospitals_details',admin_views.admin_view_hospitals_details,name='admin_view_hospitals_details'),
    path('admin_view_bloodbanks_details',admin_views.admin_view_bloodbanks_details,name='admin_view_bloodbanks_details'),
    path('admin_view_user_details',admin_views.admin_view_user_details,name='admin_view_user_details'),
    path('admin_view_bloodstock_details',admin_views.admin_view_bloodstock_details,name='admin_view_bloodstock_details'),
    path('admin_view_ngo_conducts_camps',admin_views.admin_view_ngo_conducts_camps,name='admin_view_ngo_conducts_camps'),
    path('admin_login',admin_views.admin_login,name='admin_login'),
    path('admin_ngo_recevice_request',admin_views.admin_ngo_recevice_request,name='admin_ngo_recevice_request'),
    path('ngo_register_accept/<int:id>/',admin_views.ngo_register_accept,name='ngo_register_accept'),
    path('ngo_register_reject/<int:id>/',admin_views.ngo_register_reject,name='ngo_register_reject'),
    path('bloodbank_register_accept/<int:id>/',admin_views.bloodbank_register_accept,name='bloodbank_register_accept'),
    path('bloodbank_register_reject/<int:id>/',admin_views.bloodbank_register_reject,name='bloodbank_register_reject'),   
    path('use_register_accept/<int:id>/',admin_views.use_register_accept,name='use_register_accept'),   
    path('use_register_rejected/<int:id>/',admin_views.use_register_rejected,name='use_register_rejected'),   
    path('hospital_register_accept/<int:id>/',admin_views.hospital_register_accept,name='hospital_register_accept'),   
    path('hospital_register_rejected/<int:id>/',admin_views.hospital_register_rejected,name='hospital_register_rejected'),      
    
    
    
    
    
    
    
    
    
    #hospital_views
    
    path('hospital_dashboard',hospital_views.hospital_dashboard,name='hospital_dashboard'),
    path('hospital_profile',hospital_views.hospital_profile,name='hospital_profile'),
    path('hospital_view_donar_details_update_blood_details/<int:id>/',hospital_views.hospital_view_donar_details_update_blood_details,name='hospital_view_donar_details_update_blood_details'),
    path('hospital_registration',hospital_views.hospital_registration,name='hospital_registration'),
    path('hospital_view_blood_donated_user_details',hospital_views.hospital_view_blood_donated_user_details,name='hospital_view_blood_donated_user_details'),
    path('hospital_view_blood_stock',hospital_views.hospital_view_blood_stock,name='hospital_view_blood_stock'),
    path('hospital_view_donatedblood_to_hospitals',hospital_views.hospital_view_donatedblood_to_hospitals,name='hospital_view_donatedblood_to_hospitals'),
    path('hospital_view_bloodbanks_details',hospital_views.hospital_view_bloodbanks_details,name='hospital_view_bloodbanks_details'),
    path('hospital_blood_send_request_hospitals',hospital_views.hospital_blood_send_request_hospitals,name='hospital_blood_send_request_hospitals'),
    path('hospital_blood_receive_request_hospitals',hospital_views.hospital_blood_receive_request_hospitals,name='hospital_blood_receive_request_hospitals'),
    path('hospital_blood_receive_request_bloodbanks',hospital_views.hospital_blood_receive_request_bloodbanks,name='hospital_blood_receive_request_bloodbanks'),
    path('hospital_user_blood_recpitant_receive_request',hospital_views.hospital_user_blood_recpitant_receive_request,name='hospital_user_blood_recpitant_receive_request'),
    path('hospital_ngo_camp_condut_receive_request',hospital_views.hospital_ngo_camp_condut_receive_request,name='hospital_ngo_camp_condut_receive_request'),
    path('hospital_user_blood_donating_receive_request',hospital_views.hospital_user_blood_donating_receive_request,name='hospital_user_blood_donating_receive_request'),
    path('hospital_login',hospital_views.hospital_login,name='hospital_login'),
    path('hospital_accept/<int:id>/',hospital_views.hospital_accept,name='hospital_accept'),
    path('bloodbank_accept/<int:id>/',hospital_views.bloodbank_accept,name='bloodbank_accept'),
    path('reciptant_accept/<int:id>/',hospital_views.reciptant_accept,name='reciptant_accept'),
    path('hospital_rejected/<int:id>/',hospital_views.hospital_rejected,name='hospital_rejected'),
    path('bloodbank_rejected/<int:id>/',hospital_views.bloodbank_rejected,name='bloodbank_rejected'),
    path('reciptant_rejected/<int:id>/',hospital_views.reciptant_rejected,name='reciptant_rejected'),
    path('user_donate_accept/<int:id>/',hospital_views.user_donate_accept,name='user_donate_accept'),
    path('user_donate_rejected/<int:id>/',hospital_views.user_donate_rejected,name='user_donate_rejected'),
    path('hospital_ngo_accept/<int:id>/',hospital_views.hospital_ngo_accept,name='hospital_ngo_accept'),
    path('hospital_ngo_rejected/<int:id>/',hospital_views.hospital_ngo_rejected,name='hospital_ngo_rejected'),

    #bloodbank_views
    
    path('bloodbank_dashboard',bloodbank_views.bloodbank_dashboard,name='bloodbank_dashboard'),
    path('bloodbank_registration',bloodbank_views.bloodbank_registration,name='bloodbank_registration'),
    path('bloodbank_profile',bloodbank_views.bloodbank_profile,name='bloodbank_profile'),
    path('bloodbank_view_bloodstock',bloodbank_views.bloodbank_view_bloodstock,name='bloodbank_view_bloodstock'),
    path('bloodbank_view_blood_donated_hospitals',bloodbank_views.bloodbank_view_blood_donated_hospitals,name='bloodbank_view_blood_donated_hospitals'),
    path('bloodbank_view_blood_donar_details',bloodbank_views.bloodbank_view_blood_donar_details,name='bloodbank_view_blood_donar_details'),
    path('bloodbank_blood_send_request',bloodbank_views.bloodbank_blood_send_request,name='bloodbank_blood_send_request'),
    path('bloodbank_user_blood_donating_receivce_requset',bloodbank_views.bloodbank_user_blood_donating_receivce_requset,name='bloodbank_user_blood_donating_receivce_requset'),
    path('bloodbank_blood_request_receive_from_bloodbanks',bloodbank_views.bloodbank_blood_request_receive_from_bloodbanks,name='bloodbank_blood_request_receive_from_bloodbanks'),
    path('bloodbank_user_bloodrequesting_receive_request',bloodbank_views.bloodbank_user_bloodrequesting_receive_request,name='bloodbank_user_bloodrequesting_receive_request'),
    path('bloodbank_blood_receive_request_hospitals',bloodbank_views.bloodbank_blood_receive_request_hospitals,name='bloodbank_blood_receive_request_hospitals'),
    path('bloodbank_ngo_conduct_camp_recevie_request',bloodbank_views.bloodbank_ngo_conduct_camp_recevie_request,name='bloodbank_ngo_conduct_camp_recevie_request'),
    path('bloodbank_login',bloodbank_views.bloodbank_login,name='bloodbank_login'),
    path('bloodbank_accepted_view_details',bloodbank_views.bloodbank_accepted_view_details,name='bloodbank_accepted_view_details'),
    path('Bhospital_accept/<int:id>/',bloodbank_views.Bhospital_accept,name='Bhospital_accept'),
    path('Bbloodbank_accept/<int:id>/',bloodbank_views.Bbloodbank_accept,name='Bloodbank_accept'),
    path('Buserdonate_accept/<int:id>/',bloodbank_views.Buserdonate_accept,name='Buserdonate_accept'),
    path('Breciptant_accept/<int:id>/',bloodbank_views.Breciptant_accept,name='Breciptant_accept'),
    path('Buserdonate_Rejected/<int:id>/',bloodbank_views.Buserdonate_Rejected,name='Buserdonate_Rejected'),
    path('Bhospital_rejected/<int:id>/',bloodbank_views.Bhospital_rejected,name='Bhospital_rejected'),
    path('Breciptant_Rejected/<int:id>/',bloodbank_views.Breciptant_Rejected,name='Breciptant_Rejected'),
    path('Bbloodbank_Rejected/<int:id>/',bloodbank_views.Bbloodbank_Rejected,name='Bbloodbank_Rejected'),
    path('Bloodbank_ngo_accept/<int:id>/',bloodbank_views.Bloodbank_ngo_accept,name='Bloodbank_ngo_accept'),
    path('Bloodbank_ngo_Rejected/<int:id>/',bloodbank_views.Bloodbank_ngo_Rejected,name='Bloodbank_ngo_Rejected'),
    
    path('bloodbank_update_donation_blood_details/<int:id>/',bloodbank_views.bloodbank_update_donation_blood_details,name='bloodbank_update_donation_blood_details'),
     
  
    
    
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
