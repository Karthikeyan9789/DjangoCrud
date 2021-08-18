from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Employee
from . forms import EmployeeForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"EmployeeApp/home.html")

def list_employees(request):
    # Django ORM
    employees = Employee.objects.all()
    context = {
        "employees": employees,
        "hello":"Its not hello"
    }
    return render(request,"EmployeeApp/employee_list.html",context)


def add_employee(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            messages.success(request,f"Successfully added Employee {employee.name}")
            return redirect('list_employees')
    context = {
        "form":form
    }
    return render(request,"EmployeeApp/employee_form.html",context)


def update_employee(request,id=None):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            employee = form.save()
            messages.success(request,f"Successfully updated Employee {employee.name}")
            return redirect('list_employees')
    context = {
        "form":form
    }
    return render(request,"EmployeeApp/employee_form.html",context)


def delete_employee(request,id=None):
    employee = Employee.objects.get(id=id)
    employeename = employee.name
    employee.delete()
    messages.success(request,f"Successfully deleted Employee {employee}")
    return redirect('list_employees')
