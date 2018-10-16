
import json
import requests
import requests.utils
# Fixes some issues with TLS
import os
os.environ['REQUESTS_CA_BUNDLE'] = 'ca.pem';

task = context.getTask()

# Retrieve parameters from execution context
sys_id = str(context.getAttribute('ticket_sys_id'))
print 'Getting attribute... sys_id: ' + sys_id;
user = str(context.getAttribute('snow_user'))
pwd = str(context.getAttribute('snow_pass'))
server_uri = context.getAttribute('snow_uri')

# --- ServiceNow API ---
# per https://docs.servicenow.com/bundle/london-application-development/page/integrate/inbound-rest/concept/c_TableAPI.html

# Set the request parameters
req_uri = server_uri + 'api/now/table/incident/' + sys_id;

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
data = "{'state':'7', 'incident_state':'7', 'close_code': 'Closed/Resolved by Caller', 'close_notes': 'Deployment complete'}"
response = requests.patch(req_uri, auth=(user, pwd), headers=headers ,data=data)

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

import json
import requests
import requests.utils
# Fixes some issues with TLS
import os
os.environ['REQUESTS_CA_BUNDLE'] = 'ca.pem';

task = context.getTask()

# Retrieve parameters from execution context
sys_id = str(context.getAttribute('ticket_sys_id'))
print 'Getting attribute... sys_id: ' + sys_id;
user = str(context.getAttribute('snow_user'))
pwd = str(context.getAttribute('snow_pass'))
server_uri = context.getAttribute('snow_uri')

# --- ServiceNow API ---
# per https://docs.servicenow.com/bundle/london-application-development/page/integrate/inbound-rest/concept/c_TableAPI.html

# Set the request parameters
req_uri = server_uri + 'api/now/table/incident/' + sys_id;

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
data = "{'state':'7', 'incident_state':'7', 'close_code': 'Closed/Resolved by Caller', 'close_notes': 'Deployment complete'}"
response = requests.patch(req_uri, auth=(user, pwd), headers=headers ,data=data)

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
