from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    employee_code = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name