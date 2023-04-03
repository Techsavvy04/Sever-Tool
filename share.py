import os
import random
import threading
import requests
from pystyle import *
import time
import sys
import datetime

class MainSHare:
    def __init__(self):
        try:
            self.open_file = open('token.txt').read().split('\n')
            self.open_file.remove('')
            self.total = str(len(self.open_file))
        except:
            quit(self._print("$", 'No Such File "token.txt"'))
    def _print(self, symbol, text):
        return f"                      [{symbol}] {text}"
    def banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        title = '\n\n\n--By: Toan#2006--'
        banner = '''\n████████╗ ██████╗ ████████╗\n╚══██╔══╝██╔═══██╗╚══██╔══╝\n   ██║   ██║   ██║   ██║ \n   ██║   ██║▄▄ ██║   ██║   \n   ██║   ╚██████╔╝   ██║   \n   ╚═╝    ╚══▀▀═╝    ╚═╝   \n\n'''
        print(Center.XCenter(title+f'Token: {self.total}')+ Center.XCenter(banner)) 
        if self.total == '0':
            quit(self._print("@", "Token Number Not Enough!"))
    def share(self, id_post, token):
        rq = random.choice([requests.get, requests.post])
        dt_now = datetime.datetime.now()
        response = rq(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={token}').json()
        if 'id' in response:
            print(self._print("*",f"{dt_now.strftime('%H:%M:%S')}: {response['id']}"))
        else:
            print(self._print("*",f"{dt_now.strftime('%H:%M:%S')}: SHARE POST FAILED!"))
    def run_share(self):
        while True:
            main.banner()
            try: 
                id_post = input(self._print("!",f"INPUT POST ID: "))
                threa = int(input(self._print("!",f"INPUT THREAD: ")))
                if id_post != '' and threa > 0:
                    break
                else:
                    print(self._print("#", "THREAD > 0!"))
                    time.sleep(3)
            except:
                print(self._print("#", "THREAD INT!"))
                time.sleep(3)
        while True:
            for token in self.open_file:
                t = threading.Thread(target=self.share, args=(id_post, token))
                t.start()
                while threading.active_count() > threa:
                    pass
if __name__ == "__main__":
    try:
        main = MainSHare()
        main.run_share()
    except KeyboardInterrupt:
        time.sleep(3)
        sys.exit('\n'+main._print('*', 'Good Bye:)'))
