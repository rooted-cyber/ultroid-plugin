# " Ported to Ultroid by @e3ris "
# < https://github.com/TeamUltroid/Ultroid >
# Credits to Devs of @CatUserbot!


"""
✘ alts_paste_logs
-> Alternative to {i}paste and {i}logs command, Since both are dead rn.

✘ **CMD** :
-> `{i}ilogs <some_text/reply>`
-> `{i}ipaste <reply to file>`
"""

import os
import requests

from . import *


@ultroid_cmd(pattern="ilogs$")
async def lomgs(e):
	if e.fwd_from:
		return
	file = "ultroid_logs.txt"
	eris = await eor(e, "`...`")
	with open("ultroid.log", "r") as f:
		ulog = f.read()
		f.close()
	with open(file, "w") as ilog:
		ilog.write(ulog)

	try:
		send = await ultroid.send_file(e.chat_id, file)
	except Exception:
		return await eod(eris, "`Cant send file here!` 😬")
	finally:
		await eris.delete()

	try:
		with open(file, "r") as xfile:
			content = xfile.read()
	except Exception:
		return
	finally:
		os.remove(file)
	
	url = "https://spaceb.in/api/v1/documents/"
	try:
		request = requests.post(url, data={"content": content.encode("UTF-8"), "extension": "txt"}).json()
		url = f"https://spaceb.in/{request['payload']['id']}"
		await send.edit(
			f"Pasted [Here]({url}) as well!",
			link_preview=False,
		)
	except Exception:
		pass


@ultroid_cmd(pattern="ipaste ?(.*)")
async def ipaste(event):
    if event.fwd_from:
        return
    eris = await eor(event, "`pasting..`")
    input_str = event.pattern_match.group(1)
    message, ext = "", "txt"
    if event.is_reply:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await ultroid.download_media(
                previous_message,
            )
            ext = previous_message.file.ext.replace(".", "")
            message = ""
            try:
                with open(downloaded_file_name, "r") as f:
                    message = f.read()
                    f.close()
            except Exception as ex:
                return await eris.edit("`Error opening file`")
            finally:
                os.remove(downloaded_file_name)
        else:
            message = previous_message.text
    elif input_str:
        message = input_str
    else:
        return await eris.edit("`Reply to a file or give some text` 😛💁🏼‍♂️")
        
    url = "https://spaceb.in/api/v1/documents/"
    try:
        request = requests.post(url, data={"content": message.encode("UTF-8"), "extension": ext}).json()
        link = f"https://spaceb.in/{request['payload']['id']}"
        raw = f"{url}{request['payload']['id']}/raw"
        
        eris_ =  f"Pasted file to Space-B 🚀\n"
        eris_ += f"-> [Raw]({raw})  -> [Direct Link]({link})"
        await eris.edit(
            eris_,         
            link_preview=False,
        )
    except Exception as ex:
        return await eod(eris, f"`{ex}`")
        
        
HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
