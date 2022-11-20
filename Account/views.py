from django.shortcuts import redirect, render, reverse
from .models import CustomUser
from django.core.mail import EmailMessage
from django.views import View
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate,login,logout
# from six import text_type

# Create your views here.
class RegisterEmail(View):
    def get(self,request,uidb64,token):
        id = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(id=id)
        if user and email_generator.check_token(user,token):
            user.is_active = True
            user.save()
            return redirect('Home:index')


class EmailToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: CustomUser, timestamp: int) -> str:
        return super()._make_hash_value(user, timestamp)

email_generator = EmailToken()




# Gmail-Mail verify:  oluhyynihheyifma
def user_register(request):
    if request.method == 'POST':
        data = request.POST
        if data['pass'] == data['repeat']:
            status = 'success'

            user = CustomUser.objects.create_user(unicid=data['cid'], email=data['email'], 
                                                    username=data['email'], 
                                                    password=data['pass'])

            user.is_active = False
            user.save()
            domain = get_current_site(request).domain
            uidb64 = urlsafe_base64_encode(force_bytes(user.id))

            url = reverse('Account:active',kwargs={'uidb64':uidb64, 
                                                    'token':email_generator.make_token(user)})

            links = 'http://' + domain + url

            email = EmailMessage(
                'active user',
                links,
                'beik.behrouz@gmail.com',
                [data['email']]
            )

            email.send(fail_silently=False)
            # messages.warning(request,'karbar mohtaram lotfan jahat faalsazi b email khod morajee namei','warning')
            return redirect('Home:index')
        else:
            pass
    else:
        return render(request, 'Account/signup.html')

    # domain = get_current_site(request).domain
    # uidb64 = urlsafe_base64_encode(force_bytes(user.id))
    # url = reverse('accounts:active',kwargs={'uidb64':uidb64,'token':email_generator.make_token(user)})
    # links = 'http://' + domain + url
    # email = EmailMessage(
    #     'active user',
    #     links,
    #     'test<paneldjango@gmail.com>',
    #     [data['email']]
    # )
    # email.send(fail_silently=False)
    # messages.warning(request,'karbar mohtaram lotfan jahat faalsazi b email khod morajee namei','warning')


def user_logout(request):
    logout(request)
    # messages.success(request,'با موفقیت انجام شد','warning')
    return redirect('Home:index')


def user_login(request):

    if request.method == 'POST':
        data = request.POST
    # if form.is_valid():
        # data = form.cleaned_data
        # remember = data['remember']
        user = authenticate(request, email=data['email'], password=data['pass'])
        if user is not None:
            print("user is authenticated")    
            login(request, user)
        else:
            print("user is not authenticated")
        # if user is not None:
            
            # if not remember:
            #     request.session.set_expiry(0)
            # else:
            #     request.session.set_expiry(10000)
            # messages.success(request,'welcome to site','primary')
        return redirect('Home:index')
        # else:
        #     messages.success(request,'user or password wrong ','danger')
    else:
        pass
    # return render(request,'accounts/login.html',{'form':form})
