from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.
class position(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

class Employee(models.Model):
    name=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=10)
    mobilenumber=models.CharField(max_length=15)
    position=models.ForeignKey(position,on_delete=models.CASCADE)
    email=EmailField(max_length=50)
   
    