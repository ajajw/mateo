import telethon
import asyncio
import os, sys
import re
from telethon import TelegramClient, events
import random

API_ID =  20597671 #tu api id bb
API_HASH = 'e89f2c4056dd402bef8299bce660cbcd'  #tu api hash bb
SEND_CHAT = -1001784544888 #chat o canal donde quieres que se envien las ccs

client = TelegramClient('session', API_ID, API_HASH)

chats  = [
    '@alvkslspqpqpqoqqq',  #chats para scrapear
    '@CCAUTH',
    '@BinsHellChat',
    '@secretgroup01',
    '@BinSkillerChat',
    '@Venexchk',
    '@leonbinerss',
    '@RemChatChk',
    '@ComunidadGOATchat',
    '@alterchkchat'
    
]

PALABRAS_CLAVE = [
     "Approved",
     "APPROVED"
]
@client.on(events.MessageEdited(chats=chats))
async def new_order(event):
     try:
          print(PALABRAS_CLAVE)
          contain_palabra_clave = False

          for palabra_clave in PALABRAS_CLAVE:
              if palabra_clave in event.message.message:
                    contain_palabra_clave = True

          if contain_palabra_clave:
             await client.send_message(SEND_CHAT, event.message)



     except Exception as ex:
            print(f'Exception: {ex}')


client.start()
client.run_until_disconnected()