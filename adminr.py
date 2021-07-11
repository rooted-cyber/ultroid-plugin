from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

@ultroid_cmd(pattern="ara ?(.*)")
async def adr(event):
  rank = event.pattern_match.group(1)
  r = ChatAdminRights(add_admins=False, invite_users=True, change_info=False)
  await event.client(EditAdminRequest(event.chat_id, reply.sender_id, r ,rank))