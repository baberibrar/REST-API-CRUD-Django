from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    employee_salary = models.IntegerField()
    employee_age = models.IntegerField()

    def __str__(self):
        return self.employee_name