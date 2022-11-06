from django.shortcuts import render
from .models import MyCompanyInfo,City,Tour

# Create your views here.

def index(request):
    myCompanyInfo = MyCompanyInfo.objects.get(company_name='Behrouz Travel')
    cities = City.objects.filter(home_page_display=True).order_by('-id')[:6]
    destinations = City.objects.all()
    tour = Tour.objects.filter(home_page_display=True).order_by('-id')[:6]
    context = {
        'title': myCompanyInfo.company_name,
        'email': myCompanyInfo.email,
        'phone': myCompanyInfo.phon_number,
        'facebook': myCompanyInfo.facebook,
        'twiter': myCompanyInfo.twiter,
        'linkedin': myCompanyInfo.linkedin,
        'insta': myCompanyInfo.insta,
        'utube': myCompanyInfo.utube,
        'destinations': destinations,
        'SignIn': 'Sign In',
        'SignOut': 'SignOut',
        'SignUp': 'SignUp',
        'Search': 'Search',
        'Services': 'Services',
        'Menu': 'Menu',
        'cities':cities,
        'tour':tour,
    }
    return (render(request,'Home/index.html', context))

def about(request):
    return (render(request,'Home/about.html'))

def services(request):
    return (render(request,'Home/service.html'))

def package(request):
    return (render(request,'Home/package.html'))