import telebot

bot = telebot.TeleBot("760204273:AAFxzYj0FDZHeXs8979Dtm-8hhbIjLH1kNI")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	
bot.polling()