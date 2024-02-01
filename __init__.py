import os
import sys
import time
from typing import Callable

from Utils.NukeToken import NukeToken
from Utils.MDUsers import MDUsers
from Utils.DelFriends import DelFriends
from Utils.ExtGuilds import ExtGuilds
from Utils.DelMDs import DelMDs
from Utils.SpamFriends import SpamFriends
from Utils.GetInfo import GetInfo
from Utils.CrashDiscord import CrashDiscord

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

OPTIONS: str = f"""

{F.RED}╭══════════════════════════════════╦ $ ╦══════════════════════════════════╮
     {F.MAGENTA}[01] {F.WHITE}Nuke Token        {F.MAGENTA}[02] {F.WHITE}MD Users          {F.MAGENTA}[03] {F.WHITE}Delete Friends
     {F.MAGENTA}[04] {F.WHITE}Exit Guilds       {F.MAGENTA}[05] {F.WHITE}Close DMs         {F.MAGENTA}[06] {F.WHITE}Spam Friends
     {F.MAGENTA}[07] {F.WHITE}Get Token Info    {F.MAGENTA}[08] {F.WHITE}Crash Discord     {F.MAGENTA}[09] {F.WHITE}Exit from Shenron
{F.RED}╰══════════════════════════════════╦ $ ╦══════════════════════════════════╯

"""

clear: Callable[[], None] = lambda: os.system('cls' if os.name=='nt' else 'clear')

class Shenron:
     def Initialize(self) -> None:
          clear()
          print(Center.XCenter(BANNER))
          print(Center.XCenter(OPTIONS))
          
          option: str = input(f"{F.YELLOW}[{F.MAGENTA}>>{F.YELLOW}] Option: {F.WHITE}")
          self.HandleOption(option)
     def HandleOption(self, option) -> None:
          if (option=='01') or (option=='1'):
               try:
                    NukeToken().Initialize();return Shenron().Initialize()
               except KeyboardInterrupt:
                    Shenron().Initialize()
          elif (option=='02') or (option=='2'):
               try:
                    MDUsers().Initialize();return Shenron().Initialize()
               except KeyboardInterrupt:
                    Shenron().Initialize()
          elif (option=='03') or (option=='3'):
               try:
                    DelFriends().Initialize();return Shenron().Initialize()
               except KeyboardInterrupt:
                    Shenron().Initialize()
          elif (option=='04') or (option=='4'):
               try:
                    ExtGuilds().Initialize();return Shenron().Initialize()
               except KeyboardInterrupt:
                    Shenron().Initialize()
          elif (option=='05') or (option=='5'):
               try:
                    DelMDs().Initialize();return Shenron().Initialize()
               except KeyboardInterrupt:
                    Shenron().Initialize()
          elif (option=='06') or (option=='6'):
               try:
                    SpamFriends().Initialize();return Shenron().Initialize()
               except KeyboardInterrupt:
                    Shenron().Initialize()
          elif (option=='07') or (option=='7'):
               try:
                    GetInfo().Initialize();return Shenron().Initialize()
               except KeyboardInterrupt:
                    Shenron().Initialize()
          elif (option=='08') or (option=='8'):
               try:
                    CrashDiscord().Initialize();return Shenron().Initialize()
               except KeyboardInterrupt:
                    Shenron().Initialize()
          elif (option=='09') or (option=='9'):
               self.Exit()
          else:
               print(f"{F.YELLOW}[{F.MAGENTA}!{F.YELLOW}] Logging: {F.WHITE}Error: Invalid option")
               time.sleep(2.5)
               self.Initialize()
     def Exit(self) -> None:
          clear()
          print(f"{F.YELLOW}[{F.MAGENTA}!{F.YELLOW}] Logging: {F.WHITE}Exiting...")
          sys.exit()

if __name__ == "__main__":
     try:
          Shenron().Initialize()
     except KeyboardInterrupt:
          clear()
          print(f"{F.YELLOW}[{F.MAGENTA}!{F.YELLOW}] Logging: {F.WHITE}Exiting...")
          sys.exit()
     except Exception as e:
          clear()
          print(f"{F.YELLOW}[{F.MAGENTA}—{F.YELLOW}] Logging: {F.WHITE}Error: {e}")
          sys.exit()