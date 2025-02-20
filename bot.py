import telebot
import random
import http.client

# Bot Token
TOKEN = "7585692002:AAHcYU6Ksn16t21kb3mF82-c3fO-N_5Yik0"

# API Key & ID
RAPIDAPI_KEY = "823ad731bemsh1a89f7cbcabd094p1f2447jsnad1907e6f3a1"

bot = telebot.TeleBot(TOKEN)

# 50 Stylish Text Fonts
text_styles = [
    "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏", "𝔄𝔅ℭ𝔇𝔈𝔉𝔊𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷",
    "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕙𝕚𝕫𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫", "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",
    "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻", "𝒜ℬ𝒞𝒟ℰℱ𝒢𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏",
    "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩", "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟",
    "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉", "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ",
    "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛", "αв¢∂єfgнιנкℓмиσρqяѕтυνωχуz",
    "ค๒ς๔єŦﻮђเןкl๓ภ๏קợгรtยשฬאץչ", "A̶B̶C̶D̶E̶F̶G̶H̶I̶J̶K̶L̶M̶N̶O̶P̶Q̶R̶S̶T̶U̶V̶W̶X̶Y̶Z̶",
    "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ", "AᴮCᴰEᴷFᴳHᴵJᴷLᴹNᴼPᴿQᴿSᴿTᵁVᵂXʸZ",
    "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ", "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉",
] * 5  # 50 Styles

# 500 Emoji Pack
emoji_pack = [
    "👑💖", "🔥💎", "✨🎀", "🎉💖", "👑🥇", "💫💖", "🌟🎀", "👑😎", "🦋✨", "💜💖", "🎩🔥",
    "💛🎶", "💙💎", "🚀🔥", "🌸💖", "🥂🎉", "🎸🔥", "⚡👑", "🎭💖", "💚🎩", "🎼💎", "🥰✨", "🤩👑", "💘🔥",
    "🥇💜", "🎀💎", "✨💗", "🎊🔥", "💖🎸", "💞👑", "🔱💫", "🏆💖", "💃🎀", "🕺🔥", "🎵💎", "🎤👑",
    "🦄💖", "🌈🔥", "🌹🎀", "🥳💎", "🎯💖", "💰👑", "🎶🔥", "💐💎", "👑💓", "🎖💖", "🏅🔥", "🎩💎",
] * 10  # 500 emojis

# Stylish text generator
def fancy_text(text):
    style = random.choice(text_styles)
    return ''.join(style[i] if i < len(style) else char for i, char in enumerate(text))

# Add emojis
def add_emojis(text):
    return random.choice(emoji_pack) + " " + text + " " + random.choice(emoji_pack)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Send any text and I'll style it! Try /style YourText\n\n🔑 API ID: {API_ID}")

@bot.message_handler(commands=['style'])
def style_message(message):
    text = message.text.replace("/style ", "").strip()
    if not text:
        bot.reply_to(message, "Please provide text. Example: /style Hello")
        return
    styled_names = "\n".join([add_emojis(fancy_text(text)) for _ in range(10)])
    bot.reply_to(message, f"Here are your 10 stylish names:\n\n{styled_names}")

# API call function
@bot.message_handler(commands=['api'])
def call_api(message):
    try:
        conn = http.client.HTTPSConnection("ofc.p.rapidapi.com")
        headers = {'x-rapidapi-key': RAPIDAPI_KEY, 'x-rapidapi-host': "ofc.p.rapidapi.com"}
        conn.request("GET", "/status", headers=headers)
        res = conn.getresponse()
        data = res.read()
        bot.reply_to(message, f"API Response: {data.decode('utf-8')}\n\n🔑 API ID: {API_ID}")
    except Exception as e:
        bot.reply_to(message, f"API Error: {str(e)}")

# Run bot
bot.polling()
