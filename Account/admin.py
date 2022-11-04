from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#from .forms import *
from .models import *

# Register your models here.

@admin.register(CustomUser)
class CustomeUserAdmin(UserAdmin):
    model = CustomUser
#    add_form = CustomeUserCreationForm
#    form = CustomeUserChangeForm
    list_display = ('email' , 'username' ,)


class WaletAdmin(admin.ModelAdmin):
    pass

class ScoreAdmin(admin.ModelAdmin):
    pass

class Bank_depositAdmin(admin.ModelAdmin):
    pass

class UserscoreAdmin(admin.ModelAdmin):
    pass




admin.site.register(Score, ScoreAdmin)
admin.site.register(Bank_deposit, Bank_depositAdmin)
admin.site.register(Userscore, UserscoreAdmin)
