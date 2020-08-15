import asyncio
import datetime
import time
from userbot import bot, CMD_HELP
from telethon.tl.functions.account import UpdateProfileRequest
from userbot.events import register
import pytz

@register(outgoing=True, pattern="^.autobio")
async def _(event):
    if event.fwd_from:
        return
    while True:
        LT = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        PT = LT.strftime("%d.%m.%y")
        OT = LT.strftime("%H:%M")
        name = f"Last seen at {PT} {OT}"
        await bot(UpdateProfileRequest(about=name))
        await asyncio.sleep(60)
        
CMD_HELP.update({
"autobio":
"A module to show a last seen timer in the userbio"
})
