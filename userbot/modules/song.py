# New Easy And Simple Module by @AyushChatterjee

from telethon import events
from telethon.errors import YouBlockedUserError
import asyncio
from userbot.events import register
from userbot import bot, CMD_HELP

@register(outgoing=True, pattern="^.song (.*)")
async def _(event):
    if event.fwd_from:
        return 
    reply_message = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    await event.edit("**searching song.....**")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=752979930))
              await bot.send_message(chat, reply_message)
              response = await response 
              await event.edit("**sending the song**")
          except YouBlockedUserError: 
              await event.reply("**plz unblock me @SpotifyMusicDownloaderBot u nigga**")
              return
          if response.text.startswith("Hello,"):
             await event.edit("**please disable your forward privacy settings**")
          elif response.text.startswith("Couldn't"):
             await event.edit("**could not find the song**")
          else: 
             await bot.send_file(event.chat_id, response.message.media)
CMD_HELP.update({
"song":
"Use this plugging to search for songs and sending the song to the chat group at the same time\nSyntax : `.song artist name[optional] songname`"
})
