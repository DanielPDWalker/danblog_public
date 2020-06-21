# This file exists so that you can upload your code to github publicly
# and not leak any sensitive information. (local_setting.py is ignored by
# the .gitignore file, this is just a template for you to create your own).


SECRET_KEY = '' # A strong, long, secure secret_key. 
#You can make a random new one over what django gave you.

DEBUG = False # Debug should always be false in production.

ALLOWED_HOSTS = [] # List of your hosts, IPs and domain names

DATABASES = { # Your database, with table name, usernames, passwords and so on.
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '', 
    }
}

