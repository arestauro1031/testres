from django.shortcuts import render
from .models import Employees
from datetime import datetime
from .forms import EmployeeForm
from django.http import HttpResponse


def home(request):
    employee = Employees.objects.all()
    
    context = {'employee':employee}
    return render(request, 'base/home.html', context)

def employee(request):
    if request.method == 'POST':
        
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['emp_name']
            join_date = form.cleaned_data['set_join_date']
            emp = Employees.objects.create(
                emp_name = name,
                set_joining_date = join_date
            )
            emp.save()
            return HttpResponse("The data is saved in the datbase")
        form = EmployeeForm()
    return render(request, 'base/home.html', {'form':  form})
