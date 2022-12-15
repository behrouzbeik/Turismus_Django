from django.contrib import admin

from .models import *

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    pass

class OrderStatusAdmin(admin.ModelAdmin):
    pass

class RefundRequestAdmin(admin.ModelAdmin):
    pass

class CartAdmin(admin.ModelAdmin):
    pass

class Order_User_RelAdmin(admin.ModelAdmin):
    pass

class Cart_User_RelAdmin(admin.ModelAdmin):
    pass



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(RefundRequest, RefundRequestAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order_User_Rel, Order_User_RelAdmin)
admin.site.register(cart_User_Rel, Cart_User_RelAdmin)