from django.shortcuts import render,redirect,get_object_or_404
from Home.models import *
from .models import *

def tourbooking(request,tourid):
    if request.method == 'POST':
        pass
    else:
        tour = Tour.objects.get(id=tourid)
        user = request.user
        cart = Cart(tour=Tour.objects.get(id=tourid), adult=1, child=0, baby=0, user=CustomUser(id=request.user.id))
        cart.save()
        cur = cart_User_Rel(cart=cart, traveler=CustomUser(id=request.user.id))
        cur.save()
        traveler = cart_User_Rel.objects.filter(cart_id=cart.id)

    context = {'tour':tour, 'user':user, 'cur':cur, 'cart':cart, 'traveler':traveler}
    return (render(request,'Cart/tourBooking.html', context))



def travelerRemove(request,cartid,unicid):
    cur = cart_User_Rel.objects.get(cart_id=cartid, traveler_unicid=unicid)
    print(cur)
    cur.delete()
    return  redirect('Cart:tourBooking')