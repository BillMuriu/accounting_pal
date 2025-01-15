import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


EMAIL_BACKEND=os.environ['EMAIL_BACKEND']
EMAIL_HOST=os.environ['EMAIL_HOST']
EMAIL_PORT=os.environ['EMAIL_PORT']
EMAIL_USE_TLS=os.environ['EMAIL_USE_TLS']
EMAIL_HOST_USER=os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD=os.environ['EMAIL_HOST_PASSWORD']


EMAIL_VERIFICATION_URL = 'http://localhost:3000'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c=npkc5#jov8cw-j*$x8panrs=posr101iiqig#2qgwfpcaw6-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# settings.py
# AUTH_USER_MODEL = 'custom_auth.CustomUser'


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'rest_framework',
    'corsheaders',

# operations app
    'accounts.operations.operations_paymentvouchers',
    'accounts.operations.operations_pettycash',
    'accounts.operations.operations_receipts',
    'accounts.operations.operations_bankcharges',
    'accounts.operations.operations_balances',
    'accounts.operations.operations_cashbooks',
    'accounts.operations.operations_ledgers',
    'accounts.operations.operations_trial_balance',
    

# rmi apps
    'accounts.rmi.rmi_receipts',
    'accounts.rmi.rmi_pettycash',
    'accounts.rmi.rmi_paymentvoucher',
    'accounts.rmi.rmi_ledgers',
    'accounts.rmi.rmi_cashbook',
    'accounts.rmi.rmi_balances',
    'accounts.rmi.rmi_bankcharges',
    'accounts.rmi.rmi_trial_balance',

# tuition apps
    'accounts.tuition.tuition_balances',
    'accounts.tuition.tuition_bankcharges',
    'accounts.tuition.tuition_cashbooks',
    'accounts.tuition.tuition_ledgers',
    'accounts.tuition.tuition_paymentvouchers',
    'accounts.tuition.tuition_pettycash',
    'accounts.tuition.tuition_receipts',
    'accounts.tuition.tuition_trial_balances',

# schoolfund apps
    'accounts.school_fund.school_fund_receipts',
    'accounts.school_fund.school_fund_paymentvouchers',
    'accounts.school_fund.school_fund_pettycash',
    'accounts.school_fund.school_fund_balances',
    'accounts.school_fund.school_fund_bankcharge',
    'accounts.school_fund.school_fund_cashbook',
    'accounts.school_fund.school_fund_ledgers',

# students apps
    'students.students',
    'students.students_opening_balances',
    'other_apps.term_periods',

# authentication
    'custom_auth',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'accounting_pal.urls'

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

WSGI_APPLICATION = 'accounting_pal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # Enable form rendering in Browsable API
    ),
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True