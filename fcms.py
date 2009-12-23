# forestcms - Filesystem-Oriented reST CMS
# Or, for long, Filesystem-Oriented reStrcuturedText Content Management System

from __future__ import with_statement

import errno
from os import path
from wsgiref.simple_server import make_server
from pprint import pprint
from StringIO import StringIO
from docutils.core import publish_parts
import threading

local = threading.local()

class Conf:
	pass

conf = Conf()
conf.docroot = '.' # 'docroot'
conf.sysroot = 'sysroot'

STATUS = {
	200: 'OK',
	404: 'Not Found',
}

class HttpError (Exception):
	def __init__(self, status):
		self.status = status

def page2fname(page):
	if not page or page == '/':
		page = '/index'
	return path.join(conf.docroot, page[1:]) + '.rst'

def status2rstfile(status):
	return path.join(conf.sysroot, str(status)) + '.rst'

def render_rst(rst, whole=True):
	what = 'whole' if whole else 'html_body'
	content = publish_parts(rst, writer_name="html")[what]
	return content.encode('utf-8')

def render_file(fname, whole=True):
	try:
		with file(fname) as f:
			rst = f.read()
	except IOError, e:
		if e.errno == errno.ENOENT:
			raise HttpError(404)
	return render_rst(rst, whole)

def render_page(page, whole=True):
	fname = page2fname(page)
	return render_file(fname, whole)

def forestcms(environ, start_response):
	local.page = environ['PATH_INFO']
	local.env = environ
	local.headers = [('Content-type', 'text/html; charset=utf-8')]
	output = ''
	try:
		status = 200
		output = render_page(local.page)
	except HttpError, e:
		status = e.status
		output = render_file(status2rstfile(status))
	status = '%s %s' % (status, STATUS[status])
	start_response(status, local.headers)
	return [output]

httpd = make_server('', 8000, forestcms)
httpd.serve_forever()

