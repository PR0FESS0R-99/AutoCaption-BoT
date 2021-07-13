# Mo Tech YT

import os
import logging
import pyrogram
from config import Config  


if __name__ == "__main__" :
    plugins = dict(
        root="mt_privateautocaption"
    )
    MoTech = pyrogram.Client(
        "CaptionBot",
        bot_token=Config.MT_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    MoTech.run()
