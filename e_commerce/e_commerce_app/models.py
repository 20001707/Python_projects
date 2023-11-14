from django.db import models

    
class add_prod(models.Model):
    categories=models.CharField(max_length=30)
    prize=models.IntegerField()
    age_range=models.CharField(max_length=30)
    brand=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    productimg=models.FileField(upload_to='e_commerce_app/static/images')
    def __str__(self):
       return self.categories
class new_register_model(models.Model):
    name=models.CharField(max_length=30)
    pimage=models.FileField(upload_to='e_commerce_app/static')
    username=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
  
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class user_register_model(models.Model):
    uname=models.CharField(max_length=30)
    uusername=models.CharField(max_length=30)
    uemail=models.EmailField()
    uphone=models.IntegerField()
    proimage=models.FileField(upload_to='e_commerce_app/static')
    upassword=models.CharField(max_length=30)
    def __str__(self):
        return self.uusername
    
class wishmodel(models.Model):
    userid=models.IntegerField()
    prod_id=models.IntegerField()
    categories=models.CharField(max_length=30)
    prize=models.IntegerField()
    brand=models.CharField(max_length=30)
    productimg=models.FileField()
    def __str__(self):
        return self.categories
    


class cartmodel(models.Model):
    userid=models.IntegerField()
    prod_id=models.IntegerField()
    categories=models.CharField(max_length=30)
    prize=models.IntegerField()
    brand=models.CharField(max_length=30)
    productimg=models.FileField()
    quantity=models.IntegerField()
    
class addressmodel(models.Model):
    userid=models.IntegerField()
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    pincode=models.IntegerField()
    
    
    
    
    
       


    
    


       



# Create your models here.
