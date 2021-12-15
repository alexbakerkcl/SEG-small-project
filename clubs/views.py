from django.contrib import messages
from django.shortcuts import redirect,render
from .forms import LogInForm,SignupForm,PostForm
from django.contrib.auth import authenticate,login,logout
from .models import Post, User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden

def feed(request):
    form = PostForm()
    return render(request, 'feed.html',{'form': form})

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

def log_out(request):
   logout(request)
   return redirect('home')

def home(request):
    return render(request, 'home.html')

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

def new_post(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            current_user = request.user
            form = PostForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data.get('text')
                post = Post.objects.create(author=current_user, text=text)
                return redirect('feed')
            else:
                return render(request, 'feed.html', {'form': form})
        else:
            return redirect('login')
    else:
        return HttpResponseForbidden()

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def show_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return redirect('user_list')
    else:
        return render(request, 'show_user.html', {'user': user})
