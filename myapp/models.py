from django.db import models

# Fakultetlar uchun model
class CategoryFacultet(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Fakultet'
        verbose_name_plural = 'Fakultetlar'


# Yo'nalishlar uchun model
class CategoryYunalish(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Yo'nalish"
        verbose_name_plural = "Yo'nalishlar"


# Talabalar uchun model
class Talaba(models.Model):
    author = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200) 
    photo = models.ImageField(upload_to='Photo/', default='Photo/user.jpg', blank=True, null=True)
    guruh = models.CharField(max_length=10)
    fakultet = models.ForeignKey(CategoryFacultet, on_delete=models.CASCADE)
    yunalish = models.ForeignKey(CategoryYunalish, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"
