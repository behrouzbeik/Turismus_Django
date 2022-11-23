from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from Home.models import *
from django.contrib.auth.models import UserManager

# Create your models here.

class CustomUser (AbstractUser, PermissionsMixin):
    USERTYPE=(
        ('Ma','MASTER'),
        ('Tr','TRAVELER'),
        ('Us','USER'),
        ('Bl','BLOGER'),
        ('Gu', 'GUIDE'),
    )
    mobile  = models.CharField ( max_length=15, default='0' )
    email = models.EmailField(unique=True)
    usertype = models.CharField ( max_length=2, choices=USERTYPE, default='Us' )
    firstname  = models.CharField ( blank=True,null=True,max_length=50 )
    lastname  = models.CharField ( blank=True,null=True,max_length=50 )
    unicid  = models.CharField ( max_length=10, unique=True )
    birthday  = models.DateTimeField ( blank=True,null=True )
    gender  = models.BooleanField ( blank=True,null=True )
    status = models.BooleanField(default=False)
    image = models.ImageField ( blank=True,null=True,upload_to='Profile' )
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True,null=True)
    profesional = models.CharField ( max_length=50, blank=True, null=True )

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Walet (models.Model):
    deposit  = models.PositiveIntegerField ( blank=True,null=True )
    harvest  = models.PositiveIntegerField ( blank=True,null=True )
    description  = models.CharField ( blank=True,null=True,max_length=50 )
    date  = models.DateTimeField (  )
    amount  = models.PositiveIntegerField (  )
    user  = models.ForeignKey ( CustomUser,on_delete=models.CASCADE )
    cash  = models.PositiveIntegerField (  )

    def __str__(self):
        return self.amount


class Score (models.Model):
    deposit  = models.PositiveIntegerField ( blank=True,null=True )
    hervest  = models.PositiveIntegerField ( blank=True,null=True )
    description  = models.CharField ( blank=True,null=True,max_length=50 )
    date  = models.DateTimeField (  )
    amount  = models.PositiveIntegerField (  )
    user  = models.ForeignKey ( CustomUser,on_delete=models.CASCADE )
    cash  = models.PositiveIntegerField (  )

    def __str__(self):
        return self.description


class Bank_deposit (models.Model):
    bank  = models.CharField ( max_length=50 )
    type  = models.CharField ( blank=True,null=True,max_length=50 )
    sheba  = models.CharField ( blank=True,null=True,max_length=50 )
    cardnumber  = models.CharField ( blank=True,null=True,max_length=50 )
    depositnumber  = models.CharField ( blank=True,null=True,max_length=50 )

    def __str__(self):
        return self.depositnumber


class Userscore (models.Model):
    tour  = models.ManyToManyField ( Tour,blank=True,null=True,related_name='tour_scr' )
    transportcompany  = models.ManyToManyField ( TransportCo,blank=True,null=True,related_name='transportco_scr' )
    transport  = models.ManyToManyField ( Transport,blank=True,null=True,related_name='transport_scr' )
    residence  = models.ManyToManyField ( Residence,blank=True,null=True,related_name='residence_scr' )
    room  = models.ManyToManyField ( Room,blank=True,null=True,related_name='room_scr' )
    rate  = models.PositiveIntegerField (  )
    description  = models.TextField (  )
    user  = models.ForeignKey ( CustomUser,on_delete=models.CASCADE )

    def __str__(self):
        return self.rate
