from telethon.tl.types import InputMediaDice
from userbot.events import register
from random import randrange
from userbot import CMD_HELP

@register(outgoing=True, pattern="^.dice$")
async def _(event):
    if event.fwd_from:
        return
    input_str = print(randrange(7))
    await event.delete()
    r = await event.reply(file=InputMediaDice())
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice())
        except:
            pass

CMD_HELP.update({
"dice":
"Module to show a rolling dice with random number"
})
