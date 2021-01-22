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

        
