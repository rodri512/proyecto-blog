from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'mi_dominio_prod-ejemplo.com']

#DATA BASE
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
       

    }#'ENGINE': 'django.db.backends.postgresql',
}    #'ENGINE': 'django.db.backends.mysql',

os.environ['DJANGO_PORT'] = '3000'
