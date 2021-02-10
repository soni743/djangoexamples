from django.shortcuts import render, redirect
from myapp.models import Contact
from django.contrib import messages
# Create your views here.
def ContactUs(req):
    form = Contact.objects.all()

    context={
        'forms' : form
    }
    return render(req, 'Viewcontacts.html',context)

def DeleteContacts(req,contactid):
    data = Contact.objects.get(pk = contactid)
    data.delete()
    messages.success(req,'Contact is Deleted')
    return redirect('viewcontactus')