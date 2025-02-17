from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-z3%n#^%jq33-x!6hr4*8b@f6bse6&m9dz3$35iw27pe0sx5b8j'
DEBUG = True
ALLOWED_HOSTS = ["*","vercel.app"]
INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'articles',
    'ckeditor',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'app.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
WSGI_APPLICATION = 'app.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
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
LANGUAGE_CODE='az'
TIME_ZONE='Asia/Baku'
USE_L10N = True
USE_I18N=True
USE_TZ=True
STATIC_URL='static/'
STATIC_ROOT=BASE_DIR / 'static'
STATICFILES_DIRS=[BASE_DIR / 'staticfiles']
MEDIA_URL='media/'
MEDIA_ROOT=BASE_DIR / 'media'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
LANGUAGES = (
    ('en', 'English'),
    ('az', 'Azerbaijani'),
    ('ru', 'Russian'),
)
LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]
MODELTRANSLATION_DEFAULT_LANGUAGE = 'az'
MODELTRANSLATION_LANGUAGES = ('az','en','ru')
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}
JAZZMIN_SETTINGS = {
    "site_brand": "Babayev",
    "site_logo_classes": "img-circle",
    "search_model": ["articles.Articles"],
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Website", "url": "http://127.0.0.1:8000", "new_window": True},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": ['auth'],
    "hide_models": [],
    "custom_js": './',
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        'articles.Articles': 'fas fa-newspaper',
        'articles.Categories': 'fas fa-folder',
    },
}