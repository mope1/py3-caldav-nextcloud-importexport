from datetime import datetime
import caldav
from caldav.elements import dav, cdav
import os
import requests
import argparse

parser = argparse.ArgumentParser(description='Export/Import Caldav')
parser.add_argument('domain')
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('operation', choices=['import', 'export'])

args = parser.parse_args()

cal_url_suf="/remote.php/dav/calendars/"
cal_url = "https://{}:{}@{}{}".format(args.username,args.password,args.domain,cal_url_suf)

client = caldav.DAVClient(cal_url)
principal = client.principal()
calendars = principal.calendars()

def export_all(path, things):
  os.makedirs(path, exist_ok=True)
  for thing in things:
    filename = os.path.basename(str(thing.url))
    print(thing.url)
    if not os.path.exists(os.path.join(path,filename)):
      res = requests.get(thing.url, auth=(args.username, args.password))
      with open(os.path.join(path,filename), 'w') as f:
        f.write(res.text)

if args.operation=='export':
  for calendar in calendars:
    export_all( os.path.join('export',calendar.name,'todos'), calendar.todos() )
    export_all( os.path.join('export',calendar.name,'events'), calendar.events() )

elif args.operation=='import':
  for calendar in calendars:
    folder = os.path.join('export',calendar.name,'todos')
    for filename in os.listdir(folder):
      with open(os.path.join(folder,filename), 'r') as f:
        text=f.read()
        try:
          print(calendar.add_todo(text))
        except caldav.lib.error.PutError as e:
          print(e)

    folder = os.path.join('export',calendar.name,'events')
    for filename in os.listdir(folder):
      with open(os.path.join(folder,filename), 'r') as f:
        text=f.read()
        try:
          print(calendar.add_event(text))
        except caldav.lib.error.PutError as e:
          print(e)
    