from django import forms
from django.forms import ModelForm
from .models import *

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'img': forms.FileInput
        }

    

class PersonSalaryForm(ModelForm):
    class Meta:
        model = PersonSalary
        fields='__all__'     
        widgets={
            'userperson': forms.Select(attrs={'class':'form-control common inp_s1'}),
            'salary':forms.NumberInput(attrs={'class':'form-control common inp_s2', 'placeholder':'user'}),
        }   

#kite 
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets={
                'name' : forms.TextInput(attrs={'class':'form-control','placeholder':' Your Name'}),
                'email' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email'}),
                'purpose':forms.Select(attrs={'class':'form-control','placeholder':'Your Purpose'}),
                'msg':forms.Textarea(attrs={'class':'form-control','placeholder':'Your Message'})
        }

        
