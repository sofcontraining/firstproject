from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello my first page")
    return render(request,'home.html')

def contact(request):
    # return HttpResponse("This is my contact page")
    return render(request,'contact.html')