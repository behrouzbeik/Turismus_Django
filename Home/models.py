from django.db import models
from django.urls import reverse
from djmoney.models.fields import MoneyField
from django.forms import ModelForm
from Blog.models import *
# from Home.models import *
# # IntegerRangeField Definition
# class IntegerRangeField(models.IntegerField):
#     def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
#         self.min_value, self.max_value = min_value, max_value
#         models.IntegerField.__init__(self, verbose_name, name, **kwargs)
#     def formfield(self, **kwargs):
#         defaults = {'min_value': self.min_value, 'max_value':self.max_value}
#         defaults.update(kwargs)
#         return super(IntegerRangeField, self).formfield(**defaults)

# Create your models here.
class Country (models.Model):    
    country = models.CharField ( max_length=50 )

    def __str__(self):
        return self.country


class State (models.Model):    
    country = models.ForeignKey ( Country,on_delete=models.CASCADE )
    state = models.CharField ( max_length=50 )

    def __str__(self):
        return self.state


class City (models.Model):    
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='City', blank=True, null=True)
    home_page_display = models.BooleanField(default=False)
    short_description = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.city



class Terminal (models.Model):
    TRANSPORTTYPE=(
        ('Bu','BUS'),
        ('Tr','TRAIN'),
        ('Pl','AIR_PLAN'),
        ('Cr','CRUISE'),
    )
    type = models.CharField ( max_length=2,choices=TRANSPORTTYPE )
    city = models.ForeignKey ( City,on_delete=models.CASCADE )
    terminalname = models.CharField ( max_length=50 )

    def __str__(self):
        return self.terminalname


class TransportCo (models.Model):    
    name = models.CharField ( max_length=50 )
    logo = models.ImageField ( blank=True,null=True,upload_to=None )
    address = models.TextField ( blank=True,null=True, )
    telnum = models.CharField ( blank=True,null=True,max_length=15 )
    userscore = models.PositiveIntegerField ( blank=True,null=True )

    def __str__(self):
        return self.name


class Extradition (models.Model):  
    exno = models.CharField( max_length=10 )  
    remainingtime = models.DurationField (  )
    percent = models.PositiveIntegerField()

    def __str__(self):
        return self.exno


class Transport (models.Model):
    GSTAR=(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
    ) 
    transportCode = models.CharField ( max_length=15 )
    company = models.ForeignKey ( TransportCo,on_delete=models.CASCADE )
    starttime = models.DateTimeField (  )
    recivetime = models.DateTimeField (  )
    beginning = models.ForeignKey ( Terminal,on_delete=models.CASCADE,related_name='beginning' )
    distination = models.ForeignKey ( Terminal,on_delete=models.CASCADE,related_name='distinaton' )
    adultprice = models.PositiveIntegerField ( blank=True,null=True )
    childprice = models.PositiveIntegerField ( blank=True,null=True )
    babyprice = models.PositiveIntegerField ( blank=True,null=True )
    graid_star=models.PositiveIntegerField(choices=GSTAR, default=0, blank=True,null=True)
    discount = models.fields.PositiveIntegerField ( blank=True,null=True )
    userscore = models.PositiveIntegerField ( blank=True,null=True )
    buyscore = models.PositiveIntegerField ( blank=True,null=True )
    extradition = models.ManyToManyField( Extradition,related_name='tr_exno' )
    capacity = models.PositiveBigIntegerField(blank=True,null=True)

    def __str__(self):
        return self.transportCode


class Residence (models.Model): 
    RESIDENCE_TYPE=(
        ('Ho','HOTEL'),
        ('Mo','MOTEL'),
        ('HA','HAUSE'),
        ('Su','SUIT'),
    )   
    GSTAR=(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
    )
    name = models.CharField ( max_length=50 )
    type = models.CharField ( max_length=2,choices=RESIDENCE_TYPE )
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True,null=True)
    address = models.TextField (  )
    telnum = models.CharField ( max_length=15 )
    logo = models.ImageField ( blank=True,null=True,upload_to='logo' )
    image = models.ImageField ( blank=True,null=True,upload_to=None )
    graid_star=models.PositiveIntegerField(choices=GSTAR, default=0, blank=True,null=True)
    buyscore = models.PositiveIntegerField ( blank=True,null=True )
    userscore = models.PositiveIntegerField ( blank=True,null=True, )
    capacity = models.PositiveBigIntegerField(blank=True,null=True)

    def __str__(self):
        return self.name


class Room (models.Model):    
    residence = models.ForeignKey ( Residence,on_delete=models.CASCADE )
    startcontract = models.DateTimeField (  )
    endcontract = models.DateTimeField (  )
    adultprice = MoneyField(max_digits=14, decimal_places=2, default_currency='IRR')
    childprice = MoneyField(max_digits=14, decimal_places=2, default_currency='IRR')
    babyprice = MoneyField(max_digits=14, decimal_places=2, default_currency='IRR')
    discount = models.fields.PositiveIntegerField ( blank=True,null=True )
    userscore = models.PositiveIntegerField ( blank=True,null=True )
    buyscore = models.PositiveIntegerField ( blank=True,null=True )
    extradition = models.ManyToManyField( Extradition,related_name='ro_exno' )
    capacity = models.PositiveBigIntegerField(blank=True,null=True)

    def __str__(self):
        return self.residence.name


class Tour (models.Model):    
    name = models.CharField ( max_length=50 )
    transportGo = models.ForeignKey ( Transport,on_delete=models.CASCADE,related_name='tr_go' )
    transportBack = models.ForeignKey ( Transport,on_delete=models.CASCADE,related_name='tr_ba' )
    hotel = models.ForeignKey ( Room,on_delete=models.CASCADE )
    image = models.ImageField (upload_to='Tour', blank=True, null=True)
    userscore = models.FloatField(default=0)
    description = models.TextField ( blank=True,null=True, )
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='IRR')
    discount = models.fields.PositiveIntegerField ( blank=True,null=True )
    buyscore = models.PositiveIntegerField ( blank=True,null=True )
    extradition = models.ManyToManyField( Extradition,related_name='to_exno' )
    capacity = models.PositiveBigIntegerField(blank=True,null=True)
    home_page_display = models.BooleanField(default=False)
    short_description = models.CharField(max_length=50, blank=True, null=True)
    detail_article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def tour_duration(self):
        timediff = self.transportBack.recivetime - self.transportGo.starttime
        return timediff.days

class MyCompanyInfo (models.Model):
    company_name = models.CharField(max_length=50, default='#')
    email = models.EmailField()
    phon_number = models.CharField(max_length=55)
    facebook = models.CharField(max_length=100, default='#')
    twiter = models.CharField(max_length=100, default='#')
    linkedin = models.CharField(max_length=100, default='#')
    insta = models.CharField(max_length=100, default='#')
    utube = models.CharField(max_length=100, default='#')



