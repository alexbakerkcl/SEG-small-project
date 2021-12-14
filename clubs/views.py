from django.contrib import messages
from django.shortcuts import redirect,render
from .forms import LogInForm,SignupForm
from django.contrib.auth import authenticate,login

def feed(request):
    return render(request, 'feed.html')

def home(request):
    return render(request, 'home.html')

def user_login(request):
     if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password')
             user = authenticate(username=username, password=password)
             if user is not None:
                  login(request, user)
                  return redirect('feed')
        # Add error messages here
        messages.add_message(request, messages.ERROR, "The password is invaild")
     form = LogInForm()
     return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})



def logout(request):

    return redirect(request, 'home')
