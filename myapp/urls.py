from django.urls import path
from .views import index, users, students, tulov, profile


urlpatterns = [
    path('',index,name='index'),
    path('users/',users,name='users'),
    path('students/',students,name='students'),
    path('tolovlar/',tulov,name='tulov'),
    path('profile/',profile,name='profile'),
    


]
