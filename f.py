import telebot
from telebot import types
from telebot.apihelper import send_message

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

    bot.send_message(message.chat.id, 'Привіт, обери що ти хочеш сьогодні зробити', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'button1':
        send_time_options(call, 'Тренування спини')
    elif call.data == 'button2':
        send_time_options(call, 'Тренування грудей')
    elif call.data == 'button3':
        send_time_options(call, 'Тренування біцепса')
    elif call.data == 'button4':
        send_time_options(call, 'Тренування ніг')
    elif call.data == 'button5':
        send_time_options(call, 'Тренування пресу')

def send_time_options(call, training_type):
    markup = types.InlineKeyboardMarkup(row_width=1)
    time_15 = types.InlineKeyboardButton(text='15 хвилин', callback_data=f'{training_type}_15')
    time_30 = types.InlineKeyboardButton(text='30 хвилин', callback_data=f'{training_type}_30')
    time_45 = types.InlineKeyboardButton(text='45 хвилин', callback_data=f'{training_type}_45')
    markup.add(time_15, time_30, time_45)
    bot.send_message(call.message.chat.id, f'Вибери тривалість для {training_type}:', reply_markup=markup)
    bot.delete_message(call.message.chat.id, call.message.message_id)

@bot.callback_query_handler(func=lambda call: '15' in call.data or '30' in call.data or '45' in call.data)
def time_selection(call):
    training_type, duration = call.data.split('_')
    file_path = get_file_path(training_type, duration)

    bot.send_message(call.message.chat.id, f'Ти обрав {training_type} на {duration}! Гарного тренування!')

    with open(file_path, 'rb') as file:
        bot.send_document(call.message.chat.id, file)

    bot.delete_message(call.message.chat.id, call.message.message_id)

def get_file_path(training_type, duration):

    file_paths = {
        'Тренування спини, 15 хвилин': 'files/back_15.pdf',
        'Тренування спини, 30 хвилин': 'files/back_30.pdf',
        'Тренування спини, 45 хвилин': 'files/back_45.pdf',

    }
    return file_paths.get(f'{training_type}_{duration}')

bot.polling(none_stop=True)

