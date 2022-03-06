from re import M
from django import forms
from .models import Student

class StudentModelForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = (
			'first_name',
   			'last_name',
    		'identityNumber',
    		'address',
    		'department',
			'representative'
		)
