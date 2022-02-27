from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.html import format_html 

STATION = (
    ('Home','Home'),
    ('Office','Office'),
    ('Work','Works'),
    ('Others','Others'),
)
class Consumer(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    #User Manual Fields
    phone = models.IntegerField(default=0)
    city = models.CharField(max_length=100,default="0")
    state = models.CharField(max_length=100,default="0")
    zipcode = models.IntegerField(default="0")
    station = models.CharField(choices=STATION,max_length=20,default="Home")
    address = models.CharField(max_length=500,default="0") 
    email = models.EmailField(max_length=100,default="null@null.com") 
    otp = models.IntegerField(default=0,null=True)    
    #User Personal info
    local_ip = models.CharField(max_length=200,default=0) 
    browser = models.CharField(max_length=200,default=0) 
    router_ip = models.CharField(max_length=200,default=0) 
    #Phone Only
    mac_address =models.CharField(max_length=100,default=0) 
    #Auto Fields
    publish_date= models.DateTimeField(default=datetime.now,blank=True)
    update_date= models.DateTimeField('publish_date', auto_now=True)
    is_deleted =  models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_id(self):
        return str(self.id)
    

    
class Contacts(models.Model):
    username = models.CharField(max_length=15,default="")
    email = models.EmailField(max_length=30,default="")
    phone = models.IntegerField(default="")
    msg = models.CharField(max_length=900,default="")
    publish_date= models.DateTimeField(default=datetime.now,blank=True)
    update_date= models.DateTimeField('publish_date', auto_now=True)
    is_deleted = models.BooleanField(default=False)
    reslove = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
 
 
    