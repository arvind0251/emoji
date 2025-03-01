import telebot
import random
import http.client

# ✅ Directly Add Your Keys Here
BOT_TOKEN = "7585692002:AAHcYU6Ksn16t21kb3mF82-c3fO-N_5Yik0"
RAPIDAPI_KEY = "823ad731bemsh1a89f7cbcabd094p1f2447jsnad1907e6f3a1"

bot = telebot.TeleBot(BOT_TOKEN)

# Stylish separators
stylish_separators = [
    "★彡 {name} 彡★", "✿✧ {name} ✧✿", "💫𓆩 {name} 𓆪💫", "☾𓆩 {name} 𓆪☽", "✨𓆩 {name} 𓆪✨",
    "⚜️𓆩 {name} 𓆪⚜️", "⭐𓆩 {name} 𓆪⭐", "❀༺ {name} ༻❀", "☁️𓆩 {name} 𓆪☁️", "🦋𓆩 {name} 𓆪🦋", "⟆♡̷̷̷⟅ {name} ⟆♡̷̷̷⟅", "𓆩⟡𓆪 {name} 𓆩⟡𓆪", "𓆫❦꯭𓆩 {name} 𓆩꯭❦𓆫", "⟆💠⟅ {name} ⟆💠⟅", "⏤͟͟͞͞✧༚𓆩꯭𓆪༚✧⏤͟͟͞͞ {name} ⏤͟͟͞͞✧༚𓆩꯭𓆪༚✧⏤͟͟͞͞", "𓂃◌꯭🍃꯭𓂂 {name} 𓂃◌꯭🍃꯭𓂂", "⏤͟͟͞͞🦋꯭𓆩 {name} 𓆪꯭🦋⏤͟͟͞͞", "꧁༒☬ {name} ☬༒꧂", "✦✦✦ {name} ✦✦✦", "♛♛ {name} ♛♛", "♜♜ {name} ♜♜", "༺✮༻ {name} ༺✮༻", "★彡 {name} 彡★", "✧༚✦꯭ {name} ✦꯭༚✧", "❀⏤͟͟͞͞𓆩꯭♡꯭𓆪⏤͟͟͞͞ {name} ❀", "𖠄❥꯭ {name} ❥꯭𖠄", "⟆♡̷̷̷⟅ {name} ⟆♡̷̷̷⟅", "𓆩⟡𓆪 {name} 𓆩⟡𓆪", "𓆫❦꯭𓆩 {name} 𓆩꯭❦𓆫", "⟆💠⟅ {name} ⟆💠⟅", "𓂃◌꯭🍃꯭𓂂 {name} 𓂃◌꯭🍃꯭𓂂", "⏤͟͟͞͞🦋꯭𓆩 {name} 𓆪꯭🦋⏤͟͟͞͞", "⚜️𓆩 {name} 𓆪⚜️", "❖⏤͟͟͞͞𓆩 {name} 𓆪⏤͟͟͞͞❖", "✪𓆩 {name} 𓆪✪", "꧁༒☬ {name} ☬༒꧂", "꧁𓊈 {name} 𓊉꧂", "★彡 {name} 彡★", "❁𓆩 {name} 𓆪❁", "✿❀ {name} ❀✿", "💎⏤͟͟͞͞𓆩 {name} 𓆪⏤͟͟͞͞💎", "➳♡ {name} ♡➳", "💖𓆩 {name} 𓆪💖", "✧🖤 {name} 🖤✧", "❤⃝𓆩 {name} 𓆪❤⃝", "✾𓆩 {name} 𓆪✾", "🍂𓆩 {name} 𓆪🍂", "⚡𓆩 {name} 𓆪⚡", "🌙⏤͟͟͞͞𓆩 {name} 𓆪⏤͟͟͞͞🌙", "🌸❥ {name} ❥🌸", "☾𓆩 {name} 𓆪☽", "🌟𓆩 {name} 𓆪🌟", "✧༚✦꯭ {name} ✦꯭༚✧", "❀⏤͟͟͞͞𓆩꯭♡꯭𓆪⏤͟͟͞͞ {name} ❀", "𖠄❥꯭ {name} ❥꯭𖠄", "⟆♡̷̷̷⟅ {name} ⟆♡̷̷̷⟅", "𓆩⟡𓆪 {name} 𓆩⟡𓆪", "𓆫❦꯭𓆩 {name} 𓆩꯭❦𓆫", "⟆💠⟅ {name} ⟆💠⟅", "⏤͟͟͞͞✧༚𓆩꯭𓆪༚✧⏤͟͟͞͞ {name} ⏤͟͟͞͞✧༚𓆩꯭𓆪༚✧⏤͟͟͞͞", "𓂃◌꯭🍃꯭𓂂 {name} 𓂃◌꯭🍃꯭𓂂", "⏤͟͟͞͞🦋꯭𓆩 {name} 𓆪꯭🦋⏤͟͟͞͞", "꧁༒☬ {name} ☬༒꧂", "✦✦✦ {name} ✦✦✦", "♛♛ {name} ♛♛", "♜♜ {name} ♜♜", "༺✮༻ {name} ༺✮༻", "★彡 {name} 彡★", "⚜️𓆩 {name} 𓆪⚜️", "❖⏤͟͟͞͞𓆩 {name} 𓆪⏤͟͟͞͞❖", "✪𓆩 {name} 𓆪✪", "꧁𓊈 {name} 𓊉꧂", "💎⏤͟͟͞͞𓆩 {name} 𓆪⏤͟͟͞͞💎", "➳♡ {name} ♡➳", "💖𓆩 {name} 𓆪💖", "✧🖤 {name} 🖤✧", "❤⃝𓆩 {name} 𓆪❤⃝", "✾𓆩 {name} 𓆪✾", "🍂𓆩 {name} 𓆪🍂", "⚡𓆩 {name} 𓆪⚡", "🌙⏤͟͟͞͞𓆩 {name} 𓆪⏤͟͟͞͞🌙", "🌸❥ {name} ❥🌸", "☾𓆩 {name} 𓆪☽", "🌟𓆩 {name} 𓆪🌟", "☆⌒★ {name} ★⌒☆", "✿✧ {name} ✧✿", "💫𓆩 {name} 𓆪💫", "💠☬ {name} ☬💠", "⭑𓆩 {name} 𓆪⭑", "❀༺ {name} ༻❀", "☁️𓆩 {name} 𓆪☁️", "🦋𓆩 {name} 𓆪🦋", "✿𓆩 {name} 𓆪✿", "❥𓆩 {name} 𓆪❥", "🌹𓆩 {name} 𓆪🌹", "⭐𓆩 {name} 𓆪⭐", "✨𓆩 {name} 𓆪✨", "🎀𓆩 {name} 𓆪🎀"


]

