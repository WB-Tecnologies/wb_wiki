from inbox import Inbox
import os
import json

inbox = Inbox()

class Basecamp(object):

    def __init__(self, login, password):
        self.base_url = 'https://basecamp.com/1810831/api/v1/'
        self.login = login
        self.password = password
        self.project_id = '3082724-wb-tech-support'

    def _fill_data(self, data):
        if not data:
            return ''
        result = []
        for key, value in data.items():
            result.append('"%s": "%s"' % (key, value))
        return "-H 'Content-Type: application/json' -d '{" + ",".join(result) + "}'"

    def _request(self, command, data={}):
        text = ''
        request_url = "curl -u %s:%s  %s %sprojects/%s/%s.json" % (
            self.login, self.password, self._fill_data(data), self.base_url, self.project_id, command)
        print request_url
        result = os.popen(request_url)
        for line in result.readlines():
            text += line
        result.close()
        return json.loads(text)

    @staticmethod
    def get_url_name(obj):
        print obj
        data = obj['url'].split('/')[-1]
        return data.replace('.json', '')


@inbox.collate
def handle(to, sender, body):
    text = body[body.find("\n", body.find('Content-Type: text/html;')):]
    subject_pos = body.find('Subject')
    subject = body[body.find(" ", subject_pos)+1:body.find("\n", subject_pos)]

    
    log_file = open(r'smtp.log', 'w')
    log_file.write("%s\n%s\n%s\n%s\n" % (to[0], sender, subject, text))

# Bind directly.
#inbox.serve(address='0.0.0.0', port=4467)



camp = Basecamp('help@wbtech.pro', 'vithelpus')
todolists = camp._request('todolists/completed') + camp._request('todolists')

bugs_todolist = {}
# find todo list with name "todo"
for todolist in todolists:
    if todolist['name'] == 'todo':
        bugs_todolist = todolist
        break

# create todo list with name "todo"
if not bugs_todolist:
   bugs_todolist = camp._request('todolists', {'name': 'todo', 'description': 'auto generated todo list'})

# create task
create_command = 'todolists/%s/todos' % (Basecamp.get_url_name(bugs_todolist))
task = camp._request(create_command, {'content': 'letter subject'})

#add comment for new task
create_command = 'todos/%s/comments' % (Basecamp.get_url_name(task))
camp._request(create_command, {'content': 'letter content'})
