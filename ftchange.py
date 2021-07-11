@ultroid_cmd(pattern="ftc ?(.*)",incoming=True,outgoing=True)
async def hello(event):
  ab = event.pattern_match.group(1)
  abc = await event.get_reply_message()
  if not abc:
    await event.edit("`Reply any file !!!`")
    return
  if not ab:
    await event.edit("`Write anything..`")
    return
  await bot.send_message(event.chat_id,ab,file=abc)

