import os
import logging
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import ADMINS, LOG_CHANNEL, PICS, BOT_USERNAME
from Script import script
from plugins.users_api import get_user

@Client.on_message(filters.command(['start']) & filters.private)
async def start_command(bot: Client, message: Message):
    user_id = message.from_user.id
    await get_user(user_id) # Ensure user is in DB
    
    b1 = InlineKeyboardButton('👥 sᴜᴩᴩᴏʀᴛ ɢʀᴏᴜᴩ', url='https://t.me/+ezcJRKI_yQcwMjA9')
    b2 = InlineKeyboardButton('🎬 ᴜᴩᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ', url='https://t.me/+W0znQsN7HyAzNzU1')
    b3 = InlineKeyboardButton('❓ ʜᴇʟᴩ', callback_data='help')
    b4 = InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
    
    reply_markup = InlineKeyboardMarkup([[b1, b2], [b3, b4]])
    
    if PICS:
        try:
            await message.reply_photo(
                photo=PICS[0],
                caption=script.START_TXT.format(message.from_user.mention),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
        except Exception as e:
            logging.error(f"Error sending photo: {e}")
            await message.reply_text(
                text=script.START_TXT.format(message.from_user.mention),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
    else:
        await message.reply_text(
            text=script.START_TXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    await query.answer() # Stops the loading/clock icon instantly
    
    if query.data == "close_data":
        await query.message.delete()
        
    elif query.data == "about":
        buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('🔒 ᴄʟᴏsᴇ', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT.format((await client.get_me()).mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )
    
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('🔒 ᴄʟᴏsᴇ', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
            
    elif query.data == "start":
        b1 = InlineKeyboardButton('👥 sᴜᴩᴩᴏʀᴛ ɢʀᴏᴜᴩ', url='https://t.me/+ezcJRKI_yQcwMjA9')
        b2 = InlineKeyboardButton('🎬 ᴜᴩᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ', url='https://t.me/+W0znQsN7HyAzNzU1')
        
