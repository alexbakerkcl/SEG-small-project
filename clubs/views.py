from django.shortcuts import redirect,render
from .forms import LogInForm,SignupForm


def feed(request):
    return render(request, 'feed.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})

def login(request):
    form = LogInForm()
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect(request, 'home')
