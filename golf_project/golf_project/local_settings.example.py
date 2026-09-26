# Copy this file to local_settings.py and fill in your local values.
# local_settings.py is gitignored and will not be pushed to GitHub.

SECRET_KEY = 'django-insecure-change-me'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'abraner.pythonanywhere.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://abraner.pythonanywhere.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'abraner$PRGC4',          # your PA MySQL DB name
        'USER': 'abraner',
        'PASSWORD': 'your-mysql-password',
        'HOST': 'abraner.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
