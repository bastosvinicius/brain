def internet():
  from urllib.request import urlopen
  try:
    urlopen("http://www.google.com/", timeout=5)
    print("internet connection success")
  except:
    print("error to connect to internet")
    quit()
