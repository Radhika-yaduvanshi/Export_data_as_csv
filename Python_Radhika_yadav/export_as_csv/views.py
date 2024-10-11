from django.shortcuts import render

# Create your views here.

import csv
from django.http import HttpResponse
from .models import EmpData

def export_as_csv(empDataAdmin,request,queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Employee_Data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email','Address','Date Joined'])

    for data in queryset:
         writer.writerow([data.emp_name, data.emp_email,data.emp_Address, data.emp_joined_date])

    return response

