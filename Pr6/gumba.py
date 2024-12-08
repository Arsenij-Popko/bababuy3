import telebot
from telebot import types
from config import get_token
from decorators import log_message


def main():
    bot = telebot.TeleBot(get_token())

    @bot.message_handler(commands=['start'])
    def button(message):
        markup = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton(text='Тренування спини', callback_data='button1')
        button2 = types.InlineKeyboardButton(text='Тренування грудей', callback_data='button2')
        button3 = types.InlineKeyboardButton(text='Тренування біцепса', callback_data='button3')
        button4 = types.InlineKeyboardButton(text='Тренування ніг', callback_data='button4')
        markup.add(button1, button2, button3, button4, )

        bot.send_message(message.chat.id, 'Привіт, обери що ти хочеш сьогодні зробити', reply_markup=markup)

    @log_message
    @bot.callback_query_handler(func=lambda
            call: 'button1' in call.data or 'button2' in call.data or 'button3' in call.data or 'button4' in call.data)
    def callback_worker(call):
        if call.data == 'button1':
            send_time_options(call, 'Тренування спини')
        elif call.data == 'button2':
            send_time_options(call, 'Тренування грудей')
        elif call.data == 'button3':
            send_time_options(call, 'Тренування біцепса')
        elif call.data == 'button4':
            send_time_options(call, 'Тренування ніг')


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
        print(training_type, duration)
        file_path = get_file_path(training_type, duration)
        print(file_path)
        bot.send_message(call.message.chat.id, f'Ти обрав {training_type} на {duration}! Гарного тренування!')
        with open(file_path, 'rb') as file:
            bot.send_document(call.message.chat.id, file)

        bot.delete_message(call.message.chat.id, call.message.message_id)

    def get_file_path(training_type, duration):
        file_paths = {
            'Тренування спини 15': 'filesback_15',
            'Тренування спини 30': 'filesback_30',
            'Тренування спини 45': 'filesback_45',
            'Тренування грудей 15': 'fileschest_15',
            'Тренування грудей 30': 'fileschest_30',
            'Тренування грудей 45': 'fileschest_45',
            'Тренування біцепса 15': 'filesbiceps_15',
            'Тренування біцепса 30': 'filesbiceps_30',
            'Тренування біцепса 45': 'filesbiceps_45',
            'Тренування ніг 15': 'fileslegs_15',
            'Тренування ніг 30': 'fileslegs_30',
            'Тренування ніг 45': 'fileslegs_45'
        }
        return file_paths.get(f'{training_type} {duration}')

    print("bot gotov")
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()