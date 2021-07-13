# MoTech Botzz

import os
import logging
import pyrogram
from config import Config  


if __name__ == "__main__" :
    mt_privateautocaption = dict(
        root="mt_privateautocaption"
    )
    MoTech = pyrogram.Client(
        "CaptionBot",
        bot_token=Config.MT_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        mt_privateautocaption=mt_privateautocaption,
        workers=300
    )
    MoTech.run()
