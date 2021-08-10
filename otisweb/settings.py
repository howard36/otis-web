"""
Django settings for otisweb project.
"""

import logging
import os
from pathlib import Path

import discordLogging  # type: ignore
import import_export.tmp_storages
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.parent.absolute()
ENV_PATH = BASE_DIR / '.env'
if ENV_PATH.exists():
	load_dotenv(ENV_PATH)

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

## Manually added settings

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
LOGIN_REDIRECT_URL = '/'

PRODUCTION = bool(os.getenv('IS_PRODUCTION'))
DEBUG = not PRODUCTION
if PRODUCTION:
	ALLOWED_HOSTS = ['otis.evanchen.cc', '.localhost', '127.0.0.1']
else:
	INTERNAL_IPS = ['127.0.0.1',]


# Application definition

INSTALLED_APPS = [
	'core',
	'dashboard',
	'exams',
	'roster',
	'arch',
	'otisweb',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.humanize',
	'django.contrib.messages',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.staticfiles',
	'debug_toolbar',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.discord',
	'allauth.socialaccount.providers.github',
	'allauth.socialaccount.providers.google',
	'bootstrap5',
	'crispy_forms',
	'crispy_bootstrap5',
	'hijack',
	'hijack.contrib.admin',
	'import_export',
	'reversion',
]

MIDDLEWARE = [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'hijack.middleware.HijackUserMiddleware',
]

ROOT_URLCONF = 'otisweb.urls'

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
		'debug': not PRODUCTION,
		},
	},
]

WSGI_APPLICATION = 'otisweb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if os.getenv("DATABASE_NAME"):
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': os.getenv("DATABASE_NAME"),
			'USER': os.getenv("DATABASE_USER"),
			'PASSWORD': os.getenv("DATABASE_PASSWORD"),
			'HOST': os.getenv("DATABASE_HOST"),
			'PORT': os.getenv("DATABASE_PORT", '3306'),
			'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
		},
	}
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': BASE_DIR / 'db.sqlite3',
		}
	}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
AUTHENTICATION_BACKENDS = [
		'django.contrib.auth.backends.ModelBackend',
		'allauth.account.auth_backends.AuthenticationBackend',
		]

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https" if PRODUCTION else "http"
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SIGNUP_FORM_CLASS = 'otisweb.forms.OTISUserRegistrationForm'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SOCIALACCOUNT_EMAIL_REQUIRED = True

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = BASE_DIR / 'static/'
MEDIA_ROOT = BASE_DIR / 'media/'

if PRODUCTION:
	DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
	STATIC_URL = os.getenv("STATIC_URL")
	GS_BUCKET_NAME = os.getenv("GS_BUCKET_NAME")
	MEDIA_URL = os.getenv("MEDIA_URL")
	assert STATIC_URL is not None
	assert GS_BUCKET_NAME is not None
	assert MEDIA_URL is not None
	IMPORT_EXPORT_TMP_STORAGE_CLASS = import_export.tmp_storages.CacheStorage
	SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
	assert SECRET_KEY is not None
else:
	STATIC_URL = '/static/'
	MEDIA_URL = '/media/'
	SECRET_KEY = 'evan_chen_is_really_cool'

FILE_UPLOAD_HANDLERS = ('django.core.files.uploadhandler.MemoryFileUploadHandler',)
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760 # 10MB

# Custom Evan keys
INVOICE_HASH_KEY = os.getenv("INVOICE_HASH_KEY", "evan_chen_is_still_really_cool")
STORAGE_HASH_KEY = os.getenv("STORAGE_HASH_KEY", "look_at_me_im_a_cute_kitten")
API_TARGET_HASH = os.getenv("API_TARGET_HASH", '1c3592aa9241522fea1dd572c43c192a277e832dcd1ae63adfe069cb05624ead')

def filter_useless_404(record: logging.LogRecord) -> bool:
	a = tuple(record.args) # type: ignore
	return not (
			len(a) == 2 \
			and a[0] == 'Not Found' \
			and ('wp-include' in a[1] or '.php' in a[1])
			) \
		and not (
			len(a) == 3 \
			and a[1] == '404' \
			and ('wp-include' in a[0] or '.php' in a[0])
			)


VERBOSE_LOG_LEVEL = 15
SUCCESS_LOG_LEVEL = 25
logging.addLevelName(VERBOSE_LOG_LEVEL, "VERBOSE")
logging.addLevelName(SUCCESS_LOG_LEVEL, "SUCCESS")

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'verbose': {
			'format': '[{levelname}] {asctime} {module} {name}\n{message}\n',
			'style': '{',
		},
	},
	'filters': {
		'filter_useless_404': {
			'()': 'django.utils.log.CallbackFilter',
			'callback': filter_useless_404,
		},
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse',
		},
		'require_debug_true': {
			'()': 'django.utils.log.RequireDebugTrue',
		}
	},
	'handlers': {
		'console': {
			'class': 'logging.StreamHandler',
			'level': 'INFO',
			'formatter': 'verbose',
			'filters': ['filter_useless_404'],
		},
		'discord': {
			'class': 'discordLogging.DiscordHandler',
			'level': 'WARNING',
			'url': os.getenv("WEBHOOK_URL"),
			'filters': ['require_debug_false', 'filter_useless_404'],
		}
	},
	'root': {
		'handlers': ['console', 'discord'],
		'level': 'INFO',
	},
	'loggers': {
		'django': {
			'handlers': ['console', 'discord'],
			'level': 'INFO',
			'propagate': False,
		},
		'django.db.backends': {
			'handlers': ['console',],
			'level': 'DEBUG',
			'filters': ['require_debug_true'],
		},
		'django.server': {
			'handlers': ['console'],
			'level': 'DEBUG',
			'propagate': False,
		}
	},
}
