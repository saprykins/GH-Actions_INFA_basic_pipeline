
import requests
import os
import json
import time
import sys

URL = os.environ['IICS_POD_URL']
UAT_SESSION_ID = os.environ['uat_sessionId']
UAT_COMMIT_HASH = os.environ['UAT_COMMIT_HASH']


### Open additional session for UAT
###

UAT_USERNAME = os.environ['UAT_IICS_USERNAME']
UAT_PASSWORD = os.environ['UAT_IICS_PASSWORD']

URL = "https://dm-em.informaticacloud.com/ma/api/v2/user/login"
UAT_BODY = {"username": UAT_USERNAME,"password": UAT_PASSWORD}
u = requests.post(url = URL, json = UAT_BODY)
print('artificial status code ', u.status_code)
uat_data = u.json()
print('artificial sessiod id ', uat_data['icSessionId'])
SESSION_ID = uat_data['icSessionId']
URL = os.environ['IICS_POD_URL']
###



BODY={ "commitHash": UAT_COMMIT_HASH }

print("Syncing the commit " + UAT_COMMIT_HASH + " to the UAT repo")

# Sync Github and UAT Org

HEADER = {"Content-Type": "application/json; charset=utf-8", "INFA-SESSION-ID": SESSION_ID }
HEADER_V2 = {"Content-Type": "application/json; charset=utf-8", "icSessionId": SESSION_ID }

p = requests.post(URL + "/public/core/v3/pullByCommitHash", json=BODY, headers = HEADER)



print("perso msg: ", p.status_code)

if p.status_code != 200:
    print("Exception caught: " + p.text)
    sys.exit(99)



pull_json = p.json()
print('---')
print(pull_json)
print('---')

PULL_ACTION_ID = pull_json['pullActionId']
PULL_STATUS = 'IN_PROGRESS'

while PULL_STATUS == 'IN_PROGRESS':
    print("Getting pull status from Informatica")
    time.sleep(10)
    ps = requests.get(URL + '/public/core/v3/sourceControlAction/' + PULL_ACTION_ID, headers = HEADER, json=BODY)
    pull_status_json = ps.json()
    PULL_STATUS = pull_status_json['status']['state']



if PULL_STATUS != 'SUCCESSFUL':
    print('Exception caught: Pull was not successful')
    sys.exit(99)
    

# Get all the objects for commit
URL = "https://emw1.dm-em.informaticacloud.com/saas"
r = requests.get(URL + "/public/core/v3/commit/" + UAT_COMMIT_HASH, headers = HEADER)

if r.status_code != 200:
    print("Exception caught: " + r.text)
    sys.exit(99)
    
request_json = r.json()


# Only get Mapping Tasks
r_filtered = [x for x in request_json['changes'] if ( x['type'] == 'MTT') ]

# This loop runs tests for each one of the mapping tasks
for x in r_filtered:
    BODY = {"@type": "job","taskId": x['appContextId'],"taskType": "MTT"}
    t = requests.post(URL + "/api/v2/job/", headers = HEADER_V2, json = BODY )

    if t.status_code != 200:
        print("Exception caught: " + t.text)
        sys.exit(99)

    test_json = t.json()
    PARAMS = "?runId=" + str(test_json['runId'])
    #"?taskId=" + test_json['taskId']

    STATE=0
    
    while STATE == 0:
        time.sleep(60)
        a = requests.get(URL + "/api/v2/activity/activityLog" + PARAMS, headers = HEADER_V2)
        
        activity_log = a.json()

        STATE = activity_log[0]['state']

    if STATE != 1:
        print("Mapping task: " + activity_log[0]['objectName'] + " failed. ")
        sys.exit(99)
    else:
        print("Mapping task: " + activity_log[0]['objectName'] + " completed successfully. ")


requests.post(URL + "/public/core/v3/logout", headers = HEADER)
