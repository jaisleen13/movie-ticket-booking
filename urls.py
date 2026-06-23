"""
URL configuration for movie_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movieapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('foot',views.foot,name="foot"),
    path('contact',views.contact,name="contact"),
    path('REGG',views.REGG,name="REGG"),
    path('PASS',views.PASS ,name="pass"),
    path('login',views.login,name="login"),
    path('header',views.header,name="header"),
    path('sidebar',views.sidebar,name="sidebar"),
    path('changepassword',views.changepassword,name="changepassword"),
    path('logout',views.logout,name="logout"),
    path('editpro',views.editpro,name="editpro"),
    path('forgetpass',views.forgetpass,name="forgetpass"),
    path('myprofile',views.myprofile,name='myprofile'),
    # path('forgetpass',views.forgetpass),
    path('seats',views.boo_seats,name="seats"),
    path('allmovies',views.allmovies,name="allmovies"),
    path('payment',views.payment,name="payment"),
    path('booked',views.booked,name='booked'),

    path('allmovies1',views.allmovies1,name="allmovies1"),
    path('moviedetail/<int:id>',views.moviedetail,name="moviedetail"),
    path('index',views.index,name="index"),
    path('enter_otp',views.enter_otp,name="enter_otp"),
    path('trailer',views.trailer,name="trailer"),
        path('bookeddetails',views.bookeddetails,name="bookeddetails"),


    
    
    
 
]
urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
