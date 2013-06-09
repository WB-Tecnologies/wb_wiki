from inbox import Inbox

inbox = Inbox()

@inbox.collate
def handle(to, sender, subject, body):
    print "work %s %s" % (to, sender)

# Bind directly.
inbox.serve(address='0.0.0.0', port=4467)