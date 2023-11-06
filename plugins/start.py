from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random

# Replace this with your actual URL
SHORTENED_URL = "https://short.url.com"
VERIFICATION_CODE = random.randint(1000, 9999)

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    user_id = user.id
    user_data = {}  # Store user-specific data

    # Check if the user is verified
    if not user_data.get(user_id, {}).get('verified', False):
        verification_message = f"Please complete the following URL to verify your account:\n{SHORTENED_URL}\nVerification Code: {VERIFICATION_CODE}"
        await message.reply_text(verification_message)
    else:
        # User is verified, proceed with your code
        txt = f"👋 Hello Developer {user.mention}\n\nI am an Advance file Renamer and file Converter BOT with permanent and custom thumbnail support.\n\nSend me any video or document!"
        button = InlineKeyboardMarkup([[
            InlineKeyboardButton('🚩 ᴜᴘᴅᴀᴛᴇꜳ 🚩', url='https://t.me/hdlinks4uu'),
            InlineKeyboardButton('📍 ᴏᴡɴᴇʀ 📍', url='https://t.me/badal6667rai')
        ], [
            InlineKeyboardButton('🔰 ᴀʙᴏᴜᴛ 🔰', callback_data='about'),
            InlineKeyboardButton('ℹ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ℹ', url='https://t.me/sourcebotcode/2')
        ])

        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)

@Client.on_message(filters.private & filters.text)
async def verify_user(client, message):
    user = message.from_user
    user_id = user.id
    user_data = {}  # Retrieve user-specific data

    # Check if the user is trying to complete the verification
    text = message.text.strip()
    if text == SHORTENED_URL:
        user_verification_code = user_data.get(user_id, {}).get('verification_code')
        if text.isdigit() and int(text) == user_verification_code:
            # Mark the user as verified
            user_data[user_id] = {'verified': True}
            await message.reply_text("You are now verified! You can use the bot.")
        else:
            await message.reply_text("Verification code is incorrect. Please try again.")
    else:
        await message.reply_text("Please complete the shortened URL correctly to verify your account.")

@Client.on_message(filters.private & filters.command(["shorten"]))
async def shorten_url(client, message):
    user = message.from_user
    user_id = user.id
    user_data = {}  # Retrieve user-specific data

    # Check if the user is verified
    if not user_data.get(user_id, {}).get('verified', False):
        await message.reply_text("Please verify your account first to use the URL shortener.")
    else:
        if len(message.text.split()) == 1:
            await message.reply_text("Please provide a URL to shorten.")
        else:
            url_to_shorten = message.text.split(maxsplit=1)[1]

            # Add your URL shortening logic here
            # s = Shortener()
            # shortened_url = s.tinyurl.short(url_to_shorten)

            # For demonstration, we'll use a placeholder shortened URL
            shortened_url = "https://shortened.url/abcd123"
            await message.reply_text(f"Shortened URL: {shortened_url}")

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    if data == "start":
        # Your start callback logic
        pass
    elif data == "about":
        # Your about callback logic
        pass
    elif data == "close":
        # Your close callback logic
        pass
        @Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"Error:\n{e}")

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    try:
        text = f"""What do you want me to do with this file.?\n\nFile Name :- {filename}\n\nFile Size :- {filesize}"""
        buttons = [[InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename")],
                   [InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel")]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep


