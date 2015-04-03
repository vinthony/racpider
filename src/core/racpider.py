#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='welcome to the world of racpider')
parser.add_argument('command',default='fetch',help="create a new racpider project")
args = parser.parse_args()
print args.accumulate(args.integers)
