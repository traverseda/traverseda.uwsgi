from .orig_{{django_settings| basename |replace(".py", "") }} import *

##Create a unique secret key for the project
try:
    from .secret_key import *
except ImportError:
    from django.utils.crypto import get_random_string
    SETTINGS_DIR=os.path.abspath(os.path.dirname(__file__))
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(50, chars)

    secretfile = open(SETTINGS_DIR+"/secret_key.py", 'w')
    secretfile.write("SECRET_KEY = \'"+secret_key+"\'\n")
    secretfile.close()
    from .secret_key import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{name}}',
        'USER': '{{name}}',
        'PASSWORD': "{{lookup('password', 'data/{{name}}_postgresPassword.txt length=32')}}",
        'HOST': 'localhost',
        'PORT': '',
    }
}

import os

ALLOWED_HOSTS={{allowed_hosts | default(["localhost",])}}

STATIC_ROOT=os.path.expanduser('~/www/static')
STATIC_URL="/~{{name}}/static/"
MEDIA_ROOT=os.path.expanduser('~/www/media')
MEDIA_URL="/~{{name}}/media/"
