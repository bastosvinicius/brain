from termcolor import colored
import mzabbix

def menu():
  print("")
  print(colored('hello', 'blue'), ("d(-_-)b"), colored('world', 'blue'))
  print("welcome to brain\n")
  print("")
  print("make ur choice\n")
  print("[1] - zabbix")
  print("[2] - docker")
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
