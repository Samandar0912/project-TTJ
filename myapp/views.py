from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import categoryFacultet, categoryYunalish, talabalar


# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return redirect('index')
    return render(request, 'index.html')


def logout_user(request):
    logout(request)
    return redirect('index')
    

def tulov(request):
    return render(request,'tulov.html')


def main(request):
    students = talabalar.objects.all()
    context = {
        'students': students
    }
    return render(request, 'main.html', context)


def users(request):
    return render(request,'users.html')


def students(request):
    return render(request,'students.html')


def userlogin(request):
    return render(request,'userAdmin/login.html')


def profiles(request):
    return render(request,'userAdmin/profile.html')


def adminIndex(request):
    return render(request,'userAdmin/index.html')