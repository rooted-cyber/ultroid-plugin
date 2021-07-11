# made by eris. for [ultroid]
# Thanks to @ AlPacinoDump
# This plugin uses [ Backup of APD channel ]
# to fetch Movies.

"""
✘ **USE :**
• Get Movies Easily with one CMD :)
• Its not 100% perfect, use some 🧠

✘ **Commands Available :**
• `{i}movie <some_text>`
• `{i}check_movie <some_text>
    *Always check before Sending :)
"""


from asyncio import sleep
from telethon.tl.types import InputMessagesFilterVideo as Video
from telethon.errors import ChannelInvalidError, ChannelPrivateError

from . import *


@ultroid_cmd(pattern="movie ?(.*)")
async def apd_get_movie(event):
    if event.fwd_from:
        return
    here, skip = event.chat_id, 0
    chat = -1001233287542
    skip_error = "`Skip Value should be a Number,`\n"
    skip_error += "correct format: `{HNDLR}movie Interstellar ; 3`"
    not_joined_error = "You haven't joined the channel yet"
    not_joined_error += "Click [Here](https://t.me/joinchat/2mDXUO6PU0Q5OGUx) to join"
    # if Link's dead, msg @e3ris 🚶🤡🚶
    args = event.pattern_match.group(1)
    if not args:
        if not event.is_reply:
            await eor(event, "`Gib a Movie name, peru...` 🙆")
            return
        else:
            args = str((await event.get_reply_message()).message)
    eris = await eor(event, f"`Searching for {args}`")

    if ";" in args:
        split = args.split(";", 2)
        args = split[0].strip()
        try:
            skip = int(split[1].strip())
            if skip > 20:
                return await eris.edit("Woah, too mach stress, me nu work")
        except ValueError:
            return await eris.edit(skip_error)
    try:
        total_result = ((await ultroid_bot.get_messages(
                           chat, search=args, filter=Video,
                           )).total
                       )
    except ChannelPrivateError:
        return await eris.edit(f"{not_joined_error}", link_preview=False)
    except Exception as ex:
        return await eris.edit(f"Error: `{ex}`")
    if total_result == 0:
        return await eod(eris, f"**No results found for** :\n `{args}`", time=6)
    await eris.edit(
        f"**Found {total_result} results for**\n `{args}`",
    )
    try:
        movie = await ultroid_bot.get_messages(
                    chat, search=args, filter=Video, limit=20, reverse=True,
                )      
        await ultroid_bot.send_file(
            here,
            movie[(skip+1)],
            caption=str(movie[skip].text),
        )
    except Exception as ex:
        await eris.edit(f"Error: `{ex}`")
        return
    await sleep(5)
    await eris.delete()


@ultroid_cmd(pattern="check_movie ?(.*)")
async def check_movie(e):
    if e.fwd_from:
        return
    here, chat, c = e.chat_id, -1001233287542, 1
    args = e.pattern_match.group(1)
    if not args:
        await eor(e, "`Wen giving args, senpai`")
        return
    eris = await eor(e, "`Processing...`")
    file_names = f"**Result for queries {args}** :\n\n"
    try:
        msgs = await ultroid_bot.get_messages(
                   chat, search=args, filter=Video, limit=18, reverse=True,
               )
    except ChannelPrivateError:
        await eris.edit(f"Error. Pls Do `{HNDLR}movie Barfi` for Help.")
        return
    except Exception as ex:
        return await eris.edit(f"Error: `{ex}`")
    if msgs.total == 0:
        return await eod(eris, f"**No results for**:\n`{args}`", time=6)

    for msg in msgs:
        fn = msg.text.split("\n", 1)[0]
        file_names += f"{c}: {fn}\n"
        c += 1
    await eris.edit(file_names)

    

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
