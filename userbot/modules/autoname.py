import asyncio
import datetime
import time
from userbot import bot, CMD_HELP
from telethon.tl.functions.account import UpdateProfileRequest
from userbot.events import register
import pytz

@register(outgoing=True, pattern="^.autoname")
async def _(event):
    if event.fwd_from:
        return
    while True:
        LT = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        OT = LT.strftime("%H:%M")
        name = f"№𝙳𝚎𝚡𝚝𝚎𝚛[{OT}]~$"    
        await bot(UpdateProfileRequest(first_name=name))
        await asyncio.sleep(60)

CMD_HELP.update({
"autoname":
"A module to show a last seen timer in the userbio"
})
