#!/bin/python3.4
from termcolor import colored
from pyzabbix import ZabbixAPI
import menu, mzabbix, getpass, csv, os, urllib3, traceback, logging

def zabbix_extract():
  print("")
  print(colored('d(-_-)b', 'blue'))
  print("brain - zabbix extract menu\n")
  print("")
  print("make ur choice\n")
  print("[1] - users report")
  print("[2] - all hosts registered")
  print("[3] - all hostgroups registered")
  print("[4] - hosts registered in a certain hostgroup")
  print("[5] - hosts registered in a certain template")
  print("[6] - executed actions in a certain period")
  print("")
  print("[b] - back to previous menu")
  print("[q] - quit")
  print("")
  option = input("make ur choice: ")
  print("")
  if option == '1':
    print(user)
  elif option == '2':
    print("insert data menu\n")
  elif option == '3':
    print("host check availability\n")
  elif option == '4':
    print("mass agent install or upgrade\n")
  elif option == '5':
    print("mass agent uninstall\n")
  elif option == 'b':
    mzabbix.mzabbix()
  elif option == 'q':
    print("quiting\n")
    quit()
