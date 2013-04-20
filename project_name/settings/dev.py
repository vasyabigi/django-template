from os.path import join, normpath

from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': normpath(join(PROJECT_PATH, 'dev.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

ADMINS = (
    # ('', ''),
)

# South
SOUTH_TESTS_MIGRATE = False

# Show emails in the console during developement.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_SUBJECT_PREFIX = '[Rembo] '
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'email@gmail.com'
# EMAIL_HOST_PASSWORD = 'password'
# EMAIL_PORT = 587

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

# Debug toolbar
INTERNAL_IPS = ()
# INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
