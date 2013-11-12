# if no .venv, diaf

.venv/bin/pip install -r requirements.txt
#.venv/bin/python manage.py collectstatic --noinput
.venv/bin/python manage.py syncdb --noinput
.venv/bin/python manage.py migrate --noinput
.venv/bin/python manage.py runserver
