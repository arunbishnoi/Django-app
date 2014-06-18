from django.db import models
from django.forms import ModelForm
		
# Create your models here.
class Subject(models.Model):
    sub1 = models.CharField(max_length=20)
    sub2 = models.CharField(max_length=20)
    sub3 = models.CharField(max_length=20)

class Student_details(models.Model):
    name = models.CharField(max_length=30)
    roll_no = models.CharField(max_length=30)
    email = models.EmailField()
    math = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    total = models.IntegerField()
    def __unicode__(self):
    	return self.name
class Report(ModelForm):
    class Meta:
    	model = Student_details
    	exclude = ['total']
