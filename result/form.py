from django import forms
from result.models  import Subject
 
class Student_details(forms.Form):
    name = forms.CharField(max_length=30)
    roll_no = forms.CharField(max_length=30)
    email = forms.EmailField()
    math = forms.IntegerField(max_value=100)
    physics = forms.IntegerField(max_value=100)
    chemistry = forms.IntegerField(max_value=100)
    