from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='Cart'
urlpatterns = [
    path('tourBooking/<int:tourid>/',views.tourbooking,name='tourbooking'),
    path('travelerRemove/<int:cartid>/<str:unicid>/',views.travelerRemove,name='travelerRemove'),
    # path('show/',views.cart_show,name='show'),
]