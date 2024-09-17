from django.db import models
from phonenumber_field.modelfields import PhoneNumberField # type: ignore

# Create your models here.

class categoryFacultet(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Fakultet'
        verbose_name_plural = 'Fakultetlar'


class categoryYunalish(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Yo'nalish"
        verbose_name_plural = "Yo'nalishlar"


class talabalar(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='Photo/', default='Photo/user.jpg', blank=True)
    number = PhoneNumberField(blank=True, help_text="Enter phone number")
    guruh = models.CharField(max_length=10)
    fakultet = models.ForeignKey(categoryFacultet, on_delete=models.CASCADE)
    yunalish = models.ForeignKey(categoryYunalish, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"