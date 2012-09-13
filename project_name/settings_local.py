# Local settings for {{ project_name }} project.
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'v=wfqk6oj1&amp;%5w9b-un-r8r6xk#16d38*ob5052u8-j&amp;i-@+p6'

ADMINS = (
    # ('', ''),
)

# South
SOUTH_TESTS_MIGRATE = False

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # EMAIL_SUBJECT_PREFIX = '[Rembo] '
    # EMAIL_HOST = 'smtp.gmail.com'
    # EMAIL_HOST_USER = 'email@gmail.com'
    # EMAIL_HOST_PASSWORD = 'password'
    # EMAIL_PORT = 587

    LOCAL_INSTALLED_APPS = (
        'debug_toolbar',
        'django_extensions',
    )

    # Debug toolbar
    INTERNAL_IPS = ()
    # INTERNAL_IPS = ('127.0.0.1',)

    LOCAL_MIDDLEWARE_CLASSES = (
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
        # 'memcache_toolbar.panels.memcache.MemcachePanel',  # URL: https://github.com/ross/memcache-debug-panel
        # 'debug_toolbar_mongo.panel.MongoDebugPanel',  # URL: https://github.com/hmarr/django-debug-toolbar-mongo
        # 'debug_toolbar_htmltidy.panels.HTMLTidyDebugPanel',  # URL: https://github.com/joymax/django-dtpanel-htmltidy
        # 'debug_toolbar_user_panel.panels.UserPanel',  # URL: https://github.com/playfire/django-debug-toolbar-user-panel
        # 'sites_toolbar.panels.SitesDebugPanel',  # URL: https://github.com/elvard/django-sites-toolbar
        # 'haystack_panel.panel.HaystackDebugPanel',  # URL: https://github.com/streeter/django-haystack-panel
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
