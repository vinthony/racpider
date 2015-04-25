#!/usr/bin/env python 
from web import web
import os

def my_app(environ,start_response):
	status = '200 OK'
	response_headers = [('Content-type','text/plain'),("my-word","someword")]
	start_response(status,response_headers)
	return [u"this is wsgi".encode("utf-8")]


web(os.path.dirname(os.path.abspath(__file__))).run("127.0.0.1",5237)

