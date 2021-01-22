from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import  *
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
    context = {
        'title' :'AboutUs',
        'About_txt' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam minus aliquid, itaque illum assumenda repellendus dolorem, dolore numquam totam saepe, porro delectus, libero enim odio quo. Explicabo ex sapiente sit eligendi, facere voluptatum! Quia vero rerum sunt porro architecto corrupti eaque corporis eum, enim soluta, perferendis dignissimos, repellendus, beatae laboriosam.',
        'About_img' : 'about-us.png'
    }
    return render(req,"aboutus.html", context)  

def Products(req):
    return render(req,'products.html',{'productname':'C Book'})      

def Contacts(req):
    return render(req,'contactus.html',{'email':'soni7431@gmail.com'})  

def Person(req):
    form = PersonForm()
    if req.method == 'POST':
        form = PersonForm(req.POST)
        if form.is_valid():
            form.save()
            print('Saved')

    context = {
        'form' : PersonForm
    }
    return render(req,'person.html',context)   

def PersonSalary(req):
    form = PersonSalaryForm()
    if req.method == 'POST':
        form = PersonSalaryForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'User Salary Saved!')

    context={
        'form' : PersonSalaryForm
    }   
    return render(req,'personsalary.html',context)   