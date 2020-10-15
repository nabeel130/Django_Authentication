from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    count = User.objects.count()
    context = {
        'count' : count
    }
    return render(request, 'auth_app/home.html' , context)

def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    
    context = {
        'form' : form
    }
    return render(request, 'auth_app/signup.html' , context)
    
    