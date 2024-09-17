from django.contrib import admin
from .models import categoryFacultet, categoryYunalish, talabalar

# Register your models here.

admin.site.register(talabalar)
admin.site.register(categoryYunalish)
admin.site.register(categoryFacultet)