import telebot
import random
import http.client

# 🔴 Directly Add Your Keys Here
BOT_TOKEN = "7585692002:AAHcYU6Ksn16t21kb3mF82-c3fO-N_5Yik0"
RAPIDAPI_KEY = "823ad731bemsh1a89f7cbcabd094p1f2447jsnad1907e6f3a1"

bot = telebot.TeleBot(BOT_TOKEN)

# Stylish separators
stylish_separators = [
    "⟆♡̷̷̷⟅ {name} ⟆♡̷̷̷⟅", "𓆩⟡𓆪 {name} 𓆩⟡𓆪", "𓆫❦꯭𓆩 {name} 𓆩꯭❦𓆫",
    "⟆💠⟅ {name} ⟆💠⟅", "⏤͟͟͞͞✧༚𓆩꯭𓆪༚✧⏤͟͟͞͞ {name} ⏤͟͟͞͞✧༚𓆩꯭𓆪༚✧⏤͟͟͞͞",
    "𓂃◌꯭🍃꯭𓂂 {name} 𓂃◌꯭🍃꯭𓂂", "⏤͟͟͞͞🦋꯭𓆩 {name} 𓆪꯭🦋⏤͟͟͞͞",
    "꧁༒☬ {name} ☬༒꧂", "✦✦✦ {name} ✦✦✦", "♛♛ {name} ♛♛",
    "♜♜ {name} ♜♜", "༺✮༻ {name} ༺✮༻", "★彡 {name} 彡★", 
    "✧༚✦꯭ {name} ✦꯭༚✧", "❀⏤͟͟͞͞𓆩꯭♡꯭𓆪⏤͟͟͞͞ {name} ❀", "𖠄❥꯭ {name} ❥꯭𖠄", "⟆♡̷̷̷⟅ {name} ⟆♡̷̷̷⟅",
    "𓆩⟡𓆪 {name} 𓆩⟡𓆪", "𓆫❦꯭𓆩 {name} 𓆩꯭❦𓆫", "⟆💠⟅ {name} ⟆💠⟅", "𓂃◌꯭🍃꯭𓂂 {name} 𓂃◌꯭🍃꯭𓂂",
    "⏤͟͟͞͞🦋꯭𓆩 {name} 𓆪꯭🦋⏤͟͟͞͞", "⚜️𓆩 {name} 𓆪⚜️", "❖⏤͟͟͞͞𓆩 {name} 𓆪⏤͟͟͞͞❖", "✪𓆩 {name} 𓆪✪",
    "꧁༒☬ {name} ☬༒꧂", "꧁𓊈 {name} 𓊉꧂", "★彡 {name} 彡★", "❁𓆩 {name} 𓆪❁", "✿❀ {name} ❀✿",
    "💎⏤͟͟͞͞𓆩 {name} 𓆪⏤͟͟͞͞💎", "➳♡ {name} ♡➳", "💖𓆩 {name} 𓆪💖", "✧🖤 {name} 🖤✧",
    "❤⃝𓆩 {name} 𓆪❤⃝", "✾𓆩 {name} 𓆪✾", "🍂𓆩 {name} 𓆪🍂", "⚡𓆩 {name} 𓆪⚡",
    "🌙⏤͟͟͞͞𓆩 {name} 𓆪⏤͟͟͞͞🌙", "🌸❥ {name} ❥🌸", "☾𓆩 {name} 𓆪☽", "🌟𓆩 {name} 𓆪🌟",
]

# Stylish fonts (Now 20+ styles!)
def stylish_fonts(text):
    fonts = [
        f"𝒞𝓊𝓇𝓈𝒾𝓋𝑒: {text} ✨",
        f"𝔊𝔬𝔱𝔥𝔦𝔠: {text} 🔥",
        f"𝕊𝕢𝕦𝕒𝕣𝕖: {text} 🔳",
        f"🅑🅤🅑🅑🅛🅔: {text} 🟠",
        f"𝗕𝗼𝗹𝗱: {text} 💪",
        f"𝘼𝙚𝙨𝙩𝙝𝙚𝙩𝙞𝙘: {text} 🌙",
        f"Ⓕⓐⓝⓒⓨ: {text} 🎭",
        f"𝓕𝓪𝓷𝓬𝔂: {text} 💖",
        f"𝕲𝖑𝖎𝖙𝖈𝖍: {text} ⚡",
        f"𝐅𝐮𝐭𝐮𝐫𝐢𝐬𝐭𝐢𝐜: {text} 🚀",
        f"𝔖𝔱𝔶𝔩𝔦𝔰𝔥: {text} 💎",
        f"Ƥяємιυм: {text} 🏆",
        f"🆂🆃🆈🅻🅴: {text} 🎨",
        f"𝕄𝕆𝔻𝔼ℝℕ: {text} 💻",
        f"꧁𓊈𒆜 {text} 𒆜𓊉꧂",
        f"《¤ {text} ¤》",
        f"𝓓𝓮𝓬𝓸𝓻𝓪𝓽𝓲𝓿𝓮: {text} 🖌",
        f"➵❦{text}❦➵",
        f"༄༄ {text} ༄༄",
        f"『 {text} 』",
        f"卍 {text} 卍"
    ]
    return random.choice(fonts)

# Emoji pack
emoji_pack = ["❤️", "💖", "💞", "💜", "✨", "🔥", "💎", "🌟", "🎀", "👑"]

# Generate stylish text
def generate_stylish_text(name):
    sep = random.choice(stylish_separators)
    tag = random.choice(["@", "#"])
    heart = random.choice(emoji_pack)
    return sep.format(name=f"{tag}{stylish_fonts(name)} {heart}")

# Generate 50 stylish names
def generate_50_stylish_names(name):
    names = [generate_stylish_text(name) for _ in range(50)]
    return "\n".join(names)

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "👋 Welcome! Send /style YourName to get stylish names.")

# Style command
@bot.message_handler(commands=['style'])
def style_message(message):
    text = message.text.replace("/style ", "").strip()
    
    if not text:
        bot.reply_to(message, "Please provide a name. Example: /style Alex")
        return

    stylish_names = generate_50_stylish_names(text)
    bot.send_message(message.chat.id, f"✨ Here are 50 stylish names:\n\n{stylish_names}")

# API check command
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
