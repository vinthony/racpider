#!/usr/bin/env python 

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys,os,time,subprocess
from utils import log

class MyFileSystemEventHandler(FileSystemEventHandler):
	def __init__(self,fn):
		super(MyFileSystemEventHandler,self).__init__()
		self.restart = fn

	def on_any_event(self,event):
		if event.src_path.endswith('.py'):
			log.info('Python source file changed:%s' % event.src_path)
			self.restart()

command = ['echo','ok']
process = None

def kill_process():
	global process
	if process:
		log.info('Kill process [%s] ...' % process.pid)
		process.kill()
		process.wait()
		log.info('Process ended with code %s.' % process.returncode)
		process = None

def start_process():
	global process,command
	log.info('Start process %s...'% ' '.join(command))
	process = subprocess.Popen(command,stdin=sys.stdin,stdout=sys.stdout,stderr=sys.stderr)			

def restart_process():
	kill_process()
	start_process()

def start_watch(path,callback):
	observer = Observer()		
	path = os.path.join(path,"src/server")
	observer.schedule(MyFileSystemEventHandler(restart_process),path, recursive=True)	
	observer.start()
	log.info('Watching directory %s ' % path)
	start_process()
	try:
		while True:
			time.sleep(0.5)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()	

if __name__ == '__main__':
	argv = sys.argv[1:]
	if not argv:
		log.info('Usage:./pymonitor your-script.py') 
	if argv[0] !='python':
		argv.insert(0,'python')
	command = argv
	path = os.path.abspath('.')
	start_watch(path,None)	