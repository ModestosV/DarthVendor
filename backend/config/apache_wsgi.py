import os
import sys
import site

VIRTUAL_ENV_DIR = "/home/foobar/venv/darthvendor"  # Root path of the virtual environment directory
PROJECT_DIR = "/home/foobar/venv/darthvendor/SOEN343_GroupProject"  # Root path of the project directory
CONFIG_DIR = "/home/foobar/venv/darthvendor/SOEN343_GroupProject/backend/config"  # Root path of the project directory
PYTHON_VERSION = '3.5'  # Python version in the virtual environment directory

ALLDIRS = [
    PROJECT_DIR,
    CONFIG_DIR,
    "{}/lib/python{}/site_packages".format(VIRTUAL_ENV_DIR, PYTHON_VERSION)
]


def update_sys_path():

    # Remember original sys.path.
    prev_sys_path = list(sys.path)

    # Add each new site-packages directory.
    for directory in ALLDIRS:
        site.addsitedir(directory)

    # Reorder sys.path so new directories at the front.
    new_sys_path = []
    for item in list(sys.path):
        if item not in prev_sys_path:
            new_sys_path.append(item)
            sys.path.remove(item)
    sys.path[:0] = new_sys_path

update_sys_path()

# Activate virtual environment
activate_env = "{}/bin/activate_this.py".format(VIRTUAL_ENV_DIR)

with open(activate_env) as file:
    exec(file.read(), dict(__file__=activate_env))

from environment import SETTINGS_MODULE

# Import WSGI app
from django.core.wsgi import get_wsgi_application

# Set environment variables
os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)

application = get_wsgi_application()
