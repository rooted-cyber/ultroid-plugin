# made by eris. for [ultroid]
# This plugin uses @ stickerizerbot,
# to send stickers

"""
✘ **USE :**
> Send stickers with your own text :)

✘ **Commands Available :**
> `{i}sz some_text`
> `{i}sz (-r / -s / -t)* text` 
         *(optional)
"""

import random
import emoji
import re

from . import *

def remove_emoji(string):
    return emoji.get_emoji_regexp().sub(u'', string)
    # bot hates emojis. "press F"

@ultroid_cmd(pattern=f"sz ?(.*)")
async def stickerizer(e):
    if e.fwd_from:
        return
    eris = await eor(e, "`...`")
    args = e.pattern_match.group(1)
    if not args:
        await eod(eris, "`huehue give sum text, master` 🤡")
        return
    await eris.delete()
    args = str((remove_emoji(args)).strip())
    code_ = random.randint(1, 23)
    if "-t" in args:  # for colourful text
        args = f'&{code_}{args.replace("-t", "")}'        
    elif "-r" in args:  # for rounded bgs
        args = f'*{code_}{args.replace("-r", "")}'
    elif "-s" in args:  # special (meme) type
        args = f'#{code_}{args.replace("-s", "")}'
    else:
        selector = random.randint(1, 2)
        if selector == 1:
            args_ = "$"
            code_ = random.randint(1, 39)
        else:
            args_ = "#"
            code_ = random.randint(1, 66)
        args = f"{args_}{code_}{args}"

    stick_inline = await ultroid_bot.inline_query(
        "stickerizerbot", 
        args,
    )

    to_fwd = await stick_inline[0].click("me", silent=True)
    await ultroid_bot.send_file(
        e.chat_id,
        to_fwd,
        reply_to = e.reply_to_msg_id if e.is_reply else None,
        silent = False,
    )
    await to_fwd.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