# ✅ 50 Stylish Fonts
def stylish_fonts(text):
    fonts = [
        "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝐽𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵",
        "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝓉𝓊𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ",
        "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅",
        "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ",
        "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉",
        "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡",
        "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝘌𝘍𝘎𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕",
    ]
    return text.translate(str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", random.choice(fonts)))

# Emoji pack
emoji_pack = ["❤️", "💖", "💞", "💜", "✨", "🔥", "💎", "🌟", "🎀", "👑"]

# Generate stylish text
def generate_stylish_text(name):
    sep = random.choice(stylish_separators)
    heart = random.choice(emoji_pack)
    return sep.format(name=f"{stylish_fonts(name)} {heart}")

# ✅ Generate 100 stylish names
def generate_100_stylish_names(name):
    return "\n".join([generate_stylish_text(name) for _ in range(100)])

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "👋 Welcome! Send /style YourName to get 100 stylish names.")

# Style command
@bot.message_handler(commands=['style'])
def style_message(message):
    text = message.text.replace("/style", "").strip()
    
    if not text:
        bot.reply_to(message, "Please provide a name. Example: /style Alex")
        return

    stylish_names = generate_100_stylish_names(text)
    bot.send_message(message.chat.id, f"✨ Here are 100 stylish names:\n\n{stylish_names}")

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
