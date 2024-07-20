from django.contrib import admin

# Register your models here.
from .models import Todo

class ListTodo(admin.ModelAdmin):
    search_fields = ['text']
    list_filter = ['text', 'date']


admin.site.register(Todo, ListTodo)