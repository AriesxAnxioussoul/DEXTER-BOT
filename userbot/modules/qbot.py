import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import register
from userbot import CMD_HELP

@register(outgoing=True, pattern=".qbot (.*)")
async def new_event(event):
    if event.fwd_from:
        return 
    await event.delete()
    reply_message = event.pattern_match.group(1)
    chat = "@QuotLyBot"
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await event.client.send_message(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock me (@QuotLyBot) u Nigga```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.client.send_message(event.chat_id, response.message)



CMD_HELP.update({
".": 
"A module to create a sticker from a text in reply\nWARNING : @Quotlybot should not be in the chat where you are using this plugin else it may cause errors !\nJust type .qbot and the message you wanna convert to sticklet"
})
