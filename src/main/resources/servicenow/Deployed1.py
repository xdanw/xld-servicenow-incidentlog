
import json
import requests
import requests.utils
# Fixes some issues with TLS
import os
os.environ['REQUESTS_CA_BUNDLE'] = 'ca.pem';

# response = requests.get('https://webhook.site/062e2ea7-5a36-4abb-a2c8-862dd85f777f')
# print response.status_code;

server_uri = deployed.container.address;
if server_uri[len(server_uri)-1] != '/': server_uri = server_uri + '/';
print 'ServiceNow server: ' + server_uri;

user = deployed.container.username
pwd = deployed.container.password

# Persist these to the execution context
context.setAttribute('snow_user', user)
context.setAttribute('snow_pass', pwd)
context.setAttribute('snow_uri', server_uri)

task = context.getTask()
# Debug
# print "Task info?"
# print str(task.getId());
# print str(task.getUsername());
# print str(task.getMetadata());

msg = "XL Deploy message: " + str(task.getMetadata()['application']) + \
    " (ver: " + str(task.getMetadata()['version']) + ") " + \
    "is being deployed to: " + str(task.getMetadata()['environment']) + \
    " by user: " + str(task.getUsername());

print msg;

# --- ServiceNow API ---
# per https://docs.servicenow.com/bundle/london-application-development/page/integrate/inbound-rest/concept/c_TableAPI.html

# Set the request parameters
req_uri = server_uri + 'api/now/table/incident'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
data = "{'short_description':'" + msg +"','urgency':'5','impact':'5'}"
response = requests.post(req_uri, auth=(user, pwd), headers=headers ,data=data)

# Check for HTTP codes other than 200 and 201
if response.status_code != 200 and response.status_code != 201:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    raise exception;

# Decode the JSON response into a dictionary and use the data
data = response.json()
# print(data)
# responseData = json.loads(data)
# print str(responseData.get('result').get('sys_id')); # Get sys_id

# --- End API ---

# Dummy
deployed.ResultUri = server_uri + "incident.do?sys_id=" + str(data['result']['sys_id']);
deployed.ResponseCode = response.status_code;

context.setAttribute('ticket_sys_id', str(data['result']['sys_id']))
print 'Storing attribute... sys_id: ' + context.getAttribute('ticket_sys_id');

print "Ticket opened.";

import json
import requests
import requests.utils
# Fixes some issues with TLS
import os
os.environ['REQUESTS_CA_BUNDLE'] = 'ca.pem';

# response = requests.get('https://webhook.site/062e2ea7-5a36-4abb-a2c8-862dd85f777f')
# print response.status_code;

server_uri = deployed.container.address;
if server_uri[len(server_uri)-1] != '/': server_uri = server_uri + '/';
print 'ServiceNow server: ' + server_uri;

user = deployed.container.username
pwd = deployed.container.password

# Persist these to the execution context
context.setAttribute('snow_user', user)
context.setAttribute('snow_pass', pwd)
context.setAttribute('snow_uri', server_uri)

task = context.getTask()
# Debug
# print "Task info?"
# print str(task.getId());
# print str(task.getUsername());
# print str(task.getMetadata());

msg = "XL Deploy message: " + str(task.getMetadata()['application']) + \
    " (ver: " + str(task.getMetadata()['version']) + ") " + \
    "is being deployed to: " + str(task.getMetadata()['environment']) + \
    " by user: " + str(task.getUsername());

print msg;

# --- ServiceNow API ---
# per https://docs.servicenow.com/bundle/london-application-development/page/integrate/inbound-rest/concept/c_TableAPI.html

# Set the request parameters
req_uri = server_uri + 'api/now/table/incident'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
data = "{'short_description':'" + msg +"','urgency':'5','impact':'5'}"
response = requests.post(req_uri, auth=(user, pwd), headers=headers ,data=data)

# Check for HTTP codes other than 200 and 201
if response.status_code != 200 and response.status_code != 201:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    raise exception;

# Decode the JSON response into a dictionary and use the data
data = response.json()
# print(data)
# responseData = json.loads(data)
# print str(responseData.get('result').get('sys_id')); # Get sys_id

# --- End API ---

# Dummy
deployed.ResultUri = server_uri + "incident.do?sys_id=" + str(data['result']['sys_id']);
deployed.ResponseCode = response.status_code;

context.setAttribute('ticket_sys_id', str(data['result']['sys_id']))
print 'Storing attribute... sys_id: ' + context.getAttribute('ticket_sys_id');

print "Ticket opened.";
