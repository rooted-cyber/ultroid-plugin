# made by eris. for [ultroid]
# this plug fetches songs from [@deezer2drivebot]


"""
✘ Commands Available -

• {i}deezer <song name or reply>
  Get High quality Songs from Deezer,
    using `@deezer2drivebot`
   
eg: `{i}deezer Attention - Charlie Puth`
eg: `{i}deezer Teri ore ; 4`
   (will send 4th song!)   
"""

import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *

@ultroid_cmd(pattern="deezer ?(.*)")
async def deezer(e):
    if e.fwd_from:
        return
    here = e.chat_id
    args = e.pattern_match.group(1)
    if not args:
        reply = await e.get_reply_message()
        if not reply:
            return await eod(e, "`Giving song name when? 🙁`", time=5)
        else:
            args = str(reply.text)
    f1 = await eor(e, "`. . .`")
    if ";" in args:
        strimg = args.split(";", 2)   
        args = str(strimg[0].strip())
        try:
            skip_ = int(strimg[1].strip())
            skip = skip_ - 1
        except ValueError:
            return await eod(f1, "`skip needs number ree 🤷🏻‍♀️`", time=5)
    else:
        skip = int("0")
        args = args.strip()
     #  values done.
    chat = await ultroid_bot.get_entity("deezer2drivebot")

    chk = udB.get("DEEZER")
    if chk != "True":
        await f1.edit("**Setting up bot cz first time user 🌝**")
        async with ultroid_bot.conversation(chat.username) as conv:
            try:
                await conv.send_message('/start')
                await conv.get_response()
                await asyncio.sleep(3)

                await conv.send_message('/settings')
                reply_ = await conv.get_response()
                await reply_.click(1)
                await asyncio.sleep(1.2)

                idk = (await ultroid_bot.get_messages(chat.id, limit=1))[0]
                await idk.click(text='Telegram')
                udB.set("DEEZER", "True")
                await f1.edit("__Setup Done! Run the CMD again!__")

            except YouBlockedUserError:
                await f1.edit(f'`Unblock @{chat.username} first`')
            except Exception:
#               await ultroid_bot.send_message(Var.LOG_CHANNEL, reply_.text)
                await f1.edit("`Error 😶`")
    else:
        results = await ultroid_bot.inline_query(chat.username, args)
        await asyncio.sleep(1)
        if len(results) == 0:
            return await eod(f1, f'No results for: `{args}`', time=6)
        else:
            await f1.edit("__got the song, sending in a bit...__")
            async with ultroid_bot.conversation(chat.username) as conv:
                try:
                    response = conv.wait_event(
                        events.NewMessage(incoming=True, from_users=chat.id, func=lambda a: a.audio)
                    )
                    try:
                        message = await results[skip].click(
                            chat.id,
                            silent=True,
                            hide_via=True,
                        )
                    except IndexError:
                        return await eod(f1, f'`Wrong skip value sir, pls chk`', time=5)
                    response = await response
                except YouBlockedUserError:
                    return await eod(f1, f'`Unblock @{chat.username} first`', time=8)
                except asyncio.TimeoutError:
                    return await f1.edit("`Bot didn't respond in time`")
                file_ = response.message
                size = humanbytes(file_.file.size)
                await ultroid_bot.send_file(here, file_, caption=f'🎶 [`{size}`] 🎶')
                await f1.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})

        