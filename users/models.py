from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField # type: ignore


# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='Photo/', default='Photo/user.jpg', blank=True)
    number = PhoneNumberField(blank=True, help_text="Enter phone number")
    guruh = models.CharField(max_length=10)
    
    
    def __str__(self) -> str:
        return self.username