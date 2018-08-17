#!/bin/python3.4

import os, sys, socket, pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

# local paths

localpath = os.getcwd()
localmodules = localpath+"/modules"
localconfig = localpath+"/.config"
sys.path.insert(0, localmodules)

# local modules

import menu, internet

print("hi, i'm brain")
print("i'll help you to do some things that zabbix can offer you with python lang")

try:
  internet.internet()
except:
  print("no internet connection")

try:
  pkg_resources.require(dependencies)
  print("all dependencies are satisfied")
except:
  print("not all dependencies were met")
  print("trying to install the dependencies")
  try:
    os.system('pip3.4 install -r '+localconfig+'/modules-requiriments > /dev/null')
  except:
    print("failed to install dependencies")
    print("quitting")
    quit()

# py modules

menu.menu()
