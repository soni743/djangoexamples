from django.urls import path
from .views import *

urlpatterns = [
    path('viewcontact', ContactUs, name='viewcontactus'),
    path('delcontacts/<str:contactid>/',DeleteContacts,name='deletecontacts')
]