from .views import *

# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
from django.urls import path
from trail import views
# router.register(r'', listViewSet, basename = "list_trails")
# router.register('search_trail', search_trail, basename = "keyword-search")
urlpatterns=[
    path('search_trail', views.search_trail, name='search_trail'),
    path('insert_schedule', views.insert_schedule, name='insert_schedule'),
    path('to_insert_schedule', views.to_insert_schedule, name='to_insert_schedule'),
    path('to_update_schedule', views.to_update_schedule, name='to_update_schedule'),
    path('to_schedule', views.to_schedule, name='to_schedule'),
    path('delete_schedule', views.delete_schedule, name='delete_schedule'),
    path('update_schedule', views.update_schedule, name='update_schedule'),
]
