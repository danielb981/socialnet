from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')