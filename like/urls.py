from .views import *

# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
from django.urls import path
from like import views
# router.register(r'', listViewSet, basename = "list_trails")
# router.register('search_trail', search_trail, basename = "keyword-search")
urlpatterns=[
    path('to_like', views.to_like, name='to_like'),
    path('update_like', views.update_like, name='update_like'),
    path('delete_like', views.delete_like, name='delete_like'),
]
