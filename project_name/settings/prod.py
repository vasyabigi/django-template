import os
from django.core.exceptions import ImproperlyConfigured

from .common import *


def get_env_variable(var_name):
    """
    Get the environment variable or return exception.

    """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'NAME': get_env_variable("DATABASE_NAME"),
        'USER': get_env_variable("DATABASE_USER"),
        'PASSWORD': get_env_variable("DATABASE_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SECRET_KEY = get_env_variable("SECRET_KEY")

ADMINS = (
    # ('', ''),
)

ALLOWED_HOSTS = []
