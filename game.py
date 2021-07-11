from telethon import events
@bot.on(events.NewMessage(pattern="game", outgoing= True, incoming=True))
async def hi(event):
  for c in await bot.inline_query("inlinegamesbot"," a"):
    await c.click(event.chat_id)
    break