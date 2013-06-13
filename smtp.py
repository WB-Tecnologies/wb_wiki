from inbox import Inbox
import os
import json

inbox = Inbox()

@inbox.collate
def handle(to, sender, body):
    text = body[body.find("\n", body.find('Content-Type: text/html;')):]
    subject_pos = body.find('Subject')
    subject = body[body.find(" ", subject_pos)+1:body.find("\n", subject_pos)]

    log_file = open(r'smtp.log', 'w')
    log_file.write("%s\n%s\n%s\n%s\n" % (to[0], sender, subject, text))

# Bind directly.
#inbox.serve(address='0.0.0.0', port=4467)


class Basecamp(object):

    def __init__(self, login, password, project_id):
        self.base_url = 'https://basecamp.com/1810831/api/v1/'
        self.login = login
        self.password = password
        self.project_id = project_id

    def _request(self, command):
        text = ''
        request_url = "curl -u %s:%s %sprojects/%s/%s.json" % (self.login, self.password, self.base_url, self.project_id, command)
        print request_url
        result = os.popen(request_url)
        for line in result.readlines():
            text += line
        result.close()
        print text
        return json.loads(text)


camp = Basecamp('lionasp', 'l80662', '3015357-helpdesk')
print camp._request('todolists')

