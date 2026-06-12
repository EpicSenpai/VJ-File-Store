class script(object):
    START_TXT = """<b><blockquote> ›› ʜᴇʏ {} × </blockquote>

ɪ ᴀᴍ ᴀ ᴘᴇʀᴍᴇɴᴀɴᴛ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴀɴᴅ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss sᴛᴏʀᴇᴅ ᴍᴇssᴀɢᴇs ʙʏ ᴜsɪɴɢ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ɢɪᴠᴇɴ ʙʏ ᴍᴇ.</b>"""

    CAPTION = """<b>📂 ғɪʟᴇɴᴀᴍᴇ : {file_name}

⚙️ sɪᴢᴇ : {file_size}

ᴊᴏɪɴ [ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ](https://t.me/+W0znQsN7HyAzNzU1)</b>""" 

    SHORTENER_API_MESSAGE = """<b>ᴛᴏ ᴀᴅᴅ ᴏʀ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ᴀᴘɪ, /api (ᴀᴘɪ)
            
<b>ᴇx: /api 𝟼ʟᴢǫ𝟾𝟻𝟷sxᴏғғғᴘʜᴜɢɪᴋǫǫ

<b>ᴄᴜʀʀᴇɴᴛ ᴡᴇʙsɪᴛᴇ: {base_site}

ᴄᴜʀʀᴇɴᴛ sʜᴏʀᴛᴇɴᴇʀ ᴀᴘɪ:</b> `{shortener_api}`

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀᴘɪ ᴛʜᴇɴ ᴄᴏᴘʏ ᴛʜɪs ᴀɴᴅ sᴇɴᴅ ᴛᴏ ʙᴏᴛ - `/api None`</b>"""

    ABOUT_TXT = """<b>ʜɪ ɪ ᴀᴍ ᴘPERMANENT ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴜʀʟ sʜᴏʀᴛɴᴇʀ sᴜᴘᴘᴏʀᴛ ᴀɴᴅ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ғᴇᴀᴛᴜʀᴇ.

🤖 ᴍʏ ɴᴀᴍᴇ: {}

📝 ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>𝐏𝐲𝐭𝐡𝐨𝐧𝟑</a>

📚 ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ: <a href=https://t.me/+ezcJRKI_yQcwMjA9>sᴜᴘᴘᴏʀᴛ</a>

📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ: <a href=https://t.me/+W0znQsN7HyAzNzU1>ᴜᴘᴅᴀᴛᴇs</a></b>
"""

    HELP_TXT = """<b><u>💢 ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ ☺️</u>

🔻 /link - ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴏʀ ғɪʟᴇ ᴛᴏ ɢᴇᴛ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ

🔻 /batch - sᴇɴᴅ ғɪʀsᴛ ʟɪɴᴋ ᴏғ ғɪʟᴇ sᴛᴏʀᴇ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛ ᴛʜᴇɴ ʟᴀsᴛ ᴘᴏsᴛ ʟɪɴᴋ ᴀɴᴅ ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ғɪʟᴇ sᴛᴏʀᴇ ᴄʜᴀɴɴᴇʟ.
ᴇx - /batch ʜᴛᴛᴘs://ᴛ.ᴍᴇ/ᴄʜᴀᴛ/25 ʜᴛᴛᴘs://ᴛ.ᴍᴇ/ᴄʜᴀᴛ/30

🔻 /base_site - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴ裝 ᴛᴏ sᴇᴛ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ʟɪɴᴋ ᴅᴏᴍᴀɪɴ 
ᴇx - /base_site ʏᴏᴜʀᴅᴏᴍᴀɪɴ.ᴄᴏᴍ

🔻 /api - sᴇᴛ ʏᴏᴜʀ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴀᴘɪ 
ᴇx - /api ʙᴀᴏᴡɢᴡᴋʟᴀᴀʙᴀᴋʟ

🔻 /broadcast - ʀᴇᴘʟʏ ᴛᴏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ (ʙᴏᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</b>"""

    LOG_TEXT = """<b>#ɴᴇᴡᴜsᴇʀ
    
ɪᴅ - <code>{}</code>

ɴᴀᴍᴇ - {}</b>
"""
    RESTART_TXT = """
<b>ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ !

📅 ᴅᴀᴛᴇ : <code>{}</code>
⏰ ᴛɪᴍᴇ : <code>{}</code>
🌐 ᴛɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ ʙᴜɪʟᴅ sᴛᴀᴛᴜs: <code>v2.7.1 [ sᴛᴀʙʟᴇ ]</code></b>"""
    
