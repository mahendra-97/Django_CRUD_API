# from django.core.validators import validate_email
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    # phone = models.CharField(default = 0,max_length=13, validators=[RegexValidator(r'^\+?1?\d{10}$')])
    # email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(unique=True,max_length=10)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=20)


    def __str__(self):
        return self.name
