#!/usr/bin/env python
from spider import Spider
import json,sys
sys.path.append("/Users/nantu/projects/racpider/src/")
from config import getconfig
	
config = getconfig.getconfig()
Spider(config['seeds'],config['name'],config['regexp']).fetch();