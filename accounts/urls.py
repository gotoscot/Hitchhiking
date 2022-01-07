from django.urls import path
from accounts import views

urlpatterns = [
    # path('', views.accounts, name='accounts'),
    path('login', views.login, name='login'),
    path('logging', views.logging, name='logging'),
    path('register', views.register, name='register'),
    path('logout',views.logout,name='logout')
]