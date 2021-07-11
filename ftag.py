import asyncio
@ultroid_cmd(pattern="ftag", outgoing= True, incoming=True)
async def hi(event):
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("Please reply message")
    return
  await event.edit("Processing..")
  await asyncio.sleep(1)
  await ab.forward_to(event.chat_id)



@ultroid_cmd(pattern="rtag")
async def hlo(event):
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("Please reply message")
    return
  await event.edit("Processing..")
  await asyncio.sleep(1)
  await ab.reply(ab)


