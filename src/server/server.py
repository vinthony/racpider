#!/usr/bin/env python 
from web import WSGIApplication
import os
#init the spider

wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))
wsgi.run(5237, host='0.0.0.0')
# web(os.path.dirname(os.path.abspath(__file__))).run("127.0.0.1",5237)

