#!/usr/bin/env python
import time

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
level_ = INFO;
def logConfig(level=INFO):
	global level_
	level_ =  level

def info(s,key='INFO'):
	if level_ == INFO:
		print '[%s %s %s][%s %s %s] %s' % (bcolors.OKBLUE,key,bcolors.ENDC,bcolors.HEADER,time.strftime('%H:%M'),bcolors.ENDC,s)

def warning(s,key='WARNING'):		
	if level_ == WARNING:
		print '[%s %s %s][%s %s %s]%s %s %s' % (bcolors.FAIL,key,bcolors.ENDC,bcolors.HEADER,time.strftime('%H:%M'),bcolors.ENDC,bcolors.FAIL,s,bcolors.ENDC)

def debug(s,key='DEBUG'):		
	if level_ == DEBUG:
		print '[%s %s %s][%s %s %s] %s' % (bcolors.WARNING,key,bcolors.ENDC,bcolors.HEADER,time.strftime('%H:%M'),bcolors.ENDC,s)
	
if __name__ == '__main__':
	logConfig(level=INFO)
	info('it is info')
	logConfig(WARNING)
	warning('it is warning')	
	logConfig(DEBUG)
	debug('it is warning')