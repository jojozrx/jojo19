import asyncio
import os
import sys

from asyncio import get_event_loop_policy

from atexit import register
from pyrogram import idle
from pyrogram.errors import RPCError

from ubot import *


async def auto_restart():
    while not await asyncio.sleep(2600):
        def _():
            gas()
        register(_)
        sys.exit(0)
        

async def loader_user(user_id, _ubot):
    ubot_ = Ubot(**_ubot)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=90)
        await ubot_.join_chat("kynansupport")
        await ubot_.join_chat("PesulapTelegram")
    except RPCError:
        await remove_ubot(user_id)
        await rm_all(user_id)
        await rem_expired_date(user_id)
        for X in await get_chat(user_id):
            await remove_chat(user_id, X)
        print(f"✅ {user_id} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦")
    except:
        pass


async def main():
    tasks = [
        asyncio.create_task(loader_user(int(_ubot["name"]), _ubot))
        for _ubot in await get_userbots()
    ]
    await asyncio.gather(*tasks)
    
    await bot.start()
    await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots(), idle())


if __name__ == "__main__":
    #asyncio.get_event_loop().run_until_complete(main())
    #loop = asyncio.get_event_loop_policy().get_event_loop()
    #loop.run_until_complete(main())
    LOOP = asyncio.get_event_loop_policy().get_event_loop()
    LOOP.run_until_complete(main())
