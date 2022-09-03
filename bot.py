from rubpy import Rubika
from re import findall
from time import sleep
import asyncio
from colorama import Fore, Back , Style, init
import rainbowtext, pyfiglet
from time import sleep
from os import system
import os
import sys,time
import sys,time
from json import loads,dumps
from requests import post
from datetime import date
from colorama import Fore, Back , Style, init
import rainbowtext, pyfiglet
import time
import datetime
from rubpy import Rubika
from re import findall
from time import sleep
import asyncio
print(rainbowtext.text(pyfiglet.figlet_format(' E L I A S-A‌ V‌ A ')))

x = """⠀
               ○＿＿＿＿＿＿＿＿＿
                 ∥                                |
                 ∥ 𝙎𝙀𝙉𝘿 𝙏𝙊 𝙂𝘼𝙋   |
                 ∥                                |
                 ∥￣￣￣￣￣￣￣￣
       ∧_∧   ∥
    (`･ω･ ) ∥
    ヽ    つ０
     し―Ｊ"""

bot = Rubika  ("گریه کن")
channel_guid : str = ("c0Ee9X09008b057804dadf8f941e305a")

post_link: str = ("https://rubika.ir/Elias_hacker/CHGDGFFEHCEHFBE")

green='\033[32m'
darkblue = '\033[34m' 
red = '\033[91m'
get_infos: list = [] # get post info
links = []

print(Fore.MAGENTA+'⤺')
time.sleep(0)
os.system("clear")
print(Fore.MAGENTA+'⤻')
print(Fore.YELLOW+'')
print('  10%')
time.sleep(0)
os.system("clear")
print(Fore.MAGENTA+'⤺')
print(Fore.GREEN+'')
print('  20%')
time.sleep(0)
os.system("clear")
print(Fore.MAGENTA+'⤻')
print(Fore.RED+'')
print('  30%')
time.sleep(0)
os.system("clear")
print(Fore.MAGENTA+'⤺')
print(Fore.GREEN+'')
print('  40%')
time.sleep(0)
os.system("clear")
print(Fore.MAGENTA+'⤻')
print(Fore.YELLOW+'')
print('  50%')
time.sleep(0)
os.system("clear")
print(Fore.MAGENTA+'⤺')
print(Fore.GREEN+'')
print('  60%')
time.sleep(0)
os.system("clear")
print(Fore.MAGENTA+'⤻')
print(Fore.RED+'')
print('  70%')
time.sleep(0)
os.system("clear")
print(Fore.MAGENTA+'⤺')
print(Fore.GREEN+'')
print('  80%')
time.sleep(0)
os.system("clear")
print(Fore.MAGENTA+'⤻')
print(Fore.YELLOW+'')
print('  90%')
time.sleep(0)
os.system("clear")
print(Fore.MAGENTA+'⤺')
print(Fore.GREEN+'')
print('  100%')
time.sleep(0.5)
os.system("clear")
print(Fore.MAGENTA+'⤻')
print('')
print(Fore.MAGENTA+'⤺')
print(Fore.GREEN+'')
print(' STARTED BOT')
time.sleep(0.5)
os.system("clear")
async def main():
	t: bool = False
	while(t != True):
		try:
			message_info: str = await bot.getLinkFromAppUrl(post_link)
			global get_infos
			get_infos.append(message_info['message_id'])
			get_infos.append(message_info['object_guid'])
			t: bool = True
		except:
			t: bool = False

	t: bool = False
	sum = 0
	while(t!=True):
		try:
			messages : list = await bot.getMessagesInterval(channel_guid, await bot.getChannelLastMessageId(channel_guid))
			t:bool=True
		except:
			t:bool=False
	for msg in messages:
		try:
			msg = msg['text']
			group_link = findall(r"https://rubika.ir/joing/\w{32}", msg)
			for link in group_link:
				links.append(link)
		except: pass
	
	while(1):
		for link in links:
			sleep(2.5)
			t:bool=False
			count:int=0
			limit:int=5
			while(count<1 and t!=True):
				sum+=1
				try:
					group_guid:str= await bot.joinGroup(link)
					group_guid: str =group_guid.get('data').get('group').get('group_guid')
					
					
					t:bool=True
					count += 5
				except:
					t:bool=False
					count += 1
			t:bool=False
			count:int=0
			limit:int=5
			while(count<5 and t!=True):
				try:
				#	await bot.sendMessage(group_guid, "تبلیغ")
					await bot.forwardMessages(get_infos[1], [get_infos[0]], group_guid)
					print(green + "\n_______________________________________________________")
					print(x)
					print(green + "𝗧𝗶𝗺𝗲 𝗦𝗲𝗻𝗱", time.localtime().tm_hour, time.localtime().tm_min,time.localtime().tm_sec)
					print(darkblue + "𝙂𝙐𝙄𝘿 𝙂𝘼𝙋:")
					print(group_guid)
					print("FORWARD:", sum)
					print(red + "\n_______________________________________________________")
					print("AVA ♡ ELIAS FOREVER")
					print(red + "\n_______________________________________________________")
					t:bool=True
					count+=5
				except:
					t:bool=False
					count+=1
			t:bool=False
			count:int=0
			limit:int=5
			while(count<5 and t!=True):
				try:
					await bot.leaveGroup(group_guid)
					t:bool=True
					count+=5
				except:
					t:bool=False
					count+=1

asyncio.run(main())
