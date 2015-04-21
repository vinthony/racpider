#!/usr/bin/env python
from spider import Spider
import json

with open("/Users/nantu/projects/racpider/Racpider.json",'r+') as f:
	body  = f.read()
	config = json.loads(body)
	Spider(config['seeds'],config['name'],config['regexp']).fetch();