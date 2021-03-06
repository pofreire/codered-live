import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY = 'xg6ygzpg4z091bo-l0u18r-#al&-%(dlp90*j0)$&55&6@=@g8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Meus apps
    'main_page',
    'tinymce',
    'register',
    'painel_usuario',
    'equipe',
    'codedojo'
]

#TINYMCE CONFIGURATION
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "paste",
    'paste_text_sticky': True,
    'paste_text_sticky_default': True,
    'theme': "advanced",
    'theme_advanced_buttons1': "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,|,link,unlink,anchor,|,table,removeformat,code",
    'theme_advanced_buttons2': "blockquote,image,forecolorpicker, fontselect",
    'theme_advanced_buttons3': "",
    'theme_advanced_buttons4': "",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': True,
    'height': "480",
    'selector': 'textarea',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'codered.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'codered.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'codered',
#         'USER': 'root',
#         'PASSWORD': 'mysql',
#         'HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


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

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

DATE_FORMAT = 'd/m/Y' # Estipula o formato da data

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

# CORS_REPLACE_HTTPS_REFERER      = True
# HOST_SCHEME                     = "https://"
# SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT             = True
# SESSION_COOKIE_SECURE           = True
# CSRF_COOKIE_SECURE              = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
# SECURE_HSTS_SECONDS             = 1000000
# SECURE_FRAME_DENY               = True
