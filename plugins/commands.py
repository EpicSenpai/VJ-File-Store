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
    try:
        await get_user(user_id) # Ensure user setup
    except:
        pass
    
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
    await query.answer()
    
    if query.data == "close_data":
        await query.message.delete()
        
    elif query.data == "about":
        buttons = [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('🔒 ᴄʟᴏsᴇ', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.message.delete()
        except:
            pass
        await client.send_message(
            chat_id=query.message.chat.id,
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
        try:
            await query.message.delete()
        except:
            pass
        await client.send_message(
            chat_id=query.message.chat.id,
            text=script.HELP_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
            
    elif query.data == "start":
        b1 = InlineKeyboardButton('👥 sᴜᴩᴩᴏʀᴛ ɢʀᴏᴜᴩ', url='https://t.me/+ezcJRKI_yQcwMjA9')
        b2 = InlineKeyboardButton('🎬 ᴜᴩᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ', url='https://t.me/+W0znQsN7HyAzNzU1')
        b3 = InlineKeyboardButton('❓ ʜᴇʟᴩ', callback_data='help')
        b4 = InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
        reply_markup = InlineKeyboardMarkup([[b1, b2], [b3, b4]])
        try:
            await query.message.delete()
        except:
            pass
        if PICS:
            await client.send_photo(
                chat_id=query.message.chat.id,
                photo=PICS[0],
                caption=script.START_TXT.format(query.from_user.mention),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
        else:
            await client.send_message(
                chat_id=query.message.chat.id,
                text=script.START_TXT.format(query.from_user.mention),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
            
