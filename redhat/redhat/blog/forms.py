from django import forms

class UserForm(forms.Form):
	name = forms.CharField(max_length = 30)
	phone = forms.CharField(max_length = 30)
	email = forms.EmailField()
