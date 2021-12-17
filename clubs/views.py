from django.contrib import messages
from django.shortcuts import redirect,render
from .forms import LogInForm,SignupForm,PostForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Post, User , Club
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden

@login_required
def feed(request):
    form = PostForm()
    current_user = request.user
    authors = list(current_user.followees.all()) + [current_user]
    posts = Post.objects.filter(author__in=authors)
    return render(request, 'feed.html', {'form': form, 'user': current_user, 'posts': posts})

@login_required
def follow_toggle(request, user_id):
    current_user = request.user
    try:
        followee = User.objects.get(id=user_id)
        current_user.toggle_follow(followee)
    except ObjectDoesNotExist:
        return redirect('user_list')
    else:
        return redirect('show_user', user_id=user_id)

def user_login(request):
     if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password')
             user = authenticate(username=username, password=password)
             if user is not None:
                  login(request, user)
                  redirect_url = request.POST.get('next') or 'feed'
                  return redirect(redirect_url)
        messages.add_message(request, messages.ERROR, "The password is invaild")
     form = LogInForm()
     next = request.GET.get('next') or ''
     return render(request, 'login.html', {'form': form, 'next': next})

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

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def show_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        posts = Post.objects.filter(author=user)
        following = request.user.is_following(user)
        followable = (request.user != user)
    except ObjectDoesNotExist:
        return redirect('user_list')
    else:
        return render(request, 'show_user.html',
            {'user': user,
             'posts': posts,
             'following': following,
             'followable': followable}
        )

def club_list(request):
    clubs = club.objects.all()
    return render(request, 'club_list.html', {'clubs': clubs})
