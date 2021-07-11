# "Made by eris. for Public Sudo"
# "Idea : Rooted-cyber"

from . import *


@ultroid_cmd(pattern="gibfullsudo ?(.*)")
async def _(e):
    if e.fwd_from:
        return
    x = ""
    args = e.pattern_match.group(1)
    eris = await eor(e, "`adding waimt...`")

    sudo = udB.get("SUDOS").split()
    fullsudo = udB.get("FULLSUDO").split()

    if "-g" in args:
        for m in await bot.get_participants(entity=e.chat_id, limit=None):
            if not (m.bot or m.deleted or m.is_self):
                if m in sudo or m in fullsudo:
                    pass               
                else:
                    x += f"{m.id} "
            else:
            	pass
        if len(x) == 0:
            await eris.edit("Zero users amdded,,, brah")
            return
        udB.append("FULLSUDO", x)
        udB.append("SUDOS", x)
        await eris.edit(f'`Added this group ({len(x.split(" "))} users) to fullsudo`')    

    elif e.is_reply:
        id = (await e.get_reply_message()).sender_id
        ids = await ultroid.get_entity(id)
        if id in fullsudo or id in sudo: 
            await eris.edit("`Already in Sudo`")
            return        
        elif ids.bot or ids.deleted or ids.is_self:
        	await eris.edit("`Nope cant add him..`")
        else:
            udB.append("SUDOS", f"{id} ")
            udB.append("FULLSUDO", f"{id} ")
            await eris.edit(f"Omk `{id}` has full sudo now")
    else:
        return await eris.edit("Reply to someone")
    