from django.db import models
from Home.models import *
from Account.models import CustomUser

# Create your models here.
class Order (models.Model):
    orderno = models.CharField ( max_length=10,unique=True )
    ordertime  =  models.DateTimeField ( auto_now_add=True )
    tour  =  models.ForeignKey ( Tour,on_delete=models.CASCADE,blank=True,null=True )
    transport  =  models.ForeignKey ( Transport,on_delete=models.CASCADE,blank=True,null=True )
    room  =  models.ForeignKey ( Room,on_delete=models.CASCADE,blank=True,null=True )
    adult = models.PositiveIntegerField(  )
    child = models.PositiveIntegerField(blank=True,null=True)
    baby=models.PositiveIntegerField(blank=True,null=True)
    user  =  models.ForeignKey ( CustomUser,on_delete=models.CASCADE )

    def __str__(self):
        return self.orderno


class OrderStatus (models.Model):
    ORDERSTATE=(
        ('Un','UNPAID'),
        ('Pa','PAID'),
        ('Ca','CANCEL'),
        ('Do','DONE'),
    )
    order = models.ForeignKey( Order,on_delete=models.CASCADE )
    status  =  models.CharField ( max_length=2,choices=ORDERSTATE )

    def __str__(self):
        return self.order


class RefundRequest (models.Model):
    REFUND=(
        ('Pe','PENDING'),
        ('Re','READY'),
        ('Pa','PAID'),
    )
    Order_number  =  models.ForeignKey ( Order,on_delete=models.CASCADE )
    refundtime  =  models.DateTimeField ( auto_now_add=True )
    refundprice  =  models.PositiveIntegerField (  )
    status  =  models.CharField ( max_length=2,choices=REFUND )

    def __str__(self):
        return self.Order_number


class Cart (models.Model):     
    tour  =  models.ForeignKey ( Tour,on_delete=models.CASCADE,blank=True,null=True )
    transport  =  models.ForeignKey ( Transport,on_delete=models.CASCADE,blank=True,null=True )
    room  =  models.ForeignKey ( Room,on_delete=models.CASCADE,blank=True,null=True )
    adult = models.PositiveIntegerField(  )
    child = models.PositiveIntegerField(blank=True,null=True)
    baby = models.PositiveIntegerField(blank=True,null=True)
    user  =  models.ForeignKey ( CustomUser,on_delete=models.CASCADE )


class Order_User_Rel (models.Model):
    order = models.ManyToManyField( Order,related_name='order_rel'  )
    traveler = models.ManyToManyField (CustomUser,related_name='user_rel')
