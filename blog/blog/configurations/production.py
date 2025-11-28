from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #no queremos mostrar errores en produccion

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
       
       
        #"NAME": os.getenv('DB_NAME'),
        #"USER": os.getenv('DB_USER'),
        #"PASSWORD": os.getenv('DB_PASSWORD'),
        #"HOST": os.getenv('DB_HOST'),
        #"PORT": os.getenv('DB_PORT'),

    }#'ENGINE': 'django.db.backends.postgresql',
}    #'ENGINE': 'django.db.backends.mysql',
os.environ['DJANGO_PORT'] = '8000'