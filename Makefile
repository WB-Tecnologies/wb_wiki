stop:
	kill `cat var/pid`
	
start:
	LANG=ru_RU.UTF-8
	. venv/bin/activate; gunicorn_django -c gunicorn.conf.py

notify_start:
	LANG=ru_RU.UTF-8
	. venv/bin/activate; python manage.py notifymail -d
