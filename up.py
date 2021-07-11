from telethon import events
@bot.on(events.NewMessage(pattern="up", outgoing= True, incoming=True))
async def hi(event):
  ab = await event.get_reply_message()
  await ab.download_media("files")

