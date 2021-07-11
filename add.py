@ultroid_cmd(pattern="ad ?(.*)")
async def hello(event):
  ab = event.pattern_match.group(1)
  abc = await event.get_reply_message()
  if not abc:
    await event.edit("Reply any file !!!")
    return
  if not ab:
    await event.edit("Write anything..")
    return
  abb = abc.text
  await bot.send_message(event.chat_id,f"{abb} {ab}")