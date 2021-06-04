import requests
import urllib
import time
import threading
from bs4 import BeautifulSoup
import random
import socket
import struct
from settings import *

ip = VICTIM_IP
passwords = ['pass1', 'admin', 'haslo', '123456', 'bardzotrudnehaslo', 'admin1234', 'qwerty', 'asdfghjkl']
url_start = f"http://{ip}/login.php"



def login(a):
    failed_login_attemps = [0, 1, 2, 3, 4, 5, 6]
    login_attemps_prob = [0.55, 0.78, 0.86, 0.9, 0.94, 0.96, 0.99]
    rand = random.uniform(0,1)
    index = sum( i < rand for i in login_attemps_prob)
    for attemp in range(index-1):
        max = len(list(passwords))-1
        passw = passwords[random.randint(0, max)]
        time.sleep(random.uniform(1, 20))
        headers={
        'Referer':f'http://{ip}/login.php',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Lanuage':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection':'keep-alive',
        'Content-Length':'88',
        'Content-Type':'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests':'1',
        'Cookie':a[0]}
        values={
            'username':'adimin',
            'password':f'{passw}',
            'Login':'Login',
            'user_token':a[1]
        }
        datas=urllib.parse.urlencode(values)
        response=requests.post(url_start,data=datas,headers=headers)
        response=requests.get(f"http://{ip}/index.php", headers=headers)
    
    time.sleep(random.uniform(1, 20))
    headers={
    'Referer':'http://{ip}login.php',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Lanuage':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection':'keep-alive',
    'Content-Length':'88',
    'Content-Type':'application/x-www-form-urlencoded',
    'Upgrade-Insecure-Requests':'1',
    'Cookie':a[0]}
    values={
        'username':'admin',
        'password':f'password',
        'Login':'Login',
        'user_token':a[1]
    }
    datas=urllib.parse.urlencode(values)
    response=requests.post(url_start,data=datas,headers=headers)


def user_traffic(a):
    login(a)


def get_cookie_token():
    host = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    print(host)

    url_start = f"http://{ip}/login.php"
    headers={'Host':f'{host}',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Lanuage':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests':'1'}
    res=requests.get(url_start,headers=headers)
    cookies=res.cookies
    print(type(cookies))
    html=res.text
    soup=BeautifulSoup(html,"html.parser")
    s=soup.find('input',type='hidden').get('value')
    print(cookies.items())
    cook=cookies.items()
    cook[1]=('security','medium')
    a=[(';'.join(['='.join(item)for item in cook]))]
    a.append(s)
    return a;
 

 
url = f"http://{ip}/login.php"
a=get_cookie_token()

for _ in range(4):
    a=get_cookie_token()
    t = threading.Thread(target=user_traffic, args=(a,))
    t.start()
    time.sleep(4)