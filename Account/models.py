from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from Home.models import *

# Create your models here.

class CustomUser (AbstractBaseUser):
    USERTYPE=(
        ('Ma','MASTER'),
        ('Tr','TRAVELER'),
        ('Us','USER'),
    )
    mobile  = models.CharField ( max_length=15 )
    email = models.EmailField(unique=True)
    usertype = models.CharField ( max_length=2,choices=USERTYPE )
    firstname  = models.CharField ( blank=True,null=True,max_length=50 )
    lastname  = models.CharField ( blank=True,null=True,max_length=50 )
    unicid  = models.CharField ( max_length=10 )
    birthday  = models.DateTimeField ( blank=True,null=True )
    gender  = models.BooleanField ( blank=True,null=True )
    status = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Walet (models.Model):
    deposit  = models.PositiveIntegerField ( blank=True,null=True )
    harvest  = models.PositiveIntegerField ( blank=True,null=True )
    description  = models.CharField ( blank=True,null=True,max_length=50 )
    date  = models.DateTimeField (  )
    amount  = models.PositiveIntegerField (  )
    user  = models.ForeignKey ( CustomUser,on_delete=models.CASCADE )
    cash  = models.PositiveIntegerField (  )


class Score (models.Model):
    deposit  = models.PositiveIntegerField ( blank=True,null=True )
    hervest  = models.PositiveIntegerField ( blank=True,null=True )
    description  = models.CharField ( blank=True,null=True,max_length=50 )
    date  = models.DateTimeField (  )
    amount  = models.PositiveIntegerField (  )
    user  = models.ForeignKey ( CustomUser,on_delete=models.CASCADE )
    cash  = models.PositiveIntegerField (  )


class Bank_deposit (models.Model):
    bank  = models.CharField ( max_length=50 )
    type  = models.CharField ( blank=True,null=True,max_length=50 )
    sheba  = models.CharField ( blank=True,null=True,max_length=50 )
    cardnumber  = models.CharField ( blank=True,null=True,max_length=50 )
    depositnumber  = models.CharField ( blank=True,null=True,max_length=50 )


class Userscore (models.Model):
    tour  = models.ManyToManyField ( Tour,blank=True,null=True,related_name='tour_scr' )
    transportcompany  = models.ManyToManyField ( TransportCo,blank=True,null=True,related_name='transportco_scr' )
    transport  = models.ManyToManyField ( Transport,blank=True,null=True,related_name='transport_scr' )
    residence  = models.ManyToManyField ( Residence,blank=True,null=True,related_name='residence_scr' )
    room  = models.ManyToManyField ( Room,blank=True,null=True,related_name='room_scr' )
    rate  = models.PositiveIntegerField (  )
    description  = models.TextField (  )
    user  = models.ForeignKey ( CustomUser,on_delete=models.CASCADE )
