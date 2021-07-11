from telethon import events
@bot.on(events.NewMessage(pattern=".delete", outgoing= True, incoming=True))
async def hi(event):
  a = await event.get_reply_message()
  await a.delete()