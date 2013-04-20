import os
from django.core.exceptions import ImproperlyConfigured

from .common import *


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)

# If use more that 1 project on server specify project prefix in env
PROJECT_PREFIX = os.environ.get("PROJECT_PREFIX", "")

"""
# Production {{ project_name }} settings:
export DATABASE_ENGINE=""
export DATABASE_NAME=""
export DATABASE_USER=""
export DATABASE_PASSWORD=""
export DATABASE_HOST=""
export DATABASE_PORT=""
"""
DATABASES = {
    'default': {
        'ENGINE': get_env_variable("%sDATABASE_ENGINE" % PROJECT_PREFIX),
        'NAME': get_env_variable("%sDATABASE_NAME" % PROJECT_PREFIX),
        'USER': get_env_variable("%sDATABASE_USER" % PROJECT_PREFIX),
        'PASSWORD': get_env_variable("%sDATABASE_PASSWORD" % PROJECT_PREFIX),
        'HOST': get_env_variable("%sDATABASE_HOST" % PROJECT_PREFIX),
        'PORT': get_env_variable("%sDATABASE_PORT" % PROJECT_PREFIX),
    }
}

# export SECRET_KEY=""
SECRET_KEY = get_env_variable("%sSECRET_KEY" % PROJECT_PREFIX)

ADMINS = (
    # ('', ''),
)
