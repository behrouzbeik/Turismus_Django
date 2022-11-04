from django.shortcuts import render
from .models import MyCompanyInfo

# Create your views here.

def index(request):
    myCompanyInfo = MyCompanyInfo.objects.get(company_name='Behrouz Travel')
    context = {
        'title': myCompanyInfo.company_name,
        'email': myCompanyInfo.email,
        'phone': myCompanyInfo.phon_number,
        'facebook': myCompanyInfo.facebook,
        'twiter': myCompanyInfo.twiter,
        'linkedin': myCompanyInfo.linkedin,
        'insta': myCompanyInfo.insta,
        'utube': myCompanyInfo.utube,
        'Lang': 'De',
        'SignIn': 'Sign In',
        'SignOut': 'SignOut',
        'SignUp': 'SignUp',
        'Search': 'Search',
        'Services': 'Services',
        'Menu': 'Menu',
    }
    return (render(request,'Home/index.html', context))

def about(request):
    return (render(request,'Home/about.html'))

def services(request):
    return (render(request,'Home/service.html'))

def package(request):
    return (render(request,'Home/package.html'))