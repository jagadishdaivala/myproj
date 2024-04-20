from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def v1(request):
    return HttpResponse("<h1>this is v1</h1>")

def v2(request):
    return HttpResponse("<h1>this is v2</h1>")

def home(request):
    return render(request,'home.html')

def nav(request):
    return render(request,'nav.html')
