from django.shortcuts import redirect, render, reverse
from .models import CustomUser
from django.core.mail import EmailMessage
from django.views import View
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from six import text_type

# Create your views here.
class RegisterEmail(View):
    def get(self,request):
        id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=id)
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
    # url = request.META.get('HTTP_REFERER')
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

