from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'created_at', 'is_staff', 'is_superuser']

admin.site.register(User, UserAdmin)