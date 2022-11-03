from django.db import models

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


class State (models.Model):    
    country = models.ForeignKey ( Country,on_delete=models.CASCADE )
    state = models.CharField ( max_length=50 )


class City (models.Model):    
    state = models.ForeignKey ( State,on_delete=models.CASCADE )
    city = models.CharField ( max_length=50 )


class Terminal (models.Model):    
    TRANSPORTTYPE=(
        ('Bu','BUS'),
        ('Tr','TRAIN'),
        ('Pl','AIR_PLAN'),
    )
    type = models.CharField ( max_length=2,choices=TRANSPORTTYPE )
    city = models.ForeignKey ( City,on_delete=models.CASCADE )
    terminalname = models.CharField ( max_length=50 )


class TransportCo (models.Model):    
    name = models.CharField ( max_length=50 )
    logo = models.ImageField ( blank=True,null=True,upload_to=None )
    address = models.TextField ( blank=True,null=True, )
    telnum = models.CharField ( blank=True,null=True,max_length=15 )
    userscore = models.PositiveIntegerField ( blank=True,null=True )


class Extradition (models.Model):  
    exno = models.CharField( max_length=10 )  
    remainingtime = models.DurationField (  )
    percent = models.PositiveIntegerField()


class Transport (models.Model): 
    transportCode = models.CharField ( max_length=15 )
    company = models.ForeignKey ( TransportCo,on_delete=models.CASCADE )
    starttime = models.DateTimeField (  )
    recivetime = models.DateTimeField (  )
    beginning = models.ForeignKey ( Terminal,on_delete=models.CASCADE,related_name='beginning' )
    distinaton = models.ForeignKey ( Terminal,on_delete=models.CASCADE,related_name='distinaton' )
    capacityadult = models.PositiveIntegerField (  )
    adultprice = models.PositiveIntegerField ( blank=True,null=True )
    childprice = models.PositiveIntegerField ( blank=True,null=True )
    babyprice = models.PositiveIntegerField ( blank=True,null=True )
    stars = models.PositiveIntegerField ( blank=True,null=True )
    discount = models.fields.PositiveIntegerField ( blank=True,null=True )
    userscore = models.PositiveIntegerField ( blank=True,null=True )
    buyscore = models.PositiveIntegerField ( blank=True,null=True )
    extradition = models.ManyToManyField( Extradition,related_name='tr_exno' )
    capacity = models.PositiveBigIntegerField(blank=True,null=True)


class Residence (models.Model): 
    RESIDENCE_TYPE=(
        ('Ho','HOTEL'),
        ('Mo','MOTEL'),
        ('HA','HAUSE'),
        ('Su','SUIT'),
    )   
    name = models.CharField ( max_length=50 )
    type = models.CharField ( max_length=2,choices=RESIDENCE_TYPE )
    address = models.TextField (  )
    telnum = models.CharField ( max_length=15 )
    logo = models.ImageField ( blank=True,null=True,upload_to=None )
    userscore = models.PositiveIntegerField ( blank=True,null=True, )
    capacity = models.PositiveBigIntegerField(blank=True,null=True)


class Room (models.Model):    
    residence = models.ForeignKey ( Residence,on_delete=models.CASCADE )
    startcontract = models.DateTimeField (  )
    endcontract = models.DateTimeField (  )
    adultprice = models.PositiveIntegerField (  )
    childprice = models.PositiveIntegerField (  )
    babyprice = models.PositiveIntegerField (  )
    discount = models.fields.PositiveIntegerField ( blank=True,null=True )
    adultcapacity = models.PositiveIntegerField (  )
    userscore = models.PositiveIntegerField ( blank=True,null=True )
    buyscore = models.PositiveIntegerField ( blank=True,null=True )
    extradition = models.ManyToManyField( Extradition,related_name='ro_exno' )
    capacity = models.PositiveBigIntegerField(blank=True,null=True)


class Tour (models.Model):    
    name = models.CharField ( max_length=50 )
    transportGo = models.ForeignKey ( Transport,on_delete=models.CASCADE,related_name='tr_go' )
    transportBack = models.ForeignKey ( Transport,on_delete=models.CASCADE,related_name='tr_ba' )
    hotel = models.ForeignKey ( Room,on_delete=models.CASCADE )
    userscore = models.PositiveIntegerField ( blank=True,null=True )
    description = models.TextField ( blank=True,null=True, )
    price = models.PositiveIntegerField (  )
    discount = models.fields.PositiveIntegerField ( blank=True,null=True )
    buyscore = models.PositiveIntegerField ( blank=True,null=True )
    extradition = models.ManyToManyField( Extradition,related_name='to_exno' )
    capacity = models.PositiveBigIntegerField(blank=True,null=True)



