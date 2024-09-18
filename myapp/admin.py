from django.contrib import admin
from .models import CategoryFacultet, CategoryYunalish, Talaba

# Register your models here.

admin.site.register(Talaba)
admin.site.register(CategoryYunalish)
admin.site.register(CategoryFacultet)