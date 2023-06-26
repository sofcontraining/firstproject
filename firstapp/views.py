from django.shortcuts import render, HttpResponse, redirect
from .forms import MemberForm
from .models import Member, Course
# Create your views here.

def home(request):
    # return HttpResponse("Hello my first page")
    return render(request,'home.html')

def about(request):
    # return HttpResponse("This is my contact page")
    return render(request,'about.html')

def courses(request):
    allCourse = Course.objects.all()
    context = {'allCourse':allCourse}
    return render(request,'courses.html', context)

def contact(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            contact = request.POST['contact']
            data = {'fname':fname, 'lname':lname, 'email':email, 'contact':contact}
            return render(request,'contact.html',data)
        return redirect('home')
    return render(request,'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')