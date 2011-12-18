import os
import socket
hostname = socket.gethostname()
if hostname == 'truongsinh-HP-Compaq-6520s':
	DEBUG = TEMPLATE_DEBUG = True
	PROJECT_ROOT = "/home/truongsinh/Dropbox/Sites/tykes/"
	BASE_PATH = "tykes/"
	BASE_URL = "http://localhost:8000/tykes/"
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(PROJECT_ROOT, 'data/sqlite3'),

			}
	}
elif hostname == 'TruongSinh-Hackintosh.local':
	DEBUG = TEMPLATE_DEBUG = True
	PROJECT_ROOT = "/Users/truongsinh/Sites/tykes/"
	BASE_PATH = "tykes/"
	BASE_URL = "http://localhost:8000/tykes/"
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(PROJECT_ROOT, 'data/sqlite3'),
			}
	}
elif hostname:
	DEBUG = TEMPLATE_DEBUG = True
	PROJECT_ROOT = "/home/truongsinh/root/tykes/"
	BASE_PATH = "tykes/"
	BASE_URL = "http://sinhlinh.net:9000/tykes/"
	DATABASES = {
		'default': {
			#	'''
			#	'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
			#	'NAME': 'tykes',                      # Or path to database file if using sqlite3.
			#	'USER': 'truongsinh',                      # Not used with sqlite3.
			#	'PASSWORD': '&',                  # Not used with sqlite3.
			#	'HOST': 'db.doraemontimes.com',                      # Set to empty string for localhost. Not used with sqlite3.
			#	'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
			#	'''
			'ENGINE': 'django.db.backends.sqlite3',
			# Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': '/home/truongsinh/root/tykes/data/sqlite3',
			'USER': 'truongsinh', # Not used with sqlite3.
			'PASSWORD': '&', # Not used with sqlite3.
			'HOST': 'db.doraemontimes.com', # Set to empty string for localhost. Not used with sqlite3.
			'PORT': '', # Set to empty string for default. Not used with sqlite3.
		}
	}
# Django settings for tykes project.

ADMINS = (
	('TruongSinh Tran', 'truongsinh.tran@gmail.com'),
)

MANAGERS = ADMINS



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

_ = lambda s: s

LANGUAGES = (
	('en', _('English')),
	('fi', _('Finnish')),
	('vi', _('Vietnamese')),
	)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# calculated paths for django and the site
# used as starting points for various other paths


FIXTURE_DIRS = (
os.path.join(PROJECT_ROOT, 'fixtures/'),
)
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "%s%s" % (BASE_URL, "static/")

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/tykes/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
#os.path.join(PROJECT_ROOT, 'static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
	)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-*5#&^_)&f97gbe-u1t85hw#@9=ta32lf=(c=zcvl5p68ve8lo'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	#     'django.template.loaders.eggs.Loader',
	)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.locale.LocaleMiddleware',

	)

ROOT_URLCONF = 'tykes.urls'

TEMPLATE_DIRS = (
	os.path.join(PROJECT_ROOT, 'templates'),
	)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#STATIC_URL = "%s%s" % (BASE_URL, "static/")
STATIC_URL = "http://media.lawrence.com/static/"
INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	# 'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# Uncomment the next line to enable the admin:
	'django.contrib.admin',
	# Uncomment the next line to enable admin documentation:
	# 'django.contrib.admindocs',
	'entry',
	'haystack',
	'multilingual_model',
	'django_basic_feedback',
	'page',
	)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
			},
		}
}
#LOGIN_URL = "%s%s" % (BASE_PATH, 'admin/')
LOGOUT_URL = "%s%s" % (BASE_PATH, 'admin/logout/')

LOCALE_PATHS = (
os.path.join(PROJECT_ROOT, 'locale'),
)
HAYSTACK_CONNECTIONS = {
	'default': {
		'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
		'PATH': os.path.join(PROJECT_ROOT, 'data/index'),
		},
}