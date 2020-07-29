from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
	# return render(request, "index.html")
	return HttpResponse("Hello there")

def detail(request, id):
	# return render(request, "index.html")
	return HttpResponse("Hello there "+str(id))
