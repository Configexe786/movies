import asyncio
from pyrogram import Client, filters
from pyrogram.types import *

# Tumhara Database Channel ID
CHANNEL_ID = -1003284007507

@Client.on_message(filters.channel & filters.media)
async def add_button(client, message):
    if message.chat.id == CHANNEL_ID:
        # Tumhara Movie Group Link
        button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔰𝗠𝗼𝘃𝗶𝗲 𝗦𝗲𝗮𝗿𝗰𝗵 𝗚𝗿𝗼𝘂𝗽🔰", url="https://t.me/NetflirtMovieGroup")]]
        )
        
        try:
            # Message par button add karne ke liye
            await message.edit_reply_markup(reply_markup=button)
            await asyncio.sleep(0.5)  # Rapid messages handle karne ke liye delay
        except Exception as e:
            print(f"Failed to add button: {e}")
            
