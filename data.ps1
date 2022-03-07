$makemigrations = 'python manage.py makemigrations equipment'
$migrate = 'python manage.py migrate'

Invoke-Expression $makemigrations
Invoke-Expression $migrate