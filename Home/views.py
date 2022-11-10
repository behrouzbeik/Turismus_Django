from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from .filters import *

# Create your views here.

def index(request):
    # myCompanyInfo = MyCompanyInfo.objects.get(company_name='Behrouz Travel')
    cities = City.objects.filter(home_page_display=True).order_by('-id')[:6]
    destinations = City.objects.all()
    tour = Tour.objects.filter(home_page_display=True).order_by('-id')[:6]
    context = {
        # 'title': myCompanyInfo.company_name,
        # 'email': myCompanyInfo.email,
        # 'phone': myCompanyInfo.phon_number,
        # 'facebook': myCompanyInfo.facebook,
        # 'twiter': myCompanyInfo.twiter,
        # 'linkedin': myCompanyInfo.linkedin,
        # 'insta': myCompanyInfo.insta,
        # 'utube': myCompanyInfo.utube,
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
    return (render(request,'Home/services.html'))#service

def package(request):
    tour = Tour.objects.all().order_by('-id')
    context = {
        # 'title': myCompanyInfo.company_name,
        # 'email': myCompanyInfo.email,
        # 'phone': myCompanyInfo.phon_number,
        # 'facebook': myCompanyInfo.facebook,
        # 'twiter': myCompanyInfo.twiter,
        # 'linkedin': myCompanyInfo.linkedin,
        # 'insta': myCompanyInfo.insta,
        # 'utube': myCompanyInfo.utube,
        # 'destinations': destinations,
        'SignIn': 'Sign In',
        'SignOut': 'SignOut',
        'SignUp': 'SignUp',
        'Search': 'Search',
        'Services': 'Services',
        'Menu': 'Menu',
        'tour':tour,
    }
    return (render(request,'Home/package.html', context))

def residence(request):
    url = request.META.get('HTTP_REFERER')
    residence_list= Residence.objects.all().order_by('-id')
    filter = ResidenceFilter(request.GET,queryset=residence_list)
    residence_list = filter.qs
    paginator = Paginator(residence_list,3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        # 'title': myCompanyInfo.company_name,
        # 'email': myCompanyInfo.email,
        # 'phone': myCompanyInfo.phon_number,
        # 'facebook': myCompanyInfo.facebook,
        # 'twiter': myCompanyInfo.twiter,
        # 'linkedin': myCompanyInfo.linkedin,
        # 'insta': myCompanyInfo.insta,
        # 'utube': myCompanyInfo.utube,
        # 'destinations': destinations,
        'SignIn': 'Sign In',
        'SignOut': 'SignOut',
        'SignUp': 'SignUp',
        'Search': 'Search',
        'Services': 'Services',
        'Menu': 'Menu',
        'url':url,
        'residence':page_obj,
        'page_num':page_num,
        'filter':filter,
    }
    return (render(request,'Home/residence.html', context))
