import telebot

token = "7817077672:AAH_1CFeRC7OtBPaySG4edMjHXss2R_wRTY"
bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
