import telebot
import random
import os
import http.client
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Use environment variables for sensitive information
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7585692002:AAHcYU6Ksn16t21kb3mF82-c3fO-N_5Yik0")
OWNER_ID = os.getenv("OWNER_ID", "7256617868")  # Replace with the actual owner ID
GROUP_1 = os.getenv("GROUP_1", "https://t.me/superyodha00")  # First group link
GROUP_2 = os.getenv("GROUP_2", "https://t.me/supar_yodha_X_army")  # Second group link
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "823ad731bemsh1a89f7cbcabd094p1f2447jsnad1907e6f3a1")  # RapidAPI key

bot = telebot.TeleBot(TOKEN)

# List of stylish font transformations
def fancy_text(text, style=1):
    fonts = [
        str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
                      "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏" 
                      "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝐽𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"),
        str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
                      "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝓊𝕧𝕨𝕩𝕪𝕫" 
                      "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"),
        str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
                      "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟" 
                      "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅"),
        str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
                      "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷" 
                      "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ"),
        str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
                      "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃" 
                      "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩")
    ]
    return text.translate(fonts[style])

# Emoji enhancement
def add_emojis(text):
    crown_emojis = ["👑", "🤴", "👸", "🏆", "🎗️", "💎", "🌟", "✨", "🔥", "🥇", "🏅", "👑✨", "👑🔥", "👑💎", "👑🌟", "👑🎀", "👑🎉", "👑💖", "👑💫", "👑😎", "CROWN"] * 50
    return random.choice(crown_emojis) + " " + text + " " + random.choice(crown_emojis)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    owner_button = InlineKeyboardButton("Owner", url=f"tg://user?id={OWNER_ID}")
    group1_button = InlineKeyboardButton("Join Group 1", url=GROUP_1)
    group2_button = InlineKeyboardButton("Join Group 2", url=GROUP_2)
    markup.add(owner_button, group1_button, group2_button)
    bot.send_message(message.chat.id, "Send me any text and I'll style it! Try /style YourText", reply_markup=markup)

@bot.message_handler(commands=['style'])
def style_message(message):
    user_id = message.from_user.id
    try:
        chat_member_1 = bot.get_chat_member(GROUP_1.split('/')[-1], user_id)
        chat_member_2 = bot.get_chat_member(GROUP_2.split('/')[-1], user_id)
        
        if chat_member_1.status not in ['member', 'administrator', 'creator'] or chat_member_2.status not in ['member', 'administrator', 'creator']:
            bot.reply_to(message, "You must join both groups to use this bot!", reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("Join Group 1", url=GROUP_1),
                InlineKeyboardButton("Join Group 2", url=GROUP_2)))
            return
    except Exception as e:
        bot.reply_to(message, "An error occurred while checking your group membership. Please try again later.")
        return
    
    text = message.text.replace("/style ", "")
    if not text:
        bot.reply_to(message, "Please provide text. Example: /style Hello")
        return
    
    styles = [fancy_text(text, i) for i in range(5)]
    styled_text = random.choice(styles)
    styled_text = add_emojis(styled_text)
    
    bot.reply_to(message, styled_text)

# New command to call the API
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
