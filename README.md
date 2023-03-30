# automate_time

## installation
download [chrome driver](https://chromedriver.chromium.org/downloads) according to your chrome version and expand it here <br>

create a python3 virtual environment <br>
``` 
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```
<br>


## Jira

edit automate-jira.py <br>
add your email and password <br>
edit year, month, remove_days (vacation days) values <br><br>

run
``` 
python automate-jira.py
```
you will have to enter authentication code<br>

## HRM

navigate to [hrm site](https://cdchrm.computas.com/) and get your jwt token and your employeeId making any opperation, like Log Work (Developer Tools on) <br><br>
edit automate-hrm.py <br>
add your token <br>
edit year, month, remove_days (vacation days) values <br><br>