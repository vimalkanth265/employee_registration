from django import forms
from django.db.models import fields
from .models import Employee
from django.forms import ModelForm

class employeeform(forms.ModelForm):

    class Meta:
        model=Employee
        fields='__all__'

    def __init__(self, *args,**kwargs) :
        super(employeeform,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label ='select'
        self.fields['emp_code'].required =False