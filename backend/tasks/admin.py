from django.contrib import admin
from .models import Task # import our task model to register to admin interface

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'completed', 'created_at')
    list_filter = ('completed', 'priority')
    search_fields = ('title', 'description')
    readonly_fields = ('id', 'created_at', 'updated_at')