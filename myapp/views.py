from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request,'index.html')


def logout_user(request):
    logout(request)
    return redirect('main:index')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:mainIndex')
        else:
            return redirect('main:loginAdmin')     
    return render(request,'usersAdmin/login.html')




def mainIndex(request):
    return render(request,'usersAdmin/index.html')


def mainProfile(request):
    return render(request,'usersAdmin/profile.html')


def mainStudents(request):
    return render(request,'usersAdmin/users.html')


