"""system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clubs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('feed/', views.feed, name = 'feed'),
    path('follow_toggle/<int:user_id>', views.follow_toggle, name='follow_toggle'),
    path('signup/', views.signup, name ='signup'),
    path('login/', views.user_login, name ='login'),
    path('log_out/', views.log_out, name ='log_out'),
    path('new_post/', views.new_post, name='new_post'),
    path('users/', views.user_list, name='user_list'),
    path('user/<int:user_id>', views.show_user, name='show_user'),
]
