from django.urls import path
from .views import *
urlpatterns = [
   path("",test),
   path("paramfun/<str:pk>/<str:sk>",ParamFunction),
   path("home/",HomePage, name='homepage'),
   path("about/",Aboutus, name='aboutuspage'),
   path("products/",Products, name='productpage'),
   path("contact/",Contacts, name='contactpage')
]