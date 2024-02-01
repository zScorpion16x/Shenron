import os
import sys
import json
import time
from typing import Callable, Dict, List

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

class ExtGuilds:
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
          
          params: Dict[str, str] = {
               'Limit': 100,
               'After': None
          }
          
          print(f"{F.YELLOW}[{F.MAGENTA}!{F.YELLOW}] Logging: {F.WHITE}Leaving guilds...")
          _api: str = f"https://discord.com/api/v9/users/@me/guilds"
          
          GUILDS: List[str] = []
          _GUILDS = requests.get(_api, headers=self.headers, params=params).json()
          
          for _guild in _GUILDS:
               GUILDS.append(_guild['id'])
          for guild in GUILDS:
               self.headers: Dict[str, str] = { 'Authorization': self.token }
               uri: str = f"https://discord.com/api/v9/users/@me/guilds/{guild}"
               response = requests.delete(uri, headers=self.headers)
               
               if (response.status_code==200) or (response.status_code==204):
                    print(f"\n{F.YELLOW}[{F.MAGENTA}!{F.YELLOW}] Logging: {F.WHITE}Leaved guild: {F.GREEN}{guild}")
               else:
                    print(f"\n{F.YELLOW}[{F.MAGENTA}!{F.YELLOW}] Logging: {F.WHITE}Guild not leaved: {F.RED}{guild}")
          print(f"\n{F.YELLOW}[{F.MAGENTA}!{F.YELLOW}] Logging: {F.WHITE}Guilds leaved sucessfuly...")
          input(Center.XCenter(f"\n\n\n\n\n{F.YELLOW}[{F.MAGENTA}?{F.YELLOW}] Press any key for continue"))