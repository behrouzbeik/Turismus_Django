from django.urls import path

from . import views


app_name = 'Home'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('About/', views.about, name='about'),
    path('Services/', views.services, name='services'),
    path('Package/', views.package, name='package'),
    path('Residence/', views.residence, name='residence'),
    path('Transport/', views.transport, name='transport'),
    path('ServicesLoader/', views.servicesLoader, name ='servicesLoader')

    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]