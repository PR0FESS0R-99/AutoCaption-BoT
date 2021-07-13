

# (C) PR0FESSOR-99

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

BOT_USERNAME = "demo2022Bot"

@Client.on_message(filters.private & filters.command("start"))
async def start(client, update):
    text = f"""<b> 👋Hello {update.from_user.mention}\n\nI am an AutoCaption bot\n\nAll you have to do is add me to your channel and I will show you my power\n\nFor more info check help Button</b>"""
    reply_markup =  InlineKeyboardMarkup(
                                         [[
        InlineKeyboardButton("help↗️", callback_data="heroku"),
        InlineKeyboardButton("🗣️Group", url="t.me/mo_tech_Group"),
        InlineKeyboardButton("Channel📢", url="t.me/mo_tech_yt")
        ]]
    )
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

@Client.on_callback_query(filters.regex(r"^(heroku|motech)$"))
async def callback_data(client, update: CallbackQuery):

    query_data = update.data

    if query_data == "heroku":
        buttons = [[
            InlineKeyboardButton("🖥️ Tutorial Video 🖥️", url="https://dashboard.heroku.com/")
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{BOT_USERNAME}?start=start"),
            InlineKeyboardButton("❌️Close", callback_data="motech")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            """<b>AutoCaption Bot\n\nTake a look at the end of the video\nIt has to say\n\nYoutube Tutorial Video\n\nHeroku 👉 https://dashboard.heroku.com/\n\n© @Mo_Tech_YT</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "motech":
        await update.message.delete()
