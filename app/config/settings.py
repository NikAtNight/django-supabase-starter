import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DJANGO_DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = 'app.urls'
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', "django-insecure-vkto8gdmiv=@3(ki%wza!2y1vurui4k_z*q&rm!m7w!y6*9ep^")
WSGI_APPLICATION = 'app.wsgi.application'
X_FRAME_OPTIONS = 'DENY'

# General
APPEND_SLASH = False
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
# If USE_I18N is set to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False
USE_L10N = True
USE_TZ = True

# CORS Settings
CORS_PREFLIGHT_MAX_AGE = 300
CORS_ORIGIN_ALLOW_ALL = True


DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:@postgres:5432/postgres',
        conn_max_age=int(os.getenv('POSTGRES_CONN_MAX_AGE', 600))
    ),
}

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

THIRD_PARTY_APPS = [
    'rest_framework',                               # utilities for rest apis
    'django_filters',                               # for filtering rest endpoints
    # 'django_cron',                                  # scheduled tasks with cron
    'corsheaders',                                  # CORS header injection
    # JWT blacklist functionality provider
    'rest_framework_simplejwt.token_blacklist',
    'django_json_widget',                           # JSON viewer for admin
    'django_celery_beat',                           # scheduled tasks
    'import_export',                                # admin import / export
]

PROJECT_APPS = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + "/static/"
STATICFILES_DIRS = []

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Media files
MEDIA_ROOT = '/media/'
MEDIA_URL = BASE_DIR + '/media/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': STATICFILES_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
