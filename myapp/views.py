from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(req):
    return HttpResponse("Hello World!")

def ParamFunction(req,sk,pk):
    context={
        'name' : pk,
        'contact': sk
    }    
    return render(req,'param.html',context)

def HomePage(req):
    return render(req,"index.html", {'name':'smsoni infosoft'})    

def Aboutus(req):
    return render(req,"aboutus.html", {'contact':8128992581})  

def Products(req):
    return render(req,'products.html',{'productname':'C Book'})      

def Contacts(req):
    return render(req,'contactus.html',{'email':'soni7431@gmail.com'})    