# Pyrogram 2021 -Hactoberfest

import os
import time
import asyncio
import pyrogram
from config import EFFECT, BOT_TOKEN, API_ID,API_HASH
from pyrogram import Client, Filters, Message, InlineKeyboardButton, InlineKeyboardMarkup

Leo = Client(
  bot_token=BOT_TOKEN,
  api_id=API_ID,
  api_hash=API_HASH
)

URL1="telegram.dog/XDgangs"
URL2="telegram.dog/Stopiracy"

@Leo.Client.on_message(pyrogram.Filters.document)
async def old(xequist, message):
    await xequist.edit_message_caption(
    chat_id=message.chat.id,
    message_id=message.message_id,
    caption=f"{filename}",
    caption=f_caption.replace(".mkv",EFFECT),
    caption=f_caption.replace(".mp4",EFFECT),
    caption=f_caption.replace(".avi",EFFECT),
    parse_mode="markdown", # html or none
    reply_markup=InlineKeyboardMarkup(
        [ 
            [
                [InlineKeyboardButton("🤖 Join Our Channel", url=URL1)]#,
               #[InlineKeyboardButton("🎧 Join our Group ", url=URL2)]
            ]
        ]
        )
    )
    
    
Leo.run()
