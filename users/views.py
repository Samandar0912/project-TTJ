from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False  # Bu foydalanuvchi admin panelga kira olmaydi
            user.is_superuser = False  # Superuser emas
            user.save()
            login(request, user)  # Yangi foydalanuvchini tizimga kiritish
            return redirect('home')  # Bosh sahifaga yo'naltirish
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
