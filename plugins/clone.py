import re
from pymongo import MongoClient
from Script import script
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, DB_URI, DB_NAME

# Keep connection intact to avoid any import errors in main file
mongo_client = MongoClient(DB_URI)
mongo_db = mongo_client["cloned_vjbotz"]

@Client.on_message(filters.command("clone") & filters.private)
async def clone(client, message):
    # Completely disabled the clone feature and responded in Small Caps font
    return await message.reply_text("<b>⚠️ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴅɪsᴀʙʟᴇᴅ ʙʏ ᴀᴅᴍɪɴ !</b>")

@Client.on_message(filters.command("deletecloned") & filters.private)
async def delete_cloned_bot(client, message):
    # Completely disabled the delete clone feature as well
    return await message.reply_text("<b>⚠️ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴅɪsᴀʙʟᴇᴅ ʙʏ ᴀᴅᴍɪɴ !</b>")

async def restart_bots():
    # Kept fallback function empty so that bot won't crash on boot
    pass
    
