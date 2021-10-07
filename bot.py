import os
import requests as re
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

TOKEN = os.environ.get("TOKEN", "2035040893:AAF_cDCfMmq-rSlgedcG_IvafW5AiSXLe90")

API_ID = int(os.environ.get("API_ID", 6021226))

API_HASH = os.environ.get("API_HASH", "7c6dd7679f9dc0ab599f336de13cedf1")

app = Client(
        "webscrap",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
    )
    
    
@app.on_message(filters.command(['start']))
def start(client, message):
            message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n **Iam Simple web scraper** ðŸ•¸ \n __SEND ME WEBSITE LINK AND GET THAT WEB SOURCE__",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Suppyt" ,url="https://t.me/lntechnical") ],
                 [InlineKeyboardButton("Subbilfy", url="https://youtube.com/c/LNtechnical") ]          ]        ) )

@app.on_message(filters.command(['help']))
def start(client, message):
            message.reply_text(text =f"Hello **what bn** \n\n **Iam Simple webper** ðŸ•¸ \n __SEND ME WEBSITE LINK AND GET THAT WEB SOURCE__",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support" ,url="https://t.me/lntechnical") ],
                 [InlineKeyboardButton("Subscribe", url="https://youtube.com/c/LNtechnical") ]          ]        ) )
                 
                 
app.run()
