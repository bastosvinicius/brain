#!/usr/bin/python3

from termcolor import colored
import mzabbix, sys

def menu():
  print('')
  print(colored('hello', 'blue'), ("d(-_-)b"), colored('world', 'blue'))
  print('welcome to brain\n')
  print('share knowledge creatively')
  print('')
  print('make ur choice\n')
  print('[1] - zabbix')
  print('[2] - docker')
  print('')
  print('[q] - quit')
  print('')
  option = input('make ur choice: ')
  print('')
  if option == '1':
    print('extract data menu\n')
    mzabbix.mzabbix()
  elif option == '2':
    print('TO DO')
    sys.exit()
  elif option == 'q':
    print('quiting\n')
    sys.exit(0)
  else:
    print('unknown option')
    menu()
