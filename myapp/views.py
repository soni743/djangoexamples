from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import  *
from .models import  *
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

def PersonFunction(req):
    form = PersonForm()
    formdata = Person.objects.all()
    if req.method == 'POST':
        form = PersonForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            form = PersonForm()
            messages.success(req,'Person Data is Saved!')
    context = {
        'forms' : form,
        'datas' : formdata
    }
    return render(req,'person.html',context)   
def PersonDelete(req,pid):
    data = Person.objects.get(pk=pid)
    data.delete()
    messages.success(req,'Record is Deleted!')
    return redirect('personpage')

def PersonEdit(req,pid):
    data = Person.objects.get(pk=pid)
    form = PersonForm(instance=data)
    formdata = Person.objects.all()
    site = Person.objects.only('img').get(pk=pid)
    print(site)
  
    if req.method == 'POST':
        form = PersonForm(req.POST,req.FILES,instance=data)
        if form.is_valid():
            form.save()
            data=None
            site=None
            form=PersonForm(instance=data)
            messages.success(req,"Record is Updated!")
           
            return redirect('personpage')
    context = {
        'forms' : form,
        'datas' : formdata,
        'imgurl' : site
    }
    return render(req,'person.html',context)
    
def PersonSalary(req):
    form = PersonSalaryForm()
    if req.method == 'POST':
        form = PersonSalaryForm(req.POST)
        if form.is_valid():
            form.save()
            messages.error(req, 'User Salary Saved!')

    context={
        'form' : PersonSalaryForm
    }   
    return render(req,'personsalary.html',context)  

def ContactUs(req):
    form = ContactForm()
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            messages.success(req,'We will Contact You Soon...')

    context ={
        'forms' : form
    }
    return render(req,'contacts.html',context)

