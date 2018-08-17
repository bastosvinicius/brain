from termcolor import colored
def menu():
  print(colored('hello', 'blue'), ("d(-_-)b"), colored('world', 'blue'))
  print("welcome to brain\n")
  print("this script helps u to extract infos from zabbix, mass insert of hosts, items, triggers or users, get information from hosts and install, uninstall or upgrade agents")
  print("")
  print("make ur choice\n")
  print("[1] - extract data")
  print("[2] - insert data")
  print("[3] - host check availability")
  print("[4] - mass install or upgrade")
  print("[5] - mass uninstall")
  print("")
  print("[6] - quit")
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
  elif option == '6':
    print("quiting\n")
    quit()
