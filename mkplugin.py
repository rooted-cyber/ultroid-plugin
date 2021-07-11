from telethon import *
@bot.on(events.NewMessage(pattern="plugins",outgoing= True, incoming=True))
async def hi(event):
  await event.reply("""
`from telethon import events
@bot.on(events.NewMessage(pattern=".", outgoing= True, incoming=True))
async def hi(event):`

`@ultroid_cmd(pattern="")
async def hello(event):`
""")