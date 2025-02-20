import telebot
import random
import http.client

# Bot token
TOKEN = "7585692002:AAHcYU6Ksn16t21kb3mF82-c3fO-N_5Yik0"

bot = telebot.TeleBot(TOKEN)

# 50 Stylish text fonts
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
]

# 500 Emoji Pack
emoji_pack = [
    "👑💖", "🔥💎", "✨🎀", "🎉💖", "👑🥇", "💫💖", "🌟🎀", "👑😎", "🦋✨", "💜💖", "🎩🔥",
    "💛🎶", "💙💎", "🚀🔥", "🌸💖", "🥂🎉", "🎸🔥", "⚡👑", "🎭💖", "💚🎩", "🎼💎", "🥰✨", "🤩👑", "💘🔥",
    "🥇💜", "🎀💎", "✨💗", "🎊🔥", "💖🎸", "💞👑", "🔱💫", "🏆💖", "💃🎀", "🕺🔥", "🎵💎", "🎤👑",
    "🦄💖", "🌈🔥", "🌹🎀", "🥳💎", "🎯💖", "💰👑", "🎶🔥", "💐💎", "👑💓", "🎖💖", "🏅🔥", "🎩💎",
] * 10  # 500 emojis (by repeating set 10 times)

def fancy_text(text):
    return "".join(random.choice(text_styles)[ord(c) % len(text_styles[0])] if c.isalpha() else c for c in text)

def add_emojis(text):
    return random.choice(emoji_pack) + " " + text + " " + random.choice(emoji_pack)

@bot.message_handler(commands=['style'])
def style_message(message):
    text = message.text.replace("/style ", "")
    
    if not text:
        bot.reply_to(message, "Please provide text. Example: /style Hello")
        return
    
    styled_names = "\n".join([add_emojis(fancy_text(text)) for _ in range(10)])
    
    bot.reply_to(message, f"Here are your 10 stylish names:\n\n{styled_names}")

# Run bot
bot.polling()
