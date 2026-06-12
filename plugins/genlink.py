import re
import os
import json
import base64
from pyrogram import filters, Client, enums
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, UsernameInvalid, UsernameNotModified
from config import ADMINS, LOG_CHANNEL, PUBLIC_FILE_STORE, WEBSITE_URL, WEBSITE_URL_MODE

async def allowed(_, __, message):
    if PUBLIC_FILE_STORE:
        return True
    if message.from_user and message.from_user.id in ADMINS:
        return True
    return False

@Client.on_message((filters.document | filters.video | filters.audio) & filters.private & filters.create(allowed))
async def incoming_gen_link(bot, message):
    username = (await bot.get_me()).username
    try:
        post = await message.copy(LOG_CHANNEL)
    except Exception as e:
        return await message.reply(f"<b>❌ ᴇʀʀᴏʀ: ʙᴏᴛ ɪs ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴄʜᴀɴɴᴇʟ ɪᴅ ɪs ᴡʀᴏɴɢ.\n\nᴅᴇᴛᴀɪʟs: {e}</b>")
        
    file_id = str(post.id)
    string = f"file_{file_id}"
    outstr = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
    
    if WEBSITE_URL_MODE == True:
        share_link = f"{WEBSITE_URL}?share={outstr}"
    else:
        share_link = f"https://t.me/{username}?start={outstr}"
        
    await message.reply(f"<b>⭕ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟɪɴᴋ:\n\n🔗 ᴏʀɪɢɪɴᴀʟ ʟɪɴᴋ :- {share_link}</b>")

@Client.on_message(filters.command(['link']) & filters.create(allowed))
async def gen_link_s(bot, message):
    username = (await bot.get_me()).username
    replied = message.reply_to_message
    if not replied:
        return await message.reply('<b>ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇᴛ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ.</b>')
    
    try:
        post = await replied.copy(LOG_CHANNEL)
    except Exception as e:
        return await message.reply(f"<b>❌ ᴇʀʀᴏʀ: ʙᴏᴛ ɪs ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.\n\nᴅᴇᴛᴀɪʟs: {e}</b>")
        
    file_id = str(post.id)
    string = f"file_{file_id}"
    outstr = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
    
    if WEBSITE_URL_MODE == True:
        share_link = f"{WEBSITE_URL}?share={outstr}"
    else:
        share_link = f"https://t.me/{username}?start={outstr}"
        
    await message.reply(f"<b>⭕ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟɪɴᴋ:\n\n🔗 ᴏʀɪɢɪɴᴀʟ ʟɪɴᴋ :- {share_link}</b>")

