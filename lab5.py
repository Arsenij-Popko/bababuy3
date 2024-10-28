import telebot
from telebot import types
bot = telebot.TeleBot('7817077672:AAF4SWmyD0VpKuZy9GEnC6-0vTwW-x7A7Kg')


@bot.message_handler(commands=['start'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Тренування спини', callback_data='button1')
    button2 = types.InlineKeyboardButton(text='Тренування грудей', callback_data='button2')
    button3 = types.InlineKeyboardButton(text='Тренування біцепса', callback_data='button3')
    button4 = types.InlineKeyboardButton(text='Тренування ніг', callback_data='button4')
    button5 = types.InlineKeyboardButton(text='Тренування пресу', callback_data='button5')
    markup.add(button1, button2, button3, button4, button5)

    bot.send_message(message.chat.id, 'Привіт,обери що ти хочеш сьогодні зробити', reply_markup=markup)

    

if __name__ == '__main__':
    bot.polling(none_stop=True)





