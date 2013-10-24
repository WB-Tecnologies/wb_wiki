# -*- coding: utf-8 -*-
import os

ROOT_PATH = os.path.realpath(os.path.dirname(__file__))
_rel = lambda *args: os.path.join(ROOT_PATH, *args)

bind = "0.0.0.0:8000"
daemon = True
preload_app = True
workers = 3
timeout = 10
user = "www-data"
group = "www-data"
logfile = _rel('var', 'gunicorn.log')
errorlog = _rel('var', 'error.log')
accesslog = _rel('var', 'access.log')
loglevel = "debug"
proc_name = "wb_wiki"
pidfile = _rel('var', 'pid')
