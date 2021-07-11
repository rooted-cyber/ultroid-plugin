# made by eris. for [ultroid]

""" 
✘ Commands Available -

• `{i}frwd <reply / text> `

  USE :
> Get eye icon (views) on any message 👁️
> Can be used to determine no. of active members in chat 👀

  CMD : {i}frwd (reply) | {i}frwd some_text
    U need to setup a pvt chnnl to use this.
"""

from asyncio import sleep

from . import *


@ultroid_cmd(pattern="frwd ?(.*)")
async def _(e):
    if e.fwd_from:
        return
    here = e.chat_id
    eris = await eor(e, "`. . .`")
    x = udB.get("FRWD_CHANNEL")
    if x == None:
        txt = "**Set a FRWD_CHANNEL to use this**\n\n"
        txt += "`Create a pvt Channel and get its id\n"
        txt += "Then save that id as :`\n`.setredis FRWD_CHANNEL (id)`"
        await eris.edit(txt)
        return
    else:
        try:
            entity = await ultroid_bot.get_entity(int(x))
        except Exception:
            txt = f"`Could not find entity for {x}\n"
            txt += "Kindly Re-check ur FRWD_CHANNEL`"
            await eris.edit(txt)
            return

        if e.is_reply:
            msg = await e.get_reply_message()
        else:
            args = e.pattern_match.group(1)
            if not args:
                await eris.edit("`Reply or give some text`")
                return
            msg = await eris.edit(args)

        frwd = await msg.forward_to(entity.id)
        await frwd.forward_to(here)
        await eris.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
