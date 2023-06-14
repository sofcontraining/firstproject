from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello my first page")
    return render(request,'home.html')

def about(request):
    # return HttpResponse("This is my contact page")
    return render(request,'about.html')

def services(request):
    # return HttpResponse("This is my contact page")
    return render(request,'services.html')

def contact(request):
    # return HttpResponse("This is my contact page")
    return render(request,'contact.html')