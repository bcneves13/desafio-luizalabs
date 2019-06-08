from django.contrib import admin
from .models import Employees
# Register your models here.


@admin.register(Employees)
class ListEmployee(admin.ModelAdmin):
    list_display = ('name', 'email','department')
    list_filter = ('department',)
    search_fields = ('name', 'email', 'department')