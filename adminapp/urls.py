from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactUs, name='contactus'),
]