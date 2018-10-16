
import json
import requests
import requests.utils
# Fixes some issues with TLS
import os
os.environ['REQUESTS_CA_BUNDLE'] = 'ca.pem';

task = context.getTask()

sys_id = str(context.getAttribute('ticket_sys_id'))

print 'Getting attribute... sys_id: ' + sys_id;

# --- ServiceNow API ---
# per https://docs.servicenow.com/bundle/london-application-development/page/integrate/inbound-rest/concept/c_TableAPI.html

# Set the request parameters
url = 'https://dev58646.service-now.com/api/now/table/incident/' + sys_id;

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'dgZyGsSI6L7z'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
data = "{'state':'7', 'incident_state':'7', 'close_code': 'Closed/Resolved by Caller', 'close_notes': 'Deployment complete'}"
response = requests.patch(url, auth=(user, pwd), headers=headers ,data=data)

# Check for HTTP codes other than 200 and 201
if response.status_code != 200 and response.status_code != 201:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    raise exception;

# Decode the JSON response into a dictionary and use the data
data = response.json()
# print(data)
print "sys_id: " + str(data['result']['sys_id'])

# --- End API ---

print "Ticket closed.";

raise exception;
