from django.db import models

class Consumer(models.Model):
    user = 
    phone = 
    city = 
    state = 
    zipcode =
    publish_date = 
    update_date = 
    is_deleted =  
    otp = 
    local_ip = 
    browser =
    router_ip = 
    address = 
    password = 
    #Phone Only
    mac_address =
    
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
    update_date= models.DateTimeField(default=datetime.now,blank=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
 
class 
    