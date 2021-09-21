TOKEN = '1870669418:AAGgvriqRx4xJcwCR9g85jLh3BaSrGS7LUM'

import telebot
import config
import random 
from telebot import types


bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])
def welcome(message):
        
    sti = open('/home/georgy/anim.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("рандомное число")
    item2 = types.KeyboardButton("как настроение???")
    item3 = types.KeyboardButton('инфо')
    item4 = types.KeyboardButton('сайт')
    markup.add(item1, item2, item3, item4)
  

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)




@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == 'сайт':
        bot.send_message(message.chat.id, 'тут будет сайт или что то типо того не знаю как скажете')

    elif message.text == 'инфо':

        bot.send_message(message.chat.id, 'что конкретно вы хотите узнать?')

        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("тут будет переход", callback_data='good')
        item2 = types.InlineKeyboardButton("и здесь", callback_data='bad')

        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'тут будет всякая инфа', reply_markup=markup)
    else:
         bot.send_message(message.chat.id, 'я не могу ответить')



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'тут будет заполнение')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'здесь тоже')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="инфо",
                reply_markup=None)
    

    except Exception as e:
        print(repr(e))




@bot.message_handler(content_types=['text'])
def lalala(message):

    if message.chat.type == 'private':

        if message.text == 'рандомное число':

            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'как настроение???':

            bot.send_message(message.chat.id, 'хорошо')

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Отлично, как сам?', reply_markup=markup)
        else:

            bot.send_message(message.chat.id, 'я не могу ответить') 


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько ')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает ')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Как настроение???",
                reply_markup=None)

          
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!LOOOOOOOOL")


    except Exception as e:
        print(repr(e))



    
bot.polling(none_stop=True)
