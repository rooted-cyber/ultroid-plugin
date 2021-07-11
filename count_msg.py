@ultroid_cmd(pattern="ctt ?(.*)", outgoing= True, incoming=True)
async def hi(event):
  text = event.pattern_match.group(1)
  if not text:
    await event.edit("`Enter group name !! `")
    return
  ab = await bot.get_messages(text)
  await event.reply(f"This {text} group total messages : {ab.total}")