"""
URL configuration for ecommerce project.

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
from  CoverCraft.views import *



urlpatterns = [
    path('',index),
    path('cover',cover),
    
    path('about',about),
    path('login',loginpage),
    path('signup',signup),
    path('productcover/<id>',productcover),
    path('success',buy_now),
    path('logout',logout_view),
    path('vieworder',vieworder),
    path('admin/', admin.site.urls),
    path('sendmail',send_simple_email)
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


