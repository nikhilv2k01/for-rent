from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from re import M
from django.db import models

# Create your models here.


class UserReg(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    upload_image=models.ImageField(upload_to='images/',default=None)
    first_name=models.CharField(max_length=20,default="")
    last_name=models.CharField(max_length=20,default="")
    dateofbirth=models.CharField(max_length=100,default="")
    phone=models.CharField(max_length=20)
    city=models.CharField(max_length=20,default="")
    state=models.CharField(max_length=20,default="")

    class Meta:
        db_table = 'rent_user'


class PostProperty(models.Model):
    user_id=models.ForeignKey(UserReg,on_delete=models.CASCADE)
    type=models.CharField(max_length=20)
    owner_name=models.CharField(max_length=20)
    bed=models.IntegerField()
    bath=models.IntegerField()
    furnishing=models.CharField(max_length=20)
    built_area=models.IntegerField()
    carpet_area=models.IntegerField()
    total_floor=models.IntegerField()
    floor_no=models.BigIntegerField()
    bachelors_allowed=models.CharField(max_length=5,default="")
    street=models.CharField(max_length=30)
    district=models.CharField(max_length=30)
    upload_images=models.ImageField(upload_to='images/')
    price=models.IntegerField()
    
    contact_no = models.BigIntegerField()
    status = models.BooleanField(default=False)
    premium_package = models.BooleanField(default=False)

    class Meta:
        db_table='property'

class Favourites(models.Model):
    login_id=models.ForeignKey(UserReg,on_delete=models.CASCADE)
    property_id=models.ForeignKey(PostProperty,on_delete=models.CASCADE)
    
    class Meta:
        db_table="favourites"


   