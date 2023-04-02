# automate_time

## installation
Download [chrome driver](https://chromedriver.chromium.org/downloads) according to your chrome version and expand it here <br>

Download file [client_secret.json](https://drive.google.com/file/d/1TVpcSFdt_iXdBdi0jrSb8Ch52OGN0xGI/view?usp=share_link) in the project's root folder. 

create a python3 virtual environment <br>
``` 
virtualenv .env
On Linux execute:
    source .env/bin/activate
On Windows execute:
    .env\Scripts\activate
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

edit automate-hrm.py <br>
edit year, month, remove_days (vacation days) values <br><br>