from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello my first page")

def contact(request):
    return HttpResponse("This is my contact page")