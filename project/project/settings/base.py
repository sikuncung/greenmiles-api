import os
from requests.auth import HTTPBasicAuth

# Build paths  inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'h23jkhlkh5h54254k3h5lk43h543h523hlkh523414h'

# TEST TRIGGER ##

DEBUG = True

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    #'rest_framework_filters',
    'rest_admin.apps.RestAdminConfig',
    'rest_api.apps.RestApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'notifications',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rest_api.src.middleware.rest_authorization_middleware.RestAuthorizationMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_filters.backends.DjangoFilterBackend',
    ),
}

ROOT_URLCONF = 'project.urls'

X_FRAME_OPTIONS = 'ALLOWALL'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
STATICFILES_DIRS = [
    #os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "/static"),
    os.path.join(BASE_DIR, "static"),
    #os.path.join(BASE_DIR, "/www/static")
]

ASSETS_FOLDER = os.path.join(os.path.dirname(BASE_DIR),"project/assets")

LOG_FOLDER = os.path.join(os.path.dirname(BASE_DIR),"log")

