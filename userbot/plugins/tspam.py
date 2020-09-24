import asyncio
import time

from asyncio import wait, sleep
from telethon import events
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.system import register

@register(outgoing=True, pattern="^.tspam (.*)")
async def tmeme(e):
     tspam = str(e.text[7:])
     message = tspam.replace(" ", "")
     for letter in message:
         await e.respond(letter)
     await e.delete()
