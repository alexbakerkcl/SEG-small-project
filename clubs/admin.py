from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name','last_name','username','email','bio','statement','is_active'
    ]
