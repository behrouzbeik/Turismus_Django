from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='Blog'
urlpatterns = [
    path('bloglist/',views.bloglist,name='bloglist'),
    path('blogdetail/<int:articleid>/', views.blogdetail, name='blogdetail')
]