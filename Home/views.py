from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from .filters import *
from .forms import *
from . import urls
from django.shortcuts import redirect, reverse

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
    return (render(request,'Home/service.html'))#service

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
    class counter():
        tour = Tour.objects.all().count()
        airplane = Transport.objects.filter(beginning__type='Pl').count()
        train = Transport.objects.filter(beginning__type='Tr').count()
        bus = Transport.objects.filter(beginning__type='BU').count()
        cruise = Transport.objects.filter(beginning__type='Cr').count()
        residence = Residence.objects.all().count()

    # url = filter. filter_url residence.previous_page_number
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
        'counter':counter,
        'residence':page_obj,
        'page_num':page_num,
        'filter':filter,
    }
    return (render(request,'Home/residence.html', context))


def transport(request):
    class counter():
        tour = Tour.objects.all().count()
        airplane = Transport.objects.filter(beginning__type='Pl').count()
        train = Transport.objects.filter(beginning__type='Tr').count()
        bus = Transport.objects.filter(beginning__type='BU').count()
        cruise = Transport.objects.filter(beginning__type='Cr').count()
        residence = Residence.objects.all().count()

    # url = filter. filter_url residence.previous_page_number
    transport_list= Transport.objects.all().order_by('-id')
    filter = TransportFilter(request.GET,queryset=transport_list)
    transport_list = filter.qs
    paginator = Paginator(transport_list,3)
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
        'counter':counter,
        'transport':page_obj,
        'page_num':page_num,
        'filter':filter,
    }
    return (render(request,'Home/transport.html', context))


def servicesLoader(request):
    data = request.POST
    
    if data['beginning'] == 'NULL':
        beginning = ''
    else:
        beginning = str(City.objects.get(city=data['beginning']).id)

    if data['destination'] == 'NULL':
        destination = ''
    else:
        destination = str(City.objects.get(city=data['destination']).id)
    
    date = data['depart']
    if data['service'] == 'residence' :
        base_url = redirect('Home:residence')
        url = base_url.url + '?city='+destination+'&buyscore=&userscore='
    elif data['service'] == 'plane' :
        base_url = redirect('Home:transport')
        url = base_url.url + '?beginning__city='+beginning+'&distination__city='+destination+'&starttime__date='+str(date)+'&beginning__type=Pl'+'&buyscore=&userscore='
    elif data['service'] == 'train' :
        base_url = redirect('Home:transport')
        url = base_url.url + '?beginning__city='+beginning+'&distination__city='+destination+'&starttime__date='+str(date)+'&beginning__type=Tr'+'&buyscore=&userscore='
    elif data['service'] == 'bus' :
        base_url = redirect('Home:transport')
        url = base_url.url + '?beginning__city='+beginning+'&distination__city='+destination+'&starttime__date='+str(date)+'&beginning__type=Bu'+'&buyscore=&userscore='
    elif data['service'] == 'cruise' :
        base_url = redirect('Home:transport')
        url = base_url.url + '?beginning__city='+beginning+'&distination__city='+destination+'&starttime__date='+str(date)+'&beginning__type=Cr'+'&buyscore=&userscore='
    else :
        pass
        # graid_star=&beginning__city=1&distination__city=3&starttime__date=beginning__type=Tr&buyscore=&userscore=
        # beginning__city=1&distination__city=3&starttime__date=&beginning__type=Tr&buyscore=&userscore=
        # ?graid_star=2&beginning__city=&distination__city=&starttime__date=&buyscore=&userscore=
        # print ('INJA', base_url)
        # query_string =  urlencode({'category': category.id})  # 2 category=42
        # url = '{}'.format(base_url)  # 3 /products/?category=42
    # # elif
    return (redirect(url))
    # return (render(request,'Home/blog.html', {'data':base_url}))
    