from django.contrib import admin

# Register your models here.

from .models import EmpData
from .views import export_as_csv

class EmpDataAdmin(admin.ModelAdmin):
    list_display=('emp_name','emp_email','emp_Address','emp_joined_date')
    actions=[export_as_csv]

admin.site.register(EmpData,EmpDataAdmin)