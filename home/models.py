from distutils.command.upload import upload
from django.db import models

# Create your models here.


class UserReg(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    

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
    bachelors_allowed=models.CharField(max_length=5)
    street=models.CharField(max_length=30)
    district=models.CharField(max_length=30)
    upload_images=models.ImageField(upload_to='images/')
    price=models.IntegerField()
    package=models.CharField(max_length=10,default="None")
    contact_no=models.BigIntegerField()

    class Meta:
        db_table='property'