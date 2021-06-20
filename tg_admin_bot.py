# Turdibek Developer - t.me/turdibekdev
# Bot korinishi: https://t.me/turdibekdev/56
# Kutubxonani yuklash: pip install pyTelegramBotAPI
from telebot import TeleBot

bot = TeleBot("1687562369:AH85M8u7-t1V7NvtPwf3CHPc")

	admin = "1234567890" # bu joyga oz Telegram ID'ingizni kiritib qoying
	
@bot.message_handler(commands=['start'])
def xush_kelibsiz(message):
	chat_id = message.from_user.id
	text = f"Salom {message.from_user.first_name}.\nMenga jonatgan barcha xabaringiz @turdibekdev adminiga yetkaziladi. Marhamat, xabar jonating."
	
	if str(chat_id) == admin:
		bot.send_message(admin, "Salom admin, xush kelibsiz...")
	else:
		bot.send_message(chat_id, text)

@bot.message_handler(func=lambda message: True)
def xabar(message):
	matn = message.text
	fr = message.from_user
	text = f"Yangi xabar\nIsm: {fr.first_name}\nFamilya: {fr.last_name}\nUsername: {fr.username}\nID: {fr.id}\n\nJonatilgan xabar:\n{matn}"
	bot.send_message(admin, text)
	bot.send_message(message.chat.id, "Xabar jonatildi...")
bot.polling()
