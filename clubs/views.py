from django.shortcuts import render
from .forms import LogInForm,SignupForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})

def login(request):
    form = LogInForm()
    return render(request, 'login.html',{'form':form})
