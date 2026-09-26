# Copy this file to local_settings.py and fill in your local values.
# local_settings.py is gitignored and will not be pushed to GitHub.

SECRET_KEY = 'django-insecure-change-me'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'scorecard',
        'USER': 'root',
        'PASSWORD': 'your-mysql-password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
