from termcolor import colored
import mzabbix

def menu():
  print("")
  print(colored('hello', 'blue'), ("d(-_-)b"), colored('world', 'blue'))
  print("welcome to brain\n")
  print("this script helps u to extract infos from zabbix, mass insert of hosts, items, triggers or users, get information from hosts and install, uninstall or upgrade agents")
  print("")
  print("make ur choice\n")
  print("[1] - zabbix")
  print("")
  print("[q] - quit")
  print("")
  option = input("make ur choice: ")
  print("")
  if option == '1':
    print("extract data menu\n")
    mzabbix.mzabbix()
  elif option == 'q':
    print("quiting\n")
    quit()
