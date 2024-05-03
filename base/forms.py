from django import forms
from .models import Employees

class EmployeeForm(forms.Form):
    #charfield
    emp_name = forms.CharField(
        max_length=50,
        label = "Employee Name",
        required = True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            
        }),
        initial="Name"   
    )
    #DateTimeField
    set_joining_date = forms.DateTimeField(
        widget=forms.DateInput(attrs={'class': 'form-control',
                                      'type':'datetime-local'
                                      }),
        initial=date.today()
    )