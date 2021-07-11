@ultroid_cmd(pattern="fullsudo")
async def _(e):
  a=""
  for m in await bot.get_participants(e.chat_id):
    if m.id == bot.me.id:
      pass
    else:
      a+=f"{m.id} "

  udB.append("SUDOS", a)
  udB.append("FULLSUDO", a)