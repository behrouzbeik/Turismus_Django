from django.shortcuts import render,redirect,get_object_or_404
from Home.models import *
from .models import *
from django.http import JsonResponse
from datetime import datetime

def tourbooking(request,tourid):
    if request.method == 'POST':
        pass
    else:
        tour = Tour.objects.get(id=tourid)
        user = request.user
        cart = addFirstTraveler(tour, request.user)
        # cart = Cart(tour=Tour.objects.get(id=tourid), adult=1, child=0, baby=0, user=CustomUser(id=request.user.id))
        # cart.save()
        # cur = cart_User_Rel(cart=cart, traveler=CustomUser(id=request.user.id))
        # cur.save()
        travelers = cart_User_Rel.objects.filter(cart_id=cart.id)
    context = {'tour':tour, 'user':user, 'travelers':travelers, 'cart':cart}
    return (render(request,'Cart/tourBooking.html', context))

def addFirstTraveler(tour, user):
    try:
        cart = Cart.objects.get(tour=tour, user=user)
    except:
        cart=None
    if cart is None:
        cart = Cart(tour=tour, adult=1, child=0, baby=0, user=user)
        cart.save()
        cur = cart_User_Rel(cart=cart, traveler=user)
        cur.save()
    
    return cart

# def cart_show(request, cartid):
#     travelers = cart_User_Rel.objects.filter(cart_id=cartid)
#     response = {'travelers':travelers,}
#     return JsonResponse(response)


def travelerRemove(request,cartid,unicid):
    url = request.META.get('HTTP_REFERER')
    cur = cart_User_Rel.objects.get(cart_id=cartid,traveler=CustomUser.objects.get(unicid=unicid)) #(cart_id=cartid, traveler_unicid=unicid)
    cur.delete()
    return  redirect(url)


def travelerAdd(request,cartid):
    url = request.META.get('HTTP_REFERER')
    data = request.POST
    if data['gen']=='M':
        gender=True
    elif data['gen']=='F':
        gender=False

    # user={}
    # print(CustomUser.objects.get(unicid=data['uid']).exists())
    # try:
    if CustomUser.objects.filter(unicid=data['uid']).exists():
        user = CustomUser.objects.get(unicid=data['uid'])
        cur = cart_User_Rel(cart=Cart.objects.get(id=cartid), traveler=user)
        cur.save()
    else:
        user = CustomUser.objects.create_user(unicid=data['uid'], email=data['uid']+'none@none.com', 
                                                    username=data['uid']+'none@none.com', password='datapass',
                                                    gender=gender, firstname=data['fname'], usertype='Tr',
                                                    lastname=data['lname'], birthday=data['birthday'])
                                                    # gender=data['gen'], firstname=data['fname'],
                                                    # lastname=data['lname'], birthday=data['birthday']
        user.is_active = False
        user.save()
        cur = cart_User_Rel(cart=Cart.objects.get(id=cartid), traveler=user)
        cur.save()
    
    return  redirect(url)


def payment(request,cartid):
    cart = Cart.objects.get(id=cartid)
    print(str(cartid))
    order = Order(
        orderno= str(cartid),
        ordertime=datetime.now(),
        tour=cart.tour,
        transport=cart.transport,
        room =cart.room,
        adult=cart.adult,
        child=cart.child,
        baby=cart.baby,
        user=cart.user
    )
    order.save()
    cur = cart_User_Rel.objects.filter(cart=Cart.objects.get(id=cartid))
    for c in cur:
        our = Order_User_Rel(
            order=order, 
            traveler=c.traveler
        )
        our.save()
        c.delete()

    cart.delete()
    return redirect('Home:index')