from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    designation = models.CharField(max_length=100,null=False,blank=False)
    address = models.TextField(null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    
    class Meta:
        db_table = 'employees'