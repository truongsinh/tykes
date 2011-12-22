__author__ = 'truongsinh'

import sys, os
#from multiprocessing import Pool
from gevent import pywsgi as wsgi #use Python server, not C++ for memory
sys.path.insert(1, "/home/truongsinh/root")
sys.path.insert(1, "/home/truongsinh/root/tykes")
os.environ['DJANGO_SETTINGS_MODULE'] = "tykes.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
#p = Pool(10) # do not accept more than 10000 connections
wsgi.WSGIServer(('', 9000), application).serve_forever()