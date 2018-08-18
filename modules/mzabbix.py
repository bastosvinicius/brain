#!/bin/python3.4
from termcolor import colored
from pyzabbix import ZabbixAPI
import menu, mzabbix_extract, getpass, csv, os, urllib3, traceback, logging

def mzabbix():
  def login():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    zapi = ZabbixAPI("https://<ZABBIX URL>/api_jsonrpc.php")
    zapi.session.auth = (user, password)
    zapi.session.verify = False
    zapi.timeout = 10
    zapi.login(user, password)
    print("connected to Zabbix API Versionv %s" % zapi.api_version())

  def loginerror():
    os.system('clear')
    print(colored('impossible connect to Zabbix API', 'red', attrs=['bold']))
    print(colored('verify the API URL or ur credentials', 'red', attrs=['bold']))
    menu.menu()

  print("")
  print(colored('d(-_-)b', 'blue'))
  print("welcome to brain - zabbix\n")
  print("this script helps u to extract infos from zabbix, mass insert of hosts, items, triggers or users, get information from hosts and install, uninstall or upgrade agents")
  print("")
  user = input("input ur user: ")
  password = getpass.getpass("enter ur password: ")
  try:
    login()
  except Exception as e:
    logging.error(traceback.format_exc())
    loginerror()
  print("make ur choice\n")
  print("[1] - extract data")
  print("[2] - insert data")
  print("[3] - host check availability")
  print("[4] - mass install or upgrade")
  print("[5] - mass uninstall")
  print("")
  print("[b] - back to previous menu")
  print("[q] - quit")
  print("")
  option = input("make ur choice: ")
  print("")
  if option == '1':
    mzabbix_extract.zabbix_extract()
  elif option == '2':
    print("insert data menu\n")
  elif option == '3':
    print("host check availability\n")
  elif option == '4':
    print("mass agent install or upgrade\n")
  elif option == '5':
    print("mass agent uninstall\n")
  elif option == 'b':
    menu.menu()
  elif option == 'q':
    print("quiting\n")
    quit()
