release: python manage.py migrate
web: gunicorn accountaFitBuddy.wsgi:application --log-file - --log-level debug
