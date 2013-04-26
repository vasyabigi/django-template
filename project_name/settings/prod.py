import os
from django.core.exceptions import ImproperlyConfigured

from .common import *


# If use more that 1 project on server specify project prefix here
PROJECT_PREFIX = ""


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ["%s%s" % (PROJECT_PREFIX, var_name)]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)

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
        'ENGINE': get_env_variable("DATABASE_ENGINE"),
        'NAME': get_env_variable("DATABASE_NAME"),
        'USER': get_env_variable("DATABASE_USER"),
        'PASSWORD': get_env_variable("DATABASE_PASSWORD"),
        'HOST': get_env_variable("DATABASE_HOST"),
        'PORT': get_env_variable("DATABASE_PORT"),
    }
}

# export SECRET_KEY=""
SECRET_KEY = get_env_variable("SECRET_KEY")

ADMINS = (
    # ('', ''),
)
