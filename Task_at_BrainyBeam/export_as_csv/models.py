from django.db import models

# Create your models here.


class EmpData(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_email=models.EmailField()
    emp_Address=models.CharField(max_length=100)
    emp_joined_date=models.DateField()

    def __str__(self):
        return f"{self.emp_name} ({self.emp_email})"
    
