from django.db import models

# Create your models here.


class UserRegistrationModel(models.Model): 
   user_id=models.AutoField(primary_key=True)
   user_name=models.TextField(help_text='Enter Your Name' , max_length=50)
   user_bloodgroup=models.CharField(help_text='Enter Your bloodgroup' , max_length=50)      
   user_email=models.EmailField(help_text='Enter Your email' , max_length=50) 
   user_mobilenumber=models.BigIntegerField(help_text='Enter Your mobilenumber' , max_length=50)
   user_dateofbirth=models.DateField(help_text='Enter Your dateofbirth' , max_length=50)
   user_password=models.CharField(help_text='Enter Your password' , max_length=50)
   user_address=models.TextField(help_text='Enter Your Address' , max_length=50,null=True)

   user_gender=models.CharField(help_text='Enter Your gender' , max_length=50,null=True)
   user_upload_profile=models.ImageField(help_text='Upload your image' , max_length=50,null=True)
   user_reg_date=models.DateField(auto_now_add=True,null=True)
   user_status=models.CharField(help_text='user_status', default='Pending',max_length=200)

   class Meta:
        db_table='user_registration_details'

# Ngo details

class NgoRegistrationModel(models.Model):
    ngo_id=models.AutoField(primary_key=True)
    ngo_name=models.TextField(help_text='Enter Your Name' , max_length=50)
    ngo_address=models.TextField(help_text='Enter Your address' , max_length=50)
    ngo_mobilenumber=models.BigIntegerField(help_text='Enter Your mobilenumber',max_length=50)
    ngo_email=models.EmailField(help_text='Enter gmail', max_length=50)
    ngo_password=models.CharField(help_text='enter Password',max_length=200)
    ngo_reg_date=models.DateField(auto_now_add=True,null=True)
    ngo_status=models.CharField(help_text='Status' ,default='Pending' , max_length=50)

    ngo_upload_image=models.ImageField(help_text='Upload ngo image' , max_length=50,null=True)

    class Meta:
        db_table='ngo_registration_details'    

class NgoCampConductModel(models.Model):
    ngo_camp_id=models.AutoField(primary_key=True)
    ngo_camp_name=models.CharField(help_text='Enter Your centername' , max_length=50)
    ngo_camp_location=models.TextField(help_text='Enter Your location' , max_length=50)
    ngo_camp_contact=models.CharField(help_text='Enter contact ' , max_length=50,null=True)
    ngo_camp_person_name=models.CharField(help_text='Enter contact person name' , max_length=50,null=True)
    ngo_conduct_time=models.TimeField(help_text='Enter time', max_length=50,null=True)
    ngo_conduct_end_time=models.TimeField(help_text='Enter time', max_length=50,null=True)
    ngo_conduct_date=models.DateField(help_text='enter date',max_length=200)
    ngo_reg_date=models.DateField(auto_now_add=True,null=True)
    hospital_id=models.IntegerField(help_text='hospital_id' , max_length=50,null=True)
    bloodbank_id=models.IntegerField(help_text='bloodbank_id' , max_length=50,null=True)
    status=models.CharField(help_text='Status' ,default='Pending', max_length=50)
    n_status=models.CharField(help_text='status'  ,default='Pending', max_length=50)
    ngo_email=models.EmailField(help_text='Enter gmail', max_length=50,null=True)
    class Meta:
        db_table='ngo_conduct_camps_details'             


class UserProfileModel(models.Model): 
#    user_id = models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE,null=True)
   user_profile_id=models.AutoField(primary_key=True)
   hospital_id=models.IntegerField(help_text='hospital_id' , max_length=50,null=True)
   bloodbank_id=models.IntegerField(help_text='bloodbank_id' , max_length=50,null=True)
   user_profile_name=models.TextField(help_text='Enter Your Name' , max_length=50)
   user_profile_bloodgroup=models.CharField(help_text='Enter Your bloodgroup' , max_length=50)      
   user_profile_address=models.CharField(help_text='Enter donor address' , max_length=50,null=True)      
   user_upload=models.ImageField(help_text='Upload your image' , max_length=50,null=True)
   user_profile_email=models.EmailField(help_text='Enter Your email' , max_length=50) 
   user_profile_mobilenumber=models.BigIntegerField(help_text='Enter Your mobilenumber' , max_length=50,null=True)
   user_profile_blood=models.CharField(help_text='blood' , max_length=50,null=True)
   user_profile_reg_date=models.DateField(auto_now_add=True,null=True)  
   user_profile_blood_donated_date=models.DateField(auto_now_add=True,null=True) 
   user_profile_certificate=models.CharField(help_text='certificate' , max_length=50)
   user_profile_donated_lastmonth=models.CharField(help_text='dontedlast months' , max_length=50,null=True)
   P_status=models.CharField(help_text='status'  ,default='Pending', max_length=50)
   status=models.CharField(help_text='Status' ,default='Pending' , max_length=50,)
   class Meta:
        db_table='user_donate_request_details'  
        
        
class UserReciptantModel(models.Model): 
   user_id = models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE,null=True)
   user_reciptant_id=models.AutoField(primary_key=True)
   user_reciptant_name=models.TextField(help_text='Enter Your Name' , max_length=50)   
   user_reciptant_email=models.EmailField(help_text='Enter Your email' , max_length=50) 
   user_reciptant_mobilenumber=models.BigIntegerField(help_text='Enter Your mobilenumber' , max_length=50)
   user_reciptant_requried_ml=models.CharField(help_text='enter requried ml',max_length=50,null=True)
   bloodbank_id=models.IntegerField(help_text='bloodbank_id' , max_length=50,null=True)
   u_status=models.CharField(help_text='status'  ,default='Pending', max_length=50)
   status=models.CharField(help_text='Status' ,default='Pending' , max_length=50)
   user_reciptant_requried_bloodgroup=models.CharField(help_text='enter requried bloodgroup',max_length=50,null=True)
   user_reciptant_reg_date=models.DateField(auto_now_add=True,null=True)  
   hospital_id=models.IntegerField(help_text='hospital_id' , max_length=50,null=True)
  
   
   class Meta:
        db_table='user_reciptant_request_details'         