@Client.on_message(filters.command(['batch']) & filters.create(allowed))
async def gen_link_batch(bot, message):
    username = (await bot.get_me()).username
    if " " not in message.text:
        return await message.reply("<b>uꜱᴇ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ.\nᴇxᴀᴍᴘʟᴇ /batch ʜᴛᴛᴘs://ᴛ.ᴍᴇ/ᴄʜᴀᴛ/10 ʜᴛᴛᴘs://ᴛ.ᴍᴇ/ᴄʜᴀᴛ/20</b>")
    links = message.text.strip().split(" ")
    if len(links) != 3:
        return await message.reply("<b>u<b>sᴇ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ.\nᴇxᴀᴍᴘʟᴇ /batch ʜᴛᴛᴘs://ᴛ.ᴍᴇ/ᴄʜᴀᴛ/10 ʜᴛᴛᴘs://ᴛ.ᴍᴇ/ᴄʜᴀᴛ/20</b></b>")
    cmd, first, last = links
    regex = re.compile("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")
    match = regex.match(first)
    if not match:
        return await message.reply('<b>ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ</b>')
    f_chat_id = match.group(4)
    f_msg_id = int(match.group(5))
    if f_chat_id.isnumeric():
        f_chat_id = int(("-100" + f_chat_id))
    
    match = regex.match(last)
    if not match:
        return await message.reply('<b>ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ</b>')
    l_chat_id = match.group(4)
    l_msg_id = int(match.group(5))
    if l_chat_id.isnumeric():
        l_chat_id = int(("-100" + l_chat_id))

    if f_chat_id != l_chat_id:
        return await message.reply("<b>ᴄʜᴀᴛ ɪᴅs ɴᴏᴛ ᴍᴀᴛᴄʜᴇᴅ.</b>")
    try:
        chat_id = (await bot.get_chat(f_chat_id)).id
    except ChannelInvalid:
        return await message.reply('<b>ᴛʜɪs ᴍᴀʏ ʙᴇ ᴀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ / ɢʀᴏᴜᴘ. ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ ᴏᴠᴇʀ ᴛʜᴇʀᴇ ᴛᴏ ɪɴᴅᴇx ᴛʜᴇ ғɪʟᴇs.</b>')
    except (UsernameInvalid, UsernameNotModified):
        return await message.reply('<b>ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ sᴘᴇᴄɪғɪᴇᴅ.</b>')
    except Exception as e:
        return await message.reply(f'<b>ᴇʀʀᴏʀs - {e}</b>')
    
    sts = await message.reply("<b>🔺 ɢᴇɴᴇʀᴀᴛɪɴɢ ʟɪɴᴋ...</b>")
    FRMT = "<b>ɢᴇɴᴇʀᴀᴛɪɴɢ ʟɪɴᴋ...</b>\n\n<b>ᴛᴏᴛᴀʟ ᴍᴇssᴀɢᴇs:</b> {total}\n<b>ᴅᴏɴᴇ:</b> {current}\n<b>ʀᴇᴍᴀɪɴɪɴɢ:</b> {rem}\n<b>sᴛᴀᴛᴜs:</b> {sts}"

    outlist = []
    og_msg = 0
    tot = 0
    async for msg in bot.iter_messages(f_chat_id, l_msg_id, f_msg_id):
        tot += 1
        if og_msg % 20 == 0:
            try:
                await sts.edit(FRMT.format(total=l_msg_id-f_msg_id, current=tot, rem=((l_msg_id-f_msg_id) - tot), sts="sᴀᴠɪɴɢ ᴍᴇssᴀɢᴇs"))
            except:
                pass
        if msg.empty or msg.service:
            continue
        file = {
            "channel_id": f_chat_id,
            "msg_id": msg.id
        }
        og_msg += 1
        outlist.append(file)

    with open(f"batchmode_{message.from_user.id}.json", "w+") as out:
        json.dump(outlist, out)
    
    try:
        post = await bot.send_document(LOG_CHANNEL, f"batchmode_{message.from_user.id}.json", file_name="Batch.json", caption="⚠️ ʙᴀᴛᴄʜ ɢᴇɴᴇʀᴀᴛᴇᴅ ғᴏʀ ғɪʟᴇsᴛᴏʀᴇ.")
    except Exception as e:
        return await sts.edit(f"<b>❌ ᴇʀʀᴏʀ: ʙᴏᴛ ᴄᴀɴɴᴏᴛ sᴇɴᴅ ᴅᴏᴄᴜᴍᴇɴᴛ ᴛᴏ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.\n\nᴅᴇᴛᴀɪʟs: {e}</b>")
        
    os.remove(f"batchmode_{message.from_user.id}.json")
    string = str(post.id)
    file_id = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
    
    if WEBSITE_URL_MODE == True:
        share_link = f"{WEBSITE_URL}?share=BATCH-{file_id}"
    else:
        share_link = f"https://t.me/{username}?start=BATCH-{file_id}"
        
    await sts.edit(f"<b>⭕ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟɪɴᴋ:\n\nᴄᴏɴᴛᴀɪɴs `{og_msg}` ғɪʟᴇs.\n\n🔗 ᴏʀɪɢɪɴᴀʟ ʟɪɴᴋ :- {share_link}</b>")
    
