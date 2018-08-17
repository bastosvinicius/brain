from termcolor import colored
import menu

def mzabbix():
  print("")
  print(colored('hello', 'blue'), ("d(-_-)b"), colored('world', 'blue'))
  print("welcome to brain - zabbix\n")
  print("this script helps u to extract infos from zabbix, mass insert of hosts, items, triggers or users, get information from hosts and install, uninstall or upgrade agents")
  print("")
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
    print("extract data menu\n")
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
