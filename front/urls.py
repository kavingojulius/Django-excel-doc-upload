from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name='index'),
    path('sign', Sign, name='signup'),
    path('login', Login, name='login'),
    path('home', Home, name='home')
]