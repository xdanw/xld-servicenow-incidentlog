
import json
import requests
import requests.utils
# Fixes some issues with TLS
import os
os.environ['REQUESTS_CA_BUNDLE'] = 'ca.pem';

# print "Debug ... " + deployed.ResultUri;

# response = requests.get('https://webhook.site/062e2ea7-5a36-4abb-a2c8-862dd85f777f')
# print response.status_code;

task = context.getTask()
# Debug
# print "Task info?"
# print str(task.getId());
# print str(task.getUsername());
# print str(task.getMetadata());

msg = "Message: " + str(task.getMetadata()['application']) + \
    " (ver: " + str(task.getMetadata()['version']) + ") " + \
    "is being deployed to: " + str(task.getMetadata()['environment']) + \
    " by user: " + str(task.getUsername());

print msg;

# Dummy
deployed.ResultUri = "http://example.service-now.com/incident/INC000389.test?";
deployed.ResponseCode = "200";

print deployed.ResultUri;
print deployed.ResponseCode;

print 'Storing attribute: ...';
context.setAttribute('ticketUri', 'http://www.example.com')
print 'Getting attribute: ...';
print context.getAttribute('ticketUri')

print "Ticket opened.";

raise exception;
