import telebot
from telebot import types
import random
import xlrd

TOKEN = '6243513933:AAEg8AIEMmoNIGBgQ89MbBbtYd8GYXclsos'

bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_cinema = types.KeyboardButton('Выбрать фильм ❤️')
button_serial = types.KeyboardButton('Выбрать сериал 💜')
markup.add(button_cinema, button_serial)


@bot.message_handler(commands=['start'])

def welcome(message):
    sti = open('stiker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Приветствую тебя, {0.first_name}! В данном боте ты можешь найти фильм на вечер 😎".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
    
@bot.message_handler(func=lambda message: True)

def response(message):
        
    if message.chat.type == 'private':
        # Если выбираем фильм
        if message.text == 'Выбрать фильм ❤️':
            # Считываем файл с названиями фильмов
            read_cinema = xlrd.open_workbook('cinema.xls', formatting_info=True)
            sheet = read_cinema.sheet_by_index(0)
            for rownum in range(sheet.nrows):
                rand = int(random.randint(0, rownum))
                row = sheet.row_values(rand)
            bot.send_message(message.chat.id, row)
 
        # Если выбираем сериал
        elif message.text == 'Выбрать сериал 💜':
            # Здесь можно оставить отзыв
            read_cinema = xlrd.open_workbook('serial.xls', formatting_info=True)
            sheet = read_cinema.sheet_by_index(0)
            for rownum in range(sheet.nrows):
                rand = int(random.randint(0, rownum))
                row = sheet.row_values(rand)
            bot.send_message(message.chat.id, row)

        # Если ничего не подошло             
        else:
            bot.send_message(message.chat.id, 'Я не знаю, что Вам ответить ☹️')

# Работа бота без остановки
bot.polling(none_stop = True)