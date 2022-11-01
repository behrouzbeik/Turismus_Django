from django.db import models

# Create your models here.


class Tour (models.Model):    
    name = models.CharField ( max_length=50 )
    transportGo = models.ForeignKey ( "Transport,on_delete=models.CASCADE" )
    transportBack = models.ForeignKey ( "Transport,on_delete=models.CASCADE" )
    Hotel = models.ForeignKey ( "Room,on_delete=models.CASCADE" )
    userscore = models.PositiveIntegerField (  )
    description = models.TextField (  )
    price = models.PositiveIntegerField (  )
    Discount = models.fields.IntegerRangeField ( "min_value=1, max_value=50" )
    buyscore = models.PositiveIntegerField (  )


class TransportCo (models.Model):    
    name = models.CharField ( max_length=50 )
    logo = models.ImageField ( upload_to=None )
    userscore = models.PositiveIntegerField (  )
    address = models.TextField (  )
    telnum = models.CharField ( max_length=15 )
    userscore = models.PositiveIntegerField (  )


class Transport (models.Model):    
    Type = models.CharField ( "max_length=2,choises=TransportType.choises" )
    TransportCode = models.CharField ( max_length=15 )
    starttime = models.DateTimeField (  )
    recivetime = models.DateTimeField (  )
    beginning = models.ForeignKey ( "City,on_delete=models.CASCADE" )
    distinaton = models.ForeignKey ( "City,on_delete=models.CASCADE" )
    company = models.ForeignKey ( "TransportCo,on_delete=models.CASCADE" )
    capacityadult = models.PositiveIntegerField (  )
    capacitychild = models.PositiveIntegerField (  )
    capacitybaby = models.PositiveIntegerField (  )
    adultprice = models.PositiveIntegerField (  )
    childprice = models.PositiveIntegerField (  )
    babyprice = models.PositiveIntegerField (  )
    stars = models.PositiveIntegerField (  )
    Discount = models.fields.IntegerRangeField ( "min_value=1, max_value=50" )
    userscore = models.PositiveIntegerField (  )
    buyscore = models.PositiveIntegerField (  )


class Residence (models.Model):    
    name = models.CharField ( max_length=50 )
    type = models.CharField ( "max_length=2,choises=ResideceType.choises" )
    address = models.TextField (  )
    telnum = models.CharField ( max_length=15 )
    logo = models.ImageField ( upload_to=None )
    userscore = models.PositiveIntegerField (  )


class room (models.Model):    
    residence = models.ForeignKey ( "Residence,on_delete=models.CASCADE" )
    startcontract = models.DateTimeField (  )
    endcontract = models.DateTimeField (  )
    adultprice = models.PositiveIntegerField (  )
    childprice = models.PositiveIntegerField (  )
    babyprice = models.PositiveIntegerField (  )
    Discount = models.fields.IntegerRangeField ( "min_value=1, max_value=50" )
    adultcapacity = models.PositiveIntegerField (  )
    childcapacity = models.PositiveIntegerField (  )
    babycapacity = models.PositiveIntegerField (  )
    userscore = models.PositiveIntegerField (  )
    buyscore = models.PositiveIntegerField (  )


class Extradition (models.Model):    
    transport = models.ForeignKey ( "Transport,on_delete=models.CASCADE" )
    remainingtime = models.DurationField (  )
    percent = models.fields.IntegerRangeField ( "min_value=1, max_value=50" )


class Terminal (models.Model):    
    terminaltype = models.CharField ( "max_length=2,choises=TransportType.choises" )
    city = models.ForeignKey ( "City,on_delete=models.CASCADE" )
    terminalname = models.CharField ( max_length=50 )


class City (models.Model):    
    state = models.ForeignKey ( "state,on_delete=models.CASCADE" )
    city = models.CharField ( max_length=50 )


class State (models.Model):    
    country = models.ForeignKey ( "Country,on_delete=models.CASCADE" )
    state = models.CharField ( max_length=50 )


class Country (models.Model):    
    country = models.CharField ( max_length=50 )
