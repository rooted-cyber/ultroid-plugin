from telethon import events

@bot.on(events.NewMessage(pattern="string", outgoing=True))
async def hi(event):
  await event.edit("""Here is the String session Generator: :
Bot link : @SessionGeneratorBot

Github link : https://github.com/rooted-cyber/string

Repl link : https://repl.it/@TeamUltroid/UltroidStringSession#main.py""")