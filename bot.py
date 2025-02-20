import telebot
import random
import os
import http.client
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Use environment variables for security
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
OWNER_USERNAME = "@KAARTIK_NISHAD"  # Updated Owner Username
GROUP_1_ID = -1002117177980  # Updated Group 1 ID
GROUP_2_ID = -1002486097426  # Updated Group 2 ID
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY_HERE")

bot = telebot.TeleBot(TOKEN)

# 🎨 Stylish Font Generator
def fancy_text(text):
    fonts = [
        "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭",
        "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵",
        "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅",
        "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩",
        "𝔄𝔅ℭ𝔇𝔈𝔉𝔊𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷",
        "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
    ]
    chosen_font = random.choice(fonts)
    return ''.join([chosen_font[ord(c) - 65] if 'A' <= c <= 'Z' else c for c in text.upper()])

# 👑🔥 Crown Emoji Enhancer
def add_crown_emojis(text):
    crown_styles = [
        "👑✨", "🔥👑", "💎👑", "🏆👑", "🌟👑", "🥇👑", "👑🎗️", "👑🔥",
        "👑💖", "👑💫", "👑💎", "👑🎀", "👑⚡", "👑🔥💎", "👑🌟✨", "🏆💎👑",
        "🎗️👑", "🔥🏆👑", "💎👑🌟", "👑🥇🔥"
    ]
    return f"{random.choice(crown_styles)} {text} {random.choice(crown_styles)}"

# /start Command
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    owner_button = InlineKeyboardButton("Owner", url="https://t.me/KAARTIK_NISHAD")
    group1_button = InlineKeyboardButton("Join Group 1", url="https://t.me/superyodha00")
    group2_button = InlineKeyboardButton("Join Group 2", url="https://t.me/supar_yodha_X_army")

    markup.add(owner_button, group1_button, group2_button)
    bot.send_message(message.chat.id, "Send me any text and I'll style it! Try /style YourText", reply_markup=markup)

# /style Command
@bot.message_handler(commands=['style'])
def style_message(message):
    user_id = message.from_user.id

    try:
        chat_member_1 = bot.get_chat_member(GROUP_1_ID, user_id)
        chat_member_2 = bot.get_chat_member(GROUP_2_ID, user_id)

        if chat_member_1.status not in ['member', 'administrator', 'creator'] or chat_member_2.status not in ['member', 'administrator', 'creator']:
            bot.reply_to(message, "You must join both groups to use this bot!", reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("Join Group 1", url="https://t.me/superyodha00"),
                InlineKeyboardButton("Join Group 2", url="https://t.me/supar_yodha_X_army")))
            return
    except Exception as e:
        bot.reply_to(message, "Error checking group membership. Please try again.")
        return
    
    text = message.text.replace("/style ", "")
    if not text:
        bot.reply_to(message, "Please provide text. Example: /style Hello")
        return
    
    styled_text = fancy_text(text)
    styled_text = add_crown_emojis(styled_text)
    
    bot.reply_to(message, styled_text)

# /api Command
@bot.message_handler(commands=['api'])
def call_api(message):
    try:
        conn = http.client.HTTPSConnection("ofc.p.rapidapi.com")
        headers = {
            'x-rapidapi-key': RAPIDAPI_KEY,
            'x-rapidapi-host': "ofc.p.rapidapi.com"
        }
        conn.request("GET", "/status", headers=headers)
        res = conn.getresponse()
        data = res.read()
        bot.reply_to(message, f"API Response: {data.decode('utf-8')}")
    except Exception as e:
        bot.reply_to(message, f"Failed to call API: {str(e)}")

# Run bot
bot.polling()
