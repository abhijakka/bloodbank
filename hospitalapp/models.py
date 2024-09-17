from django.db import models

# Create your models here.
class HospitalRegistrationModel(models.Model):
    
    hospital_id=models.AutoField(primary_key=True)
    hospital_name=models.TextField(help_text='Enter Your hospitalName' , max_length=50)
    hospital_address=models.TextField(help_text='Enter Your hospitaladdress' , max_length=50)
    hospital_mobilenumber=models.BigIntegerField(help_text='Enter Your mobilenumber',max_length=50)
    hpospital_email=models.EmailField(help_text='Enter email', max_length=50)
    hospital_password=models.CharField(help_text='enter Password',max_length=200)
    hospital_reg_date=models.DateField(auto_now_add=True,null=True)
    hospital_status=models.CharField(help_text='hospital_status' ,default='Pending',max_length=200)
    
    hospital_upload_image=models.ImageField(help_text='Upload hospital image ' , max_length=50,null=True)

    class Meta:
        db_table='hospital_registration_details' 


class HospitalSendRequestModel(models.Model): 
    h_id=models.AutoField(primary_key=True)
    hospital_id = models.IntegerField(help_text='hosptal_id' , max_length=50,null=True)
    hospital_name=models.TextField(help_text='Enter Your hospitalName' , max_length=50,null=True)
    hospital_email=models.EmailField(help_text='Enter email', max_length=50,null=True)    
    hospital_mobilenumber=models.BigIntegerField(help_text='Enter Your mobilenumber',max_length=50)
    hospital_bloodgroup_requried=models.CharField(help_text='Enter Your bloodgroup' , max_length=50)
    hospital_blood_requried_ml=models.CharField(help_text='Enter Your bloodrequried ml' , max_length=50)
    hospital_status=models.CharField(help_text='status' ,default='Pending' , max_length=50,null=True)
    h_status=models.CharField(help_text='status'  ,default='Pending', max_length=50)
    
    hospital_send_reg_date=models.DateField(auto_now_add=True,null=True)   
    bloodbank_id=models.IntegerField(help_text='bloodbank_id' , max_length=50,null=True)

    
    class Meta:
        db_table='hospital_send_bloodrequest_details' 