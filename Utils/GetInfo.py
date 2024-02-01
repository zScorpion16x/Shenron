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

class GetInfo:
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
          
          data = requests.get(self.api, headers=self.headers).json()
          _friends: int = 0
          friends = requests.get(f"{self.api}/relationships", headers=self.headers).json()
          for x in friends:
               _friends: int = _friends + 1
          _guilds: int = 0
          guilds = requests.get(f"{self.api}/guilds", headers=self.headers).json()
          for x in guilds:
               _guilds: int = _guilds + 1
          billing = requests.get(f"{self.api}/billing/payment-sources", headers=self.headers).json()
          status = requests.get(f"{self.api}/settings", headers=self.headers).json()
          
          DATA: str = f"""
          {F.RED}Account Data
          {F.MAGENTA}[USER] — {F.WHITE}{data['username']}#{data['discriminator']}
          {F.MAGENTA}[ID] — {F.WHITE}{data['id']}
          {F.MAGENTA}[BIO] — {F.WHITE}{data['bio'] if data['bio'] else 'None'}
          {F.MAGENTA}[LANG] — {F.WHITE}{data['locale']}
          {F.MAGENTA}[FLAGS] — {F.WHITE}{data['public_flags']}
          {F.MAGENTA}[CUSTOM] — {F.WHITE}{status['custom_status']}
          {F.MAGENTA}[STATUS] — {F.WHITE}{status['status']}
          {F.MAGENTA}[GUILDS] — {F.WHITE}{_guilds}
          {F.MAGENTA}[FRIENDS] — {F.WHITE}{_friends}
          
          {F.RED}Contact Data
          {F.MAGENTA}[EMAIL] — {F.WHITE}{data['email'] if data['email'] else 'None'}
          {F.MAGENTA}[PHONE] — {F.WHITE}{data['phone'] if data['phone'] else 'None'}
          {F.MAGENTA}[BILLING] — {F.WHITE}{bool(billing)}
          
          {F.RED}Security Data
          {F.MAGENTA}[VERIFIED] — {F.WHITE}{data['verified']}
          {F.MAGENTA}[2FA/MFA] — {F.WHITE}{data['mfa_enabled']}
          """
          
          print(Center.XCenter(DATA))
          
          input(Center.XCenter(f"\n\n\n\n\n{F.YELLOW}[{F.MAGENTA}?{F.YELLOW}] Press any key for continue"))