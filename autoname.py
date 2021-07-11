import os
from datetime import datetime
import asyncio
from telethon.tl import functions
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.errors import FloodWaitError
import pytz

AUTO_NAME = os.environ.get("AUTO_NAME", None)
DDEL_TIME_OUT = 60
TZZ = os.environ.get("TIME_ZONE","Asia/Kolkata")

@ultroid_cmd(pattern="aname")
async def _(event):
    while True:    	        
        NT = datetime.now(pytz.timezone(TZZ))
        HM = NT.strftime("%H:%M")
        nnmel = f"{HM}"
        await event.reply(f"**Unknow_Name**: successfully set last name to {HM} {TZZ}\n Sleeping 60s........")
        await event.delete()


        
        try:
        	
            await bot(UpdateProfileRequest(  # pylint:disable=E0602
                last_name=nnmel
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DDEL_TIME_OUT)