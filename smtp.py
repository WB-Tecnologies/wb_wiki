from inbox import Inbox

inbox = Inbox()

@inbox.collate
def handle(to, sender, body):
    text = body[body.find("\n", body.find('Content-Type: text/html;')):]
    subject_pos = body.find('Subject')
    subject = body[body.find(" ", subject_pos)+1:body.find("\n", subject_pos)]

    log_file = open(r'smtp.log', 'w')
    log_file.write("%s\n%s\n%s\n%s\n" % (to[0], sender, subject, text))

# Bind directly.
inbox.serve(address='0.0.0.0', port=4467)