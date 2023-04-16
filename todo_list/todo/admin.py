from django.contrib import admin
from .models import Tasks_todo
# Register your models here.


class Tasks_todoAdmin(admin.ModelAdmin):
    list_display = ('task', 'task_description', 'deadline', 'completed')

# Register your models here.

admin.site.register(Tasks_todo, Tasks_todoAdmin)