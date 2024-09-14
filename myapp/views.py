from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')


def tulov(request):
    return render(request,'tulov.html')


def profile(request):
    return render(request,'profile.html')


def users(request):
    return render(request,'users.html')


def students(request):
    return render(request,'students.html')
