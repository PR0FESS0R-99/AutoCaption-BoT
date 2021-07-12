# (C) PR0FESSOR-99

from pyrogram import filters
from pyrogram import Client, PAC_mt
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@PAC_mt.on_message(filters.private & filters.command("start"))
async def start(client, update):
    text = f"""<b> 👋Hello {update.from_user.mention}</b>"""
    reply_markup =  MT_START
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

@Mo_Tech_YT.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(client, update):
    buttons = [[
        InlineKeyboardButton("📃AutoFilter📃", url="t.me/mo_tech_yt")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=f"""<b> 👋Hello {update.from_user.mention}</b>"""
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

MT_START = InlineKeyboardMarkup(
     [[
        InlineKeyboardButton("🗣️Group", url=f"t.me/mo_tech_group"),
        InlineKeyboardButton("📑Bot List", url=f"t.me/mo_tech_yt")
     ]]
   )

@PAC_mt.on_callback_query(filters.regex(r"^(heroku|close)$"), group=2)
async def callback_data(client, update: CallbackQuery):

    query_data = update.data

    if query_data == "heroku":
        buttons = [[
            InlineKeyboardButton("🔻Click Here🔻", url="https://dashboard.heroku.com/")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            """Hy"",
            reply_markup=reply_markup,
            parse_mode="html"
        )


    elif query_data == "close":
        await update.message.delete()


