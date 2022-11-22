from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'mobile', 'email', 'usertype', 
                    'firstname', 'lastname', 'unicid',
                    'birthday', 'gender', 'status',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'mobile', 'email', 'usertype', 
                    'firstname', 'lastname', 'unicid',
                    'birthday', 'gender', 'status',)