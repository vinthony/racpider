#!/bin/bash
cat logo.txt

echo "装载Redis				[开始]"
redis-cli del "rac:queue:"
echo "装载Redis				[达成]"
echo "装载Server				[开始]"
python ./src/main.py ./src/server.py
