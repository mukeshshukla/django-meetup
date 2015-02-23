from django.http import HttpResponse
from django.shortcuts import render
from forms import *
def home(request):
	user_form = UserForm ()
	return render(request, 'home.html', {'form':user_form})
def forms (request):
	st ="%s\n%s\n%s" % (request.GET['name'],request.GET['phone'], request.GET['email']) 
	return HttpResponse(st)

