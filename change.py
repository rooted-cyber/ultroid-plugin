@ultroid_cmd(pattern="cem ?(.*)",incoming=True,outgoing=True)
async def _(event):
  a = event.pattern_match.group(1)
  if not a:
    await event.edit("`Enter any emoji`")
    return
  await event.edit(f"ᥬ{a}᭄")


