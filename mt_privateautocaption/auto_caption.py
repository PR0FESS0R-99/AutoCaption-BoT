#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K & Pr0fess0r-99

import os
from config import Config

from pyrogram import filters
from pyrogram import Client, PAC_cs
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

FIXED_CAPTION=Config.CAPTION

@PAC_cs.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    kopp, _ = get_file_id(message)
    await message.edit(f"{kopp.file_name}\n\{FIXED_CAPTION}")


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                return obj, obj.file_id
