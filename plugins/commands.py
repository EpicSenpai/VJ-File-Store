# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import logging
import random
import asyncio
from validators import domain
from Script import script
from plugins.dbusers import db
from pyrogram import Client, filters, enums
from plugins.users_api import get_user, update_user_info
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import *
from utils import verify_user, check_token, check_verification, get_token
from config import *
import re
import json
import base64
from urllib.parse import quote_plus
from TechVJ.utils.file_properties import get_name, get_hash, get_media_file_size
logger = logging.getLogger(__name__)

BATCH_FILES = {}

def get_size(size):
    """Get size in readable format"""
    units = ["ʙʏᴛᴇs", "ᴋʙ", "ᴍʙ", "ɢʙ", "ᴛʙ", "ᴘʙ", "ᴇʙ"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

def formate_file_name(file_name):
    chars = ["[", "]", "(", ")"]
    for c in chars:
        file_name.replace(c, "")
    clean_words = filter(lambda x: not x.startswith('http') and not x.startswith('@') and not x.startswith('www.'), file_name.split())
    return '@ᴠᴊ_ʙᴏᴛᴢ ' + ' '.join(clean_words)

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    username = client.me.username
    if not await db.is_user_exist(message.from_user.id):
        try:
            await db.add_user(message.from_user.id, message.from_user.first_name)
            await client.send_message(LOG_CHANNEL, f"#ɴᴇᴡᴜsᴇʀ\nɪᴅ: <code>{message.from_user.id}</code>")
        except:
            pass

    if len(message.command) != 2:
        b1 = InlineKeyboardButton('👥 sᴜᴩᴩᴏʀᴛ ɢʀᴏᴜᴩ', url='https://t.me/+ezcJRKI_yQcwMjA9')
        b2 = InlineKeyboardButton('🎬 ᴜᴩᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ', url='https://t.me/+W0znQsN7HyAzNzU1')
        b3 = InlineKeyboardButton('❓ ʜᴇʟᴩ', callback_data='help')
        b4 = InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
        
        buttons = [[b1, b2], [b3, b4]]
        reply_markup = InlineKeyboardMarkup(buttons)
        me = client.me
        
        try:
            caption_text = script.START_TXT.format(message.from_user.mention, me.mention)
        except:
            caption_text = f"<b>ʜᴇʟʟᴏ {message.from_user.mention} 👋,\n\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴡᴀɢᴜʀɪ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ! ❤️\n\nsᴇɴᴅ ᴍᴇ ᴀɴʏ ʟɪɴᴋ ᴏʀ ғɪʟᴇ ᴛᴏ ɢᴇᴛ sᴛᴀʀᴛᴇᴅ.</b>"

        try:
            return await message.reply_photo(
                photo=random.choice(PICS),
                caption=caption_text,
                reply_markup=reply_markup
            )
        except:
            return await message.reply_text(
                text=caption_text,
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )

    data = message.command[1]
    try:
        pre, file_id = data.split('_', 1)
    except:
        file_id = data
        pre = ""
        
    if data.split("-", 1)[0] == "verify":
        userid = data.split("-", 2)[1]
        token = data.split("-", 3)[2]
        
