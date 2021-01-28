from django.shortcuts import render

# Create your views here.
def ContactUs(req):
    context={
        'name' : 'satyesh soni'
    }
    return render(req, 'Viewcontacts.html',context)
