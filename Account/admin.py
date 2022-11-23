from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import *

# Register your models here.

# @admin.register(CustomUser)
class CustomeUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'mobile', 'image', 'usertype', 
                    'firstname', 'lastname', 'unicid',
                    'birthday', 'gender', 'status', 'city')
    list_editable = ('usertype','image', 'city')


class WaletAdmin(admin.ModelAdmin):
    pass

class ScoreAdmin(admin.ModelAdmin):
    pass

class Bank_depositAdmin(admin.ModelAdmin):
    pass

class UserscoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, CustomeUserAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Bank_deposit, Bank_depositAdmin)
admin.site.register(Userscore, UserscoreAdmin)