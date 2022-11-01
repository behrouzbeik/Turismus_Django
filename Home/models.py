from django.db import models

# IntegerRangeField Definition
class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

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
    TransportType=(
        ('BUS','Bu'),
        ('TRAIN', 'Tr'),
        ('AIR_PLAN', 'Pl'),
    )
    type = models.CharField ( max_length=2,choises=TransportType.choises )
    city = models.ForeignKey ( City,on_delete=models.CASCADE )
    terminalname = models.CharField ( max_length=50 )


class TransportCo (models.Model):    
    name = models.CharField ( max_length=50 )
    logo = models.ImageField ( blank=True,null=True,upload_to=None )
    userscore = models.PositiveIntegerField ( blank=True,null=True, )
    address = models.TextField ( blank=True,null=True, )
    telnum = models.CharField ( blank=True,null=True,max_length=15 )
    userscore = models.PositiveIntegerField ( blank=True,null=True )


class Extradition (models.Model):  
    exno = models.CharField( max_lenth=10 )  
    remainingtime = models.DurationField (  )
    percent = models.fields.IntegerRangeField ( min_value=1, max_value=100 )


class Transport (models.Model): 
    transportCode = models.CharField ( max_length=15 )
    company = models.ForeignKey ( TransportCo,on_delete=models.CASCADE )
    starttime = models.DateTimeField (  )
    recivetime = models.DateTimeField (  )
    beginning = models.ForeignKey ( Terminal,on_delete=models.CASCADE )
    distinaton = models.ForeignKey ( Terminal,on_delete=models.CASCADE )
    capacityadult = models.PositiveIntegerField (  )
    adultprice = models.PositiveIntegerField ( blank=True,null=True )
    childprice = models.PositiveIntegerField ( blank=True,null=True )
    babyprice = models.PositiveIntegerField ( blank=True,null=True )
    stars = models.PositiveIntegerField ( blank=True,null=True )
    discount = models.fields.IntegerRangeField ( blank=True,null=True,min_value=1, max_value=100 )
    userscore = models.PositiveIntegerField ( blank=True,null=True )
    buyscore = models.PositiveIntegerField ( blank=True,null=True )
    extradition = models.ForeignKey(Extradition,on_delete=models.CASCADE,relation='sa')


class Residence (models.Model): 
    ResideceType=(
        ('HOTEL','Ho'),
        ('MOTEL', 'Mo'),
        ('HAUSE', 'HA'),
        ('SUIT','Su'),
    )   
    name = models.CharField ( max_length=50 )
    type = models.CharField ( max_length=2,choises=ResideceType.choises )
    address = models.TextField (  )
    telnum = models.CharField ( max_length=15 )
    logo = models.ImageField ( blank=True,null=True,upload_to=None )
    userscore = models.PositiveIntegerField ( blank=True,null=True, )


class Room (models.Model):    
    residence = models.ForeignKey ( Residence,on_delete=models.CASCADE )
    startcontract = models.DateTimeField (  )
    endcontract = models.DateTimeField (  )
    adultprice = models.PositiveIntegerField (  )
    childprice = models.PositiveIntegerField (  )
    babyprice = models.PositiveIntegerField (  )
    discount = models.fields.IntegerRangeField ( blank=True,null=True,min_value=1, max_value=100 )
    adultcapacity = models.PositiveIntegerField (  )
    userscore = models.PositiveIntegerField ( blank=True,null=True )
    buyscore = models.PositiveIntegerField ( blank=True,null=True )
    extradition = models.ManyToManyField( Extradition,on_delete=models.CASCADE,related_name='exno' )


class Tour (models.Model):    
    name = models.CharField ( max_length=50 )
    transportGo = models.ForeignKey ( Transport,on_delete=models.CASCADE )
    transportBack = models.ForeignKey ( Transport,on_delete=models.CASCADE )
    hotel = models.ForeignKey ( Room,on_delete=models.CASCADE )
    userscore = models.PositiveIntegerField (  )
    description = models.TextField ( blank=True,null=True, )
    price = models.PositiveIntegerField (  )
    discount = models.fields.IntegerRangeField ( blank=True,null=True,min_value=1, max_value=100 )
    buyscore = models.PositiveIntegerField ( blank=True,null=True )
    extradition = models.ForeignKey(Extradition,on_delete=models.CASCADE,relation='sa')



