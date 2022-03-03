
import time
import os
import random
import string
import requests
import json
from requests.structures import CaseInsensitiveDict


def sleep():
    time.sleep(3)


proxy = {
    'http': 'xxxxxx',
    'https': 'xxxxxx',
}

url = "https://tibia-b.site/entry.php"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/x-www-form-urlencoded"

chars = string.ascii_letters + string.digits + '!@#$%^*()'
random.seed = (os.urandom(1024))

names = json.loads(open('names.json').read())
sobrenomes = json.loads(open('sobrenome.json').read())
value = True
while(value):
    for name in names:
        try:
            name_extra = ''.join(random.choice(string.digits))
            segundo = ''.join(random.choice(sobrenomes))
            dominio = ['@yahoo.com', '@gmail.com', '@uol.com.br',
                       '@ig.com.br', '@bol.com.br', '@outlook.com']

            mail = name.lower() + name_extra + segundo.lower() + random.choice(dominio)
            pessoa = name.capitalize() + ' ' + segundo.capitalize()
            password = ''.join(random.choice(chars) for i in range(8))

            data = "loginemail="+mail+"&loginpassword="+password + \
                "&autenticador=&page=overview&now=1646237443201"
            sleep()
            print(data)
            resp = requests.post(url, headers=headers,
                                 data=data, proxies=proxy)
            print(resp.status_code)
        except:
            pass
