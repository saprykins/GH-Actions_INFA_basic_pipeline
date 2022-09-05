import requests
import os

'''
'''

# connect to INFA

# MY PART
from datetime import timedelta
import json

def open_session():
    # LOGIN TO INFA

    # is used to get icSessionId
    url = 'https://dm-em.informaticacloud.com/ma/api/v2/user/login'

    myobj = {
        "@type":"login",
        "username":"TestServiceAccount",
        "password":"***"
    }

    # x is response from INFA
    x = requests.post(url, json = myobj)
    # make response as json to be able to read as dictionary
    json_obj = x.json()

    # informatica session id
    session_id = json_obj["icSessionId"]
    # print(session_id)
    
    # session_id below is INFA session id
    # ti.xcom_push(key='session_id', value=session_id)
    
    return session_id


def run_a_task(session_id):
    # START A TASK

    url_job = 'https://emw1.dm-em.informaticacloud.com/saas/api/v2/job'
    
    # get session_id from another function
    
    Headers = {"icSessionId": session_id}

    myobj = {
        "@type":"job",
        "taskId":"0119EH0I000000000002",
        "taskType":"DSS"
    }

    y = requests.post(url_job, headers=Headers, json = myobj)
    print(y)



def close_session(session_id):
    # CLOSE SESSION

    url_logout = "https://dm-em.informaticacloud.com/ma/api/v2/user/logout"

    myobj = {
        "@type":"logout"
    }
    z = requests.post(url_logout, json = myobj)
    return "session is closed"

session_id = open_session()
run_a_task(session_id)
close_session(session_id)






# ORIGINAL PART




URL = os.environ['IICS_LOGIN_URL']
USERNAME = os.environ['IICS_USERNAME']
PASSWORD = os.environ['IICS_PASSWORD']

UAT_USERNAME = os.environ['UAT_IICS_USERNAME']
UAT_PASSWORD = os.environ['UAT_IICS_PASSWORD']

URL = "https://dm-us.informaticacloud.com/saas/public/core/v3/login"
BODY = {"username": USERNAME,"password": PASSWORD}

r = requests.post(url = URL, json = BODY)

if r.status_code != 200:
    print("Caught exception: " + r.text)

UAT_BODY = BODY = {"username": UAT_USERNAME,"password": UAT_PASSWORD}

u = requests.post(url = URL, json = BODY)

if u.status_code != 200:
    print("Caught exception: " + r.text)

# extracting data in json format
data = r.json()
uat_data = u.json()

# Set session tokens to the environment
env_file = os.getenv('GITHUB_ENV')

with open(env_file, "a") as myfile:
    myfile.write("sessionId=" + data['userInfo']['sessionId'] + "\n")
    myfile.write("uat_sessionId=" + uat_data['userInfo']['sessionId'] + "\n")
