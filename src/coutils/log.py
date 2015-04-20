#!/usr/bin/env python
import time
import io,os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

INFO = 1;
WARNING = 2;
DEBUG = 3;
level_ = 0;
def logConfig(level=0):
	global level_
	level_ =  level

def info(s,key='INFO'):
	if level_ == INFO or level_ == 0:
		print '[%s %s %s][%s %s %s] %s' % (bcolors.OKBLUE,key,bcolors.ENDC,bcolors.HEADER,time.strftime('%H:%M'),bcolors.ENDC,s)

def warning(s,key='WARNING'):		
	if level_ == WARNING or level_ == 0:
		print '[%s %s %s][%s %s %s]%s %s %s' % (bcolors.FAIL,key,bcolors.ENDC,bcolors.HEADER,time.strftime('%H:%M'),bcolors.ENDC,bcolors.FAIL,s,bcolors.ENDC)
		with open("/Users/nantu/projects/racpider/error.log","a") as f:
			f.write(time.strftime('[%y/%m/%d %H:%M] ')+s+os.linesep)

def debug(s,key='DEBUG'):		
	if level_ == DEBUG or level_ == 0:
		print '[%s %s %s][%s %s %s] %s' % (bcolors.WARNING,key,bcolors.ENDC,bcolors.HEADER,time.strftime('%H:%M'),bcolors.ENDC,s)
	
if __name__ == '__main__':
	logConfig(level=INFO)
	info('it is info')
	logConfig(WARNING)
	warning('it is warning')	
	logConfig(DEBUG)
	debug('it is warning')