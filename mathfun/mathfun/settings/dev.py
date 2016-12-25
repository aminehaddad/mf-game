from .base import *
import dj_database_url

# Django settings
DEBUG = True
SECRET_KEY = '0%@-lkegbrljp2%_v16nz4lb3&yws4(ov5-62h^@2l0&^=%@g5'
ALLOWED_HOSTS = ['*']

# Enable /admin/
DJANGO_ADMIN_ENABLED = True

# Database settings
DATABASES = {
    'default': dj_database_url.config(default='postgres://vagrant:vagrant@127.0.0.1/vagrant'),
}
