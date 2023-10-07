
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User_Detail

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


def home(request):
    user_list = User_Detail.objects.all()
    return render(request, 'home.html', {'user_list': user_list})