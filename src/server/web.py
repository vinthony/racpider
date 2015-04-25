#!/usr/bin/env python
# -*- coding:utf-8 -*- 
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

class web(object):
	def __init__(self,_document_root):
		self.document_root = _document_root

	def run(self,domain="127.0.0.1",port=5237):
		from wsgiref.simple_server import make_server
		httpd = make_server(domain,port,self.getwsgi())
		print "wsgi application run on "+self.domain+":"+str(self.port)
		httpd.serve_forever()
	
	def getwsgi(self):
		pass
"""
用于client向server发送数据
@ask_a_job
@has_down
@post_data
"""
class Request(object):
	def __init__(self,env):
		self._env = env
	
	@property
	def remote_addr(self):
		return self._env.get('REMOTE_ADDR','0.0.0.0')
	@property
	def document_root(self):
	    return self._env.get('DOCUMNET_ROOT','')
	@property
	def query_string(self):
	    return self._env.get('QUERY_STRING',"")
	@property
	def environ(self):
	    return self._env
	@property
	def request_method(self):
	    return self._env['REQUEST_METHOD']
	@property
	def path_info(self):
	    return urllib.unquote(self._env.get('PATH_INFO',''))
	@property
	def host(self):
	    return self._env.get('HTTP_HOST','')
	
	def _get_headers(self):
		if not hasattr(self,"_headers"):
			hdrs = {}
			for k,v in self._env.iteritems():
				if k.startswith("HTTP_"):
					hdrs[k[5:].replace("_","-").upper()] = v.decode('utf-8') 
			self._headers = hdrs
		return self._headers

	@property
	def headers(self):
	    return dict(**self._get_headers())
					  
	def header(self,header,default=None):
		return self._get_headers().get(header.upper(),default)
	def _get_cookies(self):
		if not hasattr(self,"_cookies"):
			cookies = {}
			cookie_str = self._env.get('HTTP_COOKIE')
			if cookie_str:
				for c in cookie_str.split(';'):
					pos = c.find('=')
					if pos > 0:
						cookies[c[:pos].strip()] = _unquote(c[pos+1:])					   
			self._cookies = cookies
		return self._cookies
		
	@property
	def cookies(self):
	    return dict(**self._get_cookies())

	def cookie(self,name,default=None):
		return self._get_cookies().get(name,default)    
			
	    
	    
	
		
"""
用于server向client返回数据
@job_url
"""
class Response(object):
	def __init__():
		pass

if __name__ == '__main__':
	 r = Request({'REQUEST_METHOD':'POST', 'wsgi.input':StringIO('a=1&b=M%20M&c=ABC&c=XYZ&e=')})		
	 print r
