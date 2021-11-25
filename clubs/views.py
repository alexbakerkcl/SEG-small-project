from django.shortcuts import render
from .forms import SignupForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    form = SignupForm()
    return render(request,'signup.html',{'form':form})
