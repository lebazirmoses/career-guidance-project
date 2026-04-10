# config/settings/development.py
from .base import *

DEBUG = True

# Show emails in console during dev
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'