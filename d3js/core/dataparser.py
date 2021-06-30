#!/usr/bin/python3.8

'''
make file executable: sudo chmod +x dataparser.py
use interpreter from shebang: ./dataparser.py
'''

import csv
import requests
import json
import cgi
import cgitb
import sys

cgitb.enable() # enables CGI error reporting

air = "https://raw.githubusercontent.com/rpalloni/dataset/master/airquality.csv"

def get_data(url):
    ''' fetch csv data from url, remove Nan and return json data '''
    r = requests.get(url)
    data = r.text
    RESULTS = {'data': []}
    for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
        if line['Ozone'] == 'NA' or line['SolarRay'] == 'NA' or line['Wind'] == 'NA':
            pass
        else:
            RESULTS['data'].append({
                'ozone': line['Ozone'],
                'solar': line['SolarRay'],
                'wind': line['Wind'],
                'temp': line['Temp'],
                'month': line['Month'],
                'day': line['Day']
            })
    return RESULTS['data'] # array of objects [{...},{...},{...}]

d = get_data(air)

# compose response
sys.stdout.write("Content-Type: application/json\n\n")
sys.stdout.write(json.dumps(d, indent=1))
sys.stdout.close()
