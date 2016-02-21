cd "$(dirname "$0")"
. activate
nohup ./manage.py runserver 0.0.0.0:4242 &
