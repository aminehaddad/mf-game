from .base import *

SECRET_KEY = 'f(&kd3mja+k01e!7_d)g!fu4-r3bn%0=w2%q-o$v@g88hb!b!1'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
