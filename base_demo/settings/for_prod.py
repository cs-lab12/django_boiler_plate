from .general_settings import *


DEBUG = False
ALLOWED_HOSTS = ['ip-address', 'domain_name']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2,
        'NAME': 'your-db-name',
        'USER': 'your-db-user-name',
        'PASSWORD': 'your-db-password',
        'HOST': 'localhost',
        'PORT': ''
    }
}
