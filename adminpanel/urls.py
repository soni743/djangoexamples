from django.shortcuts import HttpResponse
from django.urls import path
def test(req):
    return HttpResponse('ok')
urlpatterns = [
#    path("",test),
]