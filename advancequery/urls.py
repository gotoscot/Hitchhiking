"""hitchhiking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from . import views
from .views import *
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('UserRankingmodel', UserRanking, basename= 'UserRanking')
# router.register('Recommendlistmodel', UserRecommend)

urlpatterns = [
    # path('', include(router.urls)),
    path('Ranking_table', views.get_ranking),
    path('Recommend_table', views.get_recommend),
    path('buddy_restaurant_recommend', buddy_restaurant_recommend),
]


