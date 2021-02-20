from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

def upload_excel(request):
    if request.method == 'GET':
        return render(request, 'locationapi/upload_excel.html')
    else:
        excel_file = request.FILES["excel_file"]
        excel_data = pd.read_csv(excel_file)
        print(excel_data)
        return render(request, 'locationapi/upload_excel.html')
