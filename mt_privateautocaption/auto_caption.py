import os
from config import Config

from pyrogram import filters
from pyrogram import Client, PAC_cs
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

CAPTION=Config.CAPTION

@PAC_cs.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    await message.edit(f"{message.file_name}\n\nCAPTION")
