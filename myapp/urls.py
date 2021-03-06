from django.urls import path
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
   path("",test),
   path("paramfun/<str:pk>/<str:sk>",ParamFunction),
   path("home/",HomePage, name='homepage'),
   path("about/",Aboutus, name='aboutuspage'),
   path("products/",Products, name='productpage'),
   path("contact/",Contacts, name='contactpage'),
   path("person/",PersonFunction, name='personpage'),
   path("personsalary/",PersonSalary, name='personsalarypage'),
   path("persondelete/<str:pid>/",PersonDelete, name='persondeletepage'),
   path("personedit/<str:pid>/",PersonEdit, name='personeditepage'),
   path('contactform/',ContactUs,name='contactus'),
   path('login/',UserLogin,name='loginpage'),
   path('userregistration/',UserRegisterFunction,name='userregisterpage'),
   path('logout/',logoutfunction, name='logout')
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 