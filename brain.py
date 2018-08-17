#!/bin/python3.4

print("hi, i'm brain")
print("now i'll help you to do some things that zabbix can offer you with python lang")

# py modules

import os, sys
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

# check pre-reqs

dependencies = {
  'termcolor': '1.1.0',
  'progressbar': '2.5',
  'pyzabbix': '0.7.4'
}

try:
  pkg_resources.require(dependencies)
  print("all dependencies are satisfied")
except:
  print("failed to load dependencies")
  os.system('pip3.4 install -r .config/requirements.txt > /dev/null')

# local modules

localpath = os.getcwd()
localmodules = localpath+"/modules"
sys.path.insert(0, localmodules)

import menu

menu.menu()
