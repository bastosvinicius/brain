#!/usr/bin/python3

from termcolor import colored
from pyzabbix import ZabbixAPI
import getpass, csv, os, urllib3, traceback, logging, sys, time
import menu

report = {
  'users': '[USERS REPORT]'
}

def mzabbix():

  def html(reporttype):
    htmlstart="""<!DOCTYPE html>
<html>
<body>

<h1>"""+reporttype+""" Report</h1>

<p></p>
"""

    def htmlmid():
      htmlmid="""
"""
    htmlend="""
</body>
</html>
"""

  def sendinfotype():
    print('')
    print('what type information u need?')
    print('')
    print('[1] - email with CSV attached')
    print('[2] - email with body content (HTML)')
    print('')
    print('[b] - back to previous menu')
    print('[q] - quit')
    print('')
    option = input('make ur choice: ')
    print('')
    if option == '1':
      formattype = csv
      print(str(formattype))
      mzabbix()
    elif option == '2':
      formattype = html
      print(str(formattype))
      mzabbix()
    elif option == 'b':
      extract()
    elif option == 'q':
      raise SystemExit()
    else:
      print('unknown option')
      sendinfotype()

  def default_menu():
    print('')
    print(colored('d(-_-)b', 'blue'))
    print('welcome to brain - zabbix\n')
    print('this script helps u to extract infos from zabbix, mass insert of hosts, items, triggers or users, get information from hosts and install, uninstall or upgrade agents')
    print('')
    print('make ur choice:\n')
    print('[1] - extract data')
    print('[2] - insert data')
    print('[3] - host check availability')
    print('[4] - mass install or upgrade')
    print('[5] - mass uninstall')
    print('')
    print('[b] - back to previous menu')
    print('[q] - quit')
    print('')
    option = input('make ur choice: ')
    print('')
    if option == '1':
      extract()
    elif option == '2':
      print('insert data menu\n')
    elif option == '3':
      print('host check availability\n')
    elif option == '4':
      print('mass agent install or upgrade\n')
    elif option == '5':
      print('mass agent uninstall\n')
    elif option == 'b':
      menu.menu()
    elif option == 'q':
      print('quiting\n')
      raise SystemExit()
    else:
      print('unknown option')
      default_menu()

  def usersget():
    output = open('/tmp/users-report.tmp', 'w')
    file = '/tmp/users-report.tmp'
    try:
      print('user id, alias, name, surname, groups', file=output)
      for row in zapi.user.get(output=["userid", "alias", "name", "surname"], selectUsrgrps=["name"]):
        print(row["userid"], row["alias"], row["name"], row["surname"], str([d["name"] for d in row["usrgrps"]]).replace(",", " |").replace("[","").replace("]",""), sep=",", file=output)
      output.close()
      print('output file created on '+file+'')
      sendinfotype()
    except:
      logging.error(traceback.format_exc())
      print('impossible to create output file '+file+'')
      print('please verify if u have necessary perssions to write on specified directory')
      default_menu()

  def extract():
    print('')
    print(colored('d(-_-)b', 'blue'))
    print('brain - zabbix extract menu\n')
    print('make ur choice\n')
    print('[1] - users report')
    print('[2] - all hosts registered')
    print('[3] - all hostgroups registered')
    print('[4] - hosts registered in a certain hostgroup')
    print('[5] - hosts registered in a certain template')
    print('[6] - executed actions in a certain period')
    print('')
    print('[b] - back to previous menu')
    print('[q] - quit')
    print('')
    option = input('make ur choice: ')
    print('')
    if option == '1':
      print('users report\n')
      reporttype = report['users']
      usersget()
      print(reporttype)
    elif option == '2':
      print('all hosts registered\n')
    elif option == '3':
      print('all hostgroups registered\n')
    elif option == '4':
      print('hosts registered in a certain hostgroup\n')
    elif option == '5':
      print('hosts registered in a certain template\n')
    elif option == '6':
      print('executed actions a certain period')
    elif option == 'b':
      default_menu()
    elif option == 'q':
      print("quiting\n")
      sys.exit()
    else:
      print('unknown option')
      extract()

  def loginerror():
    os.system('clear')
    print(colored('impossible connect to Zabbix API', 'red', attrs=['bold']))
    print(colored('verify the API URL or ur credentials', 'red', attrs=['bold']))
    print(colored('brute force not work like that', 'green', attrs=['bold']))
    menu.menu()

  class TryConn:

    def __init__(self):
      self.username = input('enter ur username: ')
      self.password = getpass.getpass('enter ur password: ')

    def getusername(self):
      return self.username

    def getpassword(self):
      return self.password
  
  zbxlogin = TryConn()
  try:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    zapi = ZabbixAPI(server="https://172.17.0.2/api_jsonrpc.php")
    zapi.session.auth = (zbxlogin.getusername(), zbxlogin.getpassword())
    zapi.session.verify = False
    zapi.timeout = 10
    zapi.login(zbxlogin.getusername(), zbxlogin.getpassword())
    print('connected to Zabbix API - Zabbix Version %s' % zapi.api_version())
    default_menu()
  except Exception:
    logging.error(traceback.format_exc())
    loginerror()
