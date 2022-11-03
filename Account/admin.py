from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#from .forms import *
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomeUserAdmin(UserAdmin):
    model = CustomUser
#    add_form = CustomeUserCreationForm
#    form = CustomeUserChangeForm
    list_display = ('email' , 'username' ,)