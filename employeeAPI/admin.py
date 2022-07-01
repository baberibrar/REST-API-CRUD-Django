from django.contrib import admin
from .models import Employee
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name',
                    'employee_salary', 'employee_age')
    search_fields = ('employee_name',)
