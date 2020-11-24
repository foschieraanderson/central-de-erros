from django.contrib import admin

from .models import Log

class LogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'level', 'origin', 'created_at', 'archived']

admin.site.register(Log, LogAdmin)
