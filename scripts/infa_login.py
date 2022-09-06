# no idea what to change more

import requests
import os


# URL = os.environ['IICS_LOGIN_URL']
USERNAME = os.environ['IICS_USERNAME']
PASSWORD = os.environ['IICS_PASSWORD']

UAT_USERNAME = os.environ['UAT_IICS_USERNAME']
UAT_PASSWORD = os.environ['UAT_IICS_PASSWORD']

# ORIGINAL
# URL = "https://dm-em.informaticacloud.com/saas/public/core/v3/login"
URL = "https://dm-em.informaticacloud.com/ma/api/v2/user/login"

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
    print(data['icSessionId'])
    myfile.write("sessionId=" + data['icSessionId'] + "\n")
    # myfile.write("sessionId=" + data['userInfo']['sessionId'] + "\n")
    myfile.write("uat_sessionId=" + uat_data['icSessionId'] + "\n")
    # myfile.write("uat_sessionId=" + uat_data['userInfo']['sessionId'] + "\n")
