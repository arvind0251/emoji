import telebot
import random
import http.client

# Bot token
TOKEN = "7585692002:AAHcYU6Ksn16t21kb3mF82-c3fO-N_5Yik0"

# RapidAPI Key
RAPIDAPI_KEY = "823ad731bemsh1a89f7cbcabd094p1f2447jsnad1907e6f3a1"

bot = telebot.TeleBot(TOKEN)

# Stylish text fonts
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
                      "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ")
    ]
    return text.translate(random.choice(fonts))

# 50 New Crown + Love + Fire + Stars + Diamonds Emoji Pack
def add_emojis(text):
    emoji_pack = [
        "👑💖", "💖👑", "👑🔥", "💎👑", "👑✨", "💖🎀", "👑💫", "👑🎉", "💖🥇", "👑😎",
        "🌟👑", "💖🌹", "👑👀", "🔥👑", "✨💖", "💎💖", "🎀👑", "👑💜", "👑🖤", "💖💫",
        "👑🌺", "💖🔥", "👑🎆", "🥇💖", "🌟🔥", "💖💎", "👑🎀", "💖💥", "🔥🥇", "💖🌠",
        "💖💗", "👑💞", "👑💖🌟", "🔥💎", "🎉👑", "💖👑✨", "🎆💖", "💖🔥💎", "👑💥", "🌠👑",
        "💎👑💖", "💖💡", "👑🎈", "👑💖🌹", "💖🕊", "💖👑💥", "👑💎🔥", "💖🌟✨", "🥇👑", "💖🚀"
    ]
    return random.choice(emoji_pack) + " " + text + " " + random.choice(emoji_pack)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Send any text and I'll style it! Try /style YourText")

@bot.message_handler(commands=['style'])
def style_message(message):
    text = message.text.replace("/style ", "")
    
    if not text:
        bot.reply_to(message, "Please provide text. Example: /style Hello")
        return
    
    styled_names = "\n".join([add_emojis(fancy_text(text)) for _ in range(30)])
    
    bot.reply_to(message, f"Here are your 30 stylish names:\n\n{styled_names}")

# RapidAPI se status check karne ka command
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
