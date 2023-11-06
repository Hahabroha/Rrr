from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
from pyshorteners import Shortener
import redis
import humanize
import random
from helper.txt import mr
from helper.database import db
from config import START_PIC, FLOOD, ADMIN 

Initialize Redis client
r = redis.StrictRedis(host='localhost', port=6379, db=0)

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    user_id = user.id

    if not r.get(f'verified:{user_id}'):
        # Generate a random verification code
        verification_code = random.randint(1000, 9999)

        # Generate a random shortened URL
        s = Shortener()
        full_url = "https://zxlink.in/jmezY1"  # Replace with the actual URL you want users to complete
        shortened_url = s.tinyurl.short(full_url)

        # Store the verification code and shortened URL in the database
        r.setex(f'verification_code:{user_id}', 600, verification_code)
        r.set(f'shortened_url:{user_id}', shortened_url)

        # Send the user a verification message with the shortened URL
        verification_message = (
            f"Please complete the following URL: {shortened_url}\n"
            f"Verification Code: {verification_code}"
        )
        await message.reply_text(verification_message)
    else:
        # User is verified, proceed with your code
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)             
    txt=f"👋 Hello Developer {user.mention} \n\nI am an Advance file Renamer and file Converter BOT with permanent and custom thumbnail support.\n\nSend me any video or document !"
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton('🚩 ᴜᴘᴅᴀᴛᴇꜱ 🚩', url='https://t.me/hdlinks4uu'),
        InlineKeyboardButton('📍 ᴏᴡɴᴇʀ 📍', url='https://t.me/badal6667rai')
        ],[
        InlineKeyboardButton('🔰 ᴀʙᴏᴜᴛ 🔰', callback_data='about'),
        InlineKeyboardButton('ℹ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ℹ', url='https://t.me/sourcebotcode/2')
        ]
        ])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)
    

@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"Error:\n`{e}`")

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""👋 Hello Developer {query.from_user.mention} \n\nI am an Advance file Renamer and file Converter BOT with permanent and custom thumbnail support.\n\nSend me any video or document !""",
            reply_markup=InlineKeyboardMarkup( [[
        InlineKeyboardButton('🚩 ᴜᴘᴅᴀᴛᴇꜱ 🚩', url='https://t.me/hdlinks4uu'),
        InlineKeyboardButton('📍 ᴏᴡɴᴇʀ 📍', url='https://t.me/badal6667rai')
        ],[
        InlineKeyboardButton('🔰 ᴀʙᴏᴜᴛ 🔰', callback_data='about'),
        InlineKeyboardButton('ℹ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ℹ', url='https://t.me/sourcebotcode/2')
        ]
        ]
                )
            )
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [
               [
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [
               [
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





