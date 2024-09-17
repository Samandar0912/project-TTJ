from django.urls import path
from .views import index, users, students, tulov, main, logout_user, userlogin, profiles, adminIndex

app_name = 'main' #=> asosiy app

urlpatterns = [
    path('',index,name='index'),
    path('',logout_user,name='logout'),
    
    
    path('users/',users,name='users'),
    path('students/',students,name='students'),
    path('tolovlar/',tulov,name='tulov'),
    path('profile/',main,name='main'),
    
    
    path('user-login/',userlogin,name='userlogin'),
    path('admin-profiles/',profiles,name='profiles'),
    path('admin-page/',adminIndex,name='adminIndex'),



]
