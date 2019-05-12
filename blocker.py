import time
from datetime import datetime as dt

hosts_temp= 'hosts'
hosts_path = r'C:\Windows\System32\drivers \ etc\ hosts'
redirect= '127.0.0.1'
sites_that_kill_me=['www.facebook.com','www.whatsapp.com','www.pintrest.com','www.instagram.com','www.snapchat.com']
print(dt.now())

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,17):
        print('Working Hours: ')

        with open(hosts_path, '+r') as file:
            content = file.read()
            for site in sites_that_kill_me:
                if site in content:
                    pass
                else:
                    file.write(redirect+ ''+site+'\n')
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for lines in content:
                pass