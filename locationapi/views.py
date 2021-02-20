from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

import pandas as pd
import numpy as np 
import requests 
import json, os 
import csv

# Read Config File
with open(os.path.join(settings.BASE_DIR, 'config.json')) as secrets_file:
    config = json.load(secrets_file)


def upload_excel(request):
    """
    Returns a excel file with co-ordinates 
    provided by user in a csv file.
    """
    if request.method == 'GET':
        return render(request, 'locationapi/upload_excel.html')
    else:
        # File recieved and processed using pandas dataframe
        excel_file = request.FILES["excel_file"]
        excel_data = pd.read_csv(excel_file)
        for val in excel_data['address']:
            url = f"http://www.mapquestapi.com/geocoding/v1/address?key={config['MAPQUEST_API_KEY']}&location={val}"
            output = requests.get(url)
            json_output = output.json()
            loc = json_output['results'][0]['providedLocation']['location']
            lat = json_output['results'][0]['locations'][0]['latLng']['lat']
            lng = json_output['results'][0]['locations'][0]['latLng']['lng'] 
            excel_data.loc[excel_data.address == loc, ['latitude', 'longitude']] = lat, lng

        # Reponse file sent to user
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=output.csv'
        writer = csv.writer(response)
        writer.writerow(['no' ,'address', 'latitude', 'longitude'])

        for row in excel_data.itertuples():
            writer.writerow(list(row))
        
        return response
