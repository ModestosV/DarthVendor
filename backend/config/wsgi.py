import os

from django.core.wsgi import get_wsgi_application
from environment import SETTINGS_MODULE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE.strip('config.'))

application = get_wsgi_application()
