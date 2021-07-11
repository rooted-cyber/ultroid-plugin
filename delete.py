
import asyncio
@ultroid_cmd(pattern="del",incoming=True,outgoing=True)
async def hi(event):
  ab = await event.get_reply_message()
  if not ab:
    await event.edit("`Reply your message`")
    return
  await ab.delete()
  await event.edit("`Successfully delete message`")
  await asyncio.sleep(2)
  await event.delete()
