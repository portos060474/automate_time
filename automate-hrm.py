import unittest
import requests
import json
import sys

import time
from datetime import datetime
from calendar import monthrange


jwt_token = 'your token'
url = 'https://cdchrm.computas.com:5002'
employeeId = "63"
year = 2023
month = "Mar"
remove_days = [13,14,15,16,17]
datetime_object = datetime.strptime(month, "%b")
month_number = datetime_object.month
month_number = datetime_object.month
_,max_days = monthrange(year,month_number)
days = [ x for x in range(1,max_days+1) ]
for day in remove_days: days.remove(day)
print(days)


for day in days:

    d = datetime(year, datetime.strptime(month, "%b").month, day);
    print('-'*50)
    print(d.isoformat())
    if d.weekday() > 4:
        print('Given date is weekend.')
        continue
    else:
        print('Given data is weekday.')
  
    print("logging work")
    
    
    headers_api = {
    'accept': 'application/json',
    'authority': 'cdchrm.computas.com:5002',
    'Authorization': 'Bearer ' + jwt_token 
    }
    
    
    
    data = {
        "date": d.isoformat(),
        "employeeId":employeeId,
        "endTime":"16:00",
        "startTime":"09:00"
        }

    try:
        response = requests.post(url=url + '/api/workLog/addOrUpdate', json=data, headers=headers_api, verify=False)
    except requests.exceptions as err:
        print(err)
        response = 'error'
    print(response)
    
    


# https://cdchrm.computas.com:5002/api/workFromHome
# {"startDate":"2023-03-01T00:00:00.000Z","endDate":"2023-03-31T00:00:00.000Z","employeeId":63,"comment":"","numberDaysOff":23}