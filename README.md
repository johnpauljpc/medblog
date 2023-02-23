# medblog

to backup your database before switching from SQLite to posgres use:
<b>python -Xutf8 ./manage.py dumpdata > data.json</b>


Before changing configurations, check you connect with the current database:

<b>python manage.py check --database default</b>