from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='Account'
urlpatterns = [
    path('register/',views.user_register,name='register'),
    path('active/<uidb64>/<token>/',views.RegisterEmail.as_view(),name='active'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    # path('profile/',views.user_profile,name='profile'),
    # path('update/',views.user_update,name='update'),
    # path('change/',views.change_password,name='change'),
    # path('login_phone/',views.phone,name='phone'),
    # path('verify/',views.verify,name='verify'),
    # path('reset/',views.ResetPassword.as_view(),name='reset'),
    # path('reset/done/',views.DonePassword.as_view(),name='reset_done'),
    # path('confirm/<uidb64>/<token>',views.ConfirmPassword.as_view(),name='password_reset_confirm'),
    # path('confirm/done/',views.Complete.as_view(),name='compelet'),
    # path('favourite/',views.favourite,name='favourite'),
    # path('history/',views.history,name='history'),
    # path('view/',views.product_view,name='product_view'),
]