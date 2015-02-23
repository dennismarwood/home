"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
#Bit frustrating, but I am not able to get openshift to include the
#OPENSHIFT_REPO_DIR in openshfit's path. So hack around this below.
ON_PASS = 'OPENSHIFT_REPO_DIR' in os.environ
if ON_PASS:
    print "wsgi.py detected PASS Environment ----------"
    x = os.path.abspath(os.path.join(os.environ['OPENSHIFT_REPO_DIR']))
    sys.path.insert(1, x)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
