# Copyright (C) 2020 Ronald Alfianto.
# All rights reserved.

import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern=r'^.sauce(:? |$)(.*)?')
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
       await event.edit("`Reply to a pic, GIF, a sticker, or an image file with .sauce`")
       return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
       await event.edit("`Reply to a pic, GIF, a sticker, or an image file`")
       return
    chat = "@SauceNAObot"
    sender = reply_message.sender
    if sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing...```")
    async with bot.conversation(chat) as conv:
          await event.edit("```Pouring some sauce on it...```")
          await asyncio.sleep(3)
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=946852090))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @SauceNAObot and try again```")
              return
          else: 
             await event.edit(f"{response.message.message}")
             await event.delete()   
             await bot.forward_messages(event.chat_id, response.message)

CMD_HELP.update({
        "sauce": 
        ">`.sauce`"
        "\nUsage: Reply to a pic, GIF, a sticker, or an image file."
    })
