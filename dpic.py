@ultroid_cmd(pattern="dpic ?(.*) (.*)")
async def hello(event):
  a = event.pattern_match.group(1)
  b = event.pattern_match.group(2)
  if not b:
    await event.edit("`Type : $dpic username anything`")
    return
  if not a:
    await event.edit("`Type : $dpic username anything`")
    return
  for c in await bot.inline_query(a, b):
    await c.click(event.chat_id)