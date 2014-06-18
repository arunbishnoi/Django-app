from django.shortcuts import render
from django.http import *
from django import forms
from result.models import *
from django.http import HttpResponseRedirect
#from result.forms import *

    
def marks(request):
    if request.method=='POST': 
        form = Report(request.POST) 
        if form.is_valid(): 
			cd=form.cleaned_data
			name = cd['name']
			roll_no = cd['roll_no']
			email = cd['email']
			math = cd['math']
			physics = cd['physics']
  			chemistry = cd['chemistry']
   			obj = Student_details(name=name, roll_no=roll_no, email=email, math=math, physics=physics, chemistry=chemistry, total=0) 
  			obj.save()
			return HttpResponseRedirect('/display/') 
    else:
        form = Report() # An unbound form
    return render(request, 'front.html', {
        'form': form,
    })

def display(request):
    obj = Student_details.objects.get(id=3)
    math = obj.math
    physics = obj.physics
    chemistry = obj.chemistry
    Total = math + physics + chemistry
    return render(request, 'output.html',  { 'total':Total
           })