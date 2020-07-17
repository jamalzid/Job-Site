from django.contrib import admin
from .models import *
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']


admin.site.register(Job,JobAdmin)


class ApplyAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'apply_at']


admin.site.register(Apply, ApplyAdmin)
