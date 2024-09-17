from django.db import models


# Create your models here.
class BloodbankRegistrationModel(models.Model):
   
    Bloodbank_id=models.AutoField(primary_key=True)
    Bloodname=models.TextField(help_text='Enter Your Name' , max_length=50)
    Bloodaddress=models.TextField(help_text='Enter Your address' , max_length=50)
    Bloodmobilenumber=models.BigIntegerField(help_text='Enter Your mobilenumber',max_length=50)
    Bloodemail=models.EmailField(help_text='Enter gmail', max_length=50)
    Bloodpassword=models.CharField(help_text='enter Password',max_length=200)
    Bloodreg_date=models.DateField(auto_now_add=True,null=True)
    bloodbank_upload_image=models.ImageField(help_text='Upload bloodbank_upload image ' , max_length=50,null=True)
    upload_bloodbank=models.ImageField(help_text=' upload_bloodbank image ' , max_length=50,null=True)
    bloodbank_status=models.CharField(help_text='bloodbank_status' ,default='Pending',max_length=200)

    class Meta:
        db_table='bloodbank_registration_details' 
        
        

class BloodbankSendRequestModel(models.Model): 
    b_id=models.AutoField(primary_key=True)
    bloodbank_id1 = models.ForeignKey(BloodbankRegistrationModel, on_delete=models.CASCADE,null=True)
    bloodbank_id=models.IntegerField(help_text='hospital_id' , max_length=50,null=True)
    bloodbank_name=models.TextField(help_text='Enter Your hospitalName' , max_length=50)    
    bloodbank_mobilenumber=models.BigIntegerField(help_text='Enter Your mobilenumber',max_length=50)
    bloodbank_bloodgroup_requried=models.CharField(help_text='Enter Your bloodgroup' , max_length=50)
    bloodbank_blood_requried_ml=models.CharField(help_text='Enter Your bloodrequried ml' , max_length=50)
    hospital_id=models.IntegerField(help_text='hospital_id' , max_length=50,null=True)
    bloodbank_send_reg_date=models.DateField(auto_now_add=True,null=True) 
    b_status=models.CharField(help_text='status'  ,default='Pending', max_length=50)  
    status=models.CharField(help_text='status'  ,default='Pending', max_length=50)
    Bloodemail=models.EmailField(help_text='Enter gmail',null=True)

    
    class Meta:
        db_table='bloodbank_send_bloodrequest_details'         