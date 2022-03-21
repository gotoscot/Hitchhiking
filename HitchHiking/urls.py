"""HitchHiking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.index, name='index')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('trail/', include('trail.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', include('user.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('user/', include('accounts.urls')),
    path('trail/', include('trail.urls')),
    path('advancequery/', include('advancequery.urls')),
    path('like/', include('like.urls'))
]
