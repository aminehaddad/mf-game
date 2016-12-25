from .base import *
import dj_database_url

# Django settings
DEBUG = True if get_env_variable('DJANGO_DEBUG', False) else False
SECRET_KEY = get_env_variable('SECRET_KEY', required_from_environment=True)

ALLOWED_HOSTS_IMPORT = get_env_variable('ALLOWED_HOSTS_IMPORT', required_from_environment=True)
ALLOWED_HOSTS = ALLOWED_HOSTS_IMPORT.split(',')

# Database settings
DATABASE_URL = get_env_variable('DATABASE_URL', required_from_environment=True)
DATABASES = {
    'default': dj_database_url.config(env='DATABASE_URL'),
}
CONN_MAX_AGE = int(get_env_variable('CONN_MAX_AGE', '0'))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# From https://devcenter.heroku.com/articles/getting-started-with-django
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Redirect HTTP to HTTPS
SECURE_SSL_REDIRECT = True if get_env_variable('SECURE_SSL_REDIRECT', False) else False

# Only allow cookies over SSL
SESSION_COOKIE_SECURE = True if get_env_variable('SESSION_COOKIE_SECURE', False) else False
CSRF_COOKIE_SECURE = True if get_env_variable('CSRF_COOKIE_SECURE', False) else False
SESSION_COOKIE_AGE = int(get_env_variable('SESSION_COOKIE_AGE', '1209600'))

# Expire login sessions when the browser closes
SESSION_EXPIRE_AT_BROWSER_CLOSE = True if get_env_variable('SESSION_EXPIRE_AT_BROWSER_CLOSE', False) else False

# Static files settings
STATIC_ROOT = os.path.join(BASE_DIR, '../staticfiles')
