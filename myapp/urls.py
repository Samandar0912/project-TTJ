from django.urls import path
from .views import index, logout_user, login_user, mainIndex, mainProfile, mainStudents

app_name='main' #=> asosiy app

urlpatterns = [
    path("", index, name="index"),
    path("login", login_user, name="loginAdmin"),
    path("logout_user", logout_user, name="logout"),
    path("main", mainIndex, name="mainIndex"),
    path("profile", mainProfile, name="mainProfile"),
    path("students", mainStudents, name="students"),
    
    
]
