from telethon import events
@bot.on(events.NewMessage(pattern="plugin", outgoing= True))
async def hi(event):
  await event.reply("""
`from telethon import events
@bot.on(events.NewMessage(pattern="", outgoing= True))
async def hi(event):`

`from userbot.utils import admin_cmd
@bot.on(admin_cmd(pattern=""))
async def hi(event):`

`@ultroid_cmd(pattern="")
async def hi(event):`
""")

