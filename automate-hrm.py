import requests
import json
from datetime import datetime, timedelta
from calendar import monthrange
from google_auth_oauthlib.flow import InstalledAppFlow
import random

year = 2023
month = "Apr"
remove_days = [12, 14, 17]

#####################################################################
httpSession = requests.Session()
url = 'https://cdchrm.computas.com:5002'

def GetEmployeeId(jwtAccessToken) -> int:
    with httpSession.get(
        f'{url}/api/users/loggedUser', 
        headers={ 'accept': 'application/json', 'Authorization': f'Bearer {jwtAccessToken}' }, 
        verify='CA_for_cdchrm_computas.crt') as r:
        r.raise_for_status()
        userInfo = json.loads(r.content)
        return userInfo["employeeId"]

#Getting an id_token from Google
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secrets.json',
    scopes=['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'openid'])
flow.redirect_uri = "http://localhost"
flow.run_local_server()
googleCredentials = flow.credentials

#Getting a HRM JWT Access Token
with httpSession.post(
    f'{url}/connect/google', 
    data={ 'googleAccessToken': googleCredentials.token }, 
    headers={'accept': 'application/json'},
    verify='CA_for_cdchrm_computas.crt') as r:
    r.raise_for_status()
    responseJsonData = json.loads(r.content)
    jwt_token = responseJsonData["access_token"]

headers_api = {
    'accept': 'application/json',
    'authority': 'cdchrm.computas.com:5002',
    'Authorization': f'Bearer {jwt_token}' 
}

employeeId = GetEmployeeId(jwt_token)
datetime_object = datetime.strptime(month, "%b")
month_number = datetime_object.month
_,max_days = monthrange(year,month_number)
days = [ x for x in range(1,max_days+1) ]
for day in remove_days: days.remove(day)
print(days)

random.seed()
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
    startTimeMinutes = random.randint(30, 59)
    d = datetime(d.year, d.month, d.day, hour=8, minute=startTimeMinutes, second=0, microsecond=0, tzinfo=d.tzinfo, fold=d.fold)
    workDurationInMinutes = random.randint(8*60, 8*60+30)
    endTime = d + timedelta(minutes=workDurationInMinutes)
    data = {
        "date": d.isoformat(),
        "employeeId":employeeId,
        "endTime":f"{endTime.hour:02}:{endTime.minute:02}",
        "startTime":f"{d.hour:02}:{d.minute:02}"
        }

    try:
        with httpSession.post(url=f'{url}/api/workLog/addOrUpdate', json=data, headers=headers_api, verify='CA_for_cdchrm_computas.crt') as response:
            response.raise_for_status()
            print(response)
    except requests.HTTPError as httpErr:
        error = json.loads(httpErr.response.content)
        print(f'Status Code: {error["StatusCode"]}, Message: {error["Message"]}')
    except Exception as err:
        print(err)
    
    


# https://cdchrm.computas.com:5002/api/workFromHome
# {"startDate":"2023-03-01T00:00:00.000Z","endDate":"2023-03-31T00:00:00.000Z","employeeId":63,"comment":"","numberDaysOff":23}