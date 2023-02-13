import telethon
import asyncio
import os, sys
import re
from telethon import TelegramClient, events
import random

API_ID =  27337131 #tu api id bb
API_HASH = '695a43d29e73423ad4142b20a736ea42'  #tu api hash bb
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
    '@alterchkchat',
    '@AssociatonBinners1',
    '@dSnowChat',
    '@RickPrimeChkFree',
    '@CHKBINS',
    '@bcycc',
    '@fbinschat',
    '@savagegroupoficial',
    '@CHECKEREstefany_bot',
    '@CuartelCardingGrupo'

]

PALABRAS_CLAVE = [
     "Approved",
     "APPROVED",
     "APPROVED ✅",
     "✅✅✅ Approved ✅✅✅",
     "Approved CCN",
     "Approved #AUTH! ✅",
     "Approved ❇️",
     "APPROVED ✅",
     "APPROVED ✓",
     "ccn",
     "✅Appr0ved",
     "Security code incorrect✅",
     "
     "CCN",
     "Approved ✅",
     
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
