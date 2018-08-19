#!/bin/python3.4

import os, sys, socket, pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

# local paths

localpath = os.getcwd()
localmodules = localpath+"/modules"
localconfig = localpath+"/.config"
sys.path.insert(0, localmodules)

# dictionaries

dependencies = {
  'termcolor': '1.1.0',
  'progressbar': '2.5',
  'pyzabbix': '0.7.4'
}

report = {
  'users': '[USER REPORT]'
}

# local modules

import menu, internet, this

print('')
print('hi, i\'m brain')
print('i\'ll help you to do some things with python')
print('')
print('let me test some things before we start')
print('')

print('testing modules dependencies')
try:
  pkg_resources.require(dependencies)
  print('all dependencies are satisfied')
except:
  print('not all dependencies were met')
  print('trying to install dependencies')
  print('testing your internet connection')
  try:
    internet.internet()
    print('trying to install the dependencies')
    try:
      os.system('pip3.4 install -r '+localconfig+'/modules-requiriments > /dev/null')
    except:
      print('failed to install dependencies')
      print('quitting')
      quit()
  except:
    print('no internet connection')
    print('quitting')
    quit()

# py modules

menu.menu()
