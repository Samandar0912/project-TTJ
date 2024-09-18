from django.contrib import admin
from .models import CustomUser
from .forms import UserCreationForm

class CustomUserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserCreationForm
    model = CustomUser
    list_display = ['username', 'email']

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            kwargs['form'] = self.add_form
        return super().get_form(request, obj, **kwargs)

admin.site.register(CustomUser, CustomUserAdmin)
