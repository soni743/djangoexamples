from django import forms
from django.forms import ModelForm
from .models import *

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    

class PersonSalaryForm(ModelForm):
    class Meta:
        model = PersonSalary
        fields='__all__'     
        widgets={
            'userperson': forms.Select(attrs={'class':'form-control common inp_s1'}),
            'salary':forms.NumberInput(attrs={'class':'form-control common inp_s2', 'placeholder':'user'}),
        }   

        
