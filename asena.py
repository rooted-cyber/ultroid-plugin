from telethon import events
@bot.on(events.NewMessage(pattern="asena", outgoing= True))
async def hi(event):
  await event.reply("""
**Repl site** : `https://repl.it/@phaticusthiccy/WhatsAsena-QR`

**Github** : `bash <(curl -L https://t.ly/qYqy)` or `apt update;apt install nodejs --fix-missing;pkg install git;git clone https://github.com/Quiec/WhatsAsena;cd WhatsAsena;npm install @adiwajshing/baileys;npm install chalk;node qr.js`

**Deploy link** : `https://github.com/phaticusthiccy/WhatsAsenaDuplicated`
""")