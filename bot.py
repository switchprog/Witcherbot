import telebot
from telebot import types
from info import *

info_commands = readFromJSON1()
game_commands = readFromJSON2()

token = "6371422435:AAH4dDqPui2gTcoNCN10olAe76RRA1iyEPc"

bot = telebot.TeleBot(token)

state_player = 0
state_keyItem = 0

keyboard = types.ReplyKeyboardMarkup(True)
button = types.KeyboardButton(text='/help')
button1 = types.KeyboardButton(text='Начало')
button2 = types.KeyboardButton(text='/Команды')
keyboard.add(button, button1, button2)

keyboard1 = types.ReplyKeyboardMarkup(True)
keyboard2 = types.ReplyKeyboardMarkup(True)
keyboard3 = types.ReplyKeyboardMarkup(True)
keyboard4 = types.ReplyKeyboardMarkup(True)
keyboard5 = types.ReplyKeyboardMarkup(True)
keyboard6 = types.ReplyKeyboardMarkup(True)
button = types.KeyboardButton(text='Осмотреться')
button1 = types.KeyboardButton(text='Идти на свет')
button2 = types.KeyboardButton(text='Бежать')
button3 = types.KeyboardButton(text='Сражаться')
button4 = types.KeyboardButton(text='Идти далее')
button5 = types.KeyboardButton(text='Вступить в бой')
button6 = types.KeyboardButton(text='Начать заново')
keyboard1.add(button, button1)
keyboard2.add(button1)
keyboard3.add(button2, button3)
keyboard4.add(button4)
keyboard5.add(button5)
keyboard6.add(button6)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, info_commands['/start'], reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, info_commands['/help'], reply_markup=keyboard)

@bot.message_handler(commands=['Команды'])
def help_message(message):
    bot.send_message(message.chat.id, info_commands['Команды'], reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def text_message(message):
    global state_player
    global state_keyItem
    if message.text == 'Начало' or state_player == 0:
        photo = open('0.jpg', 'rb')
        state_player = 1
        bot.send_message(message.chat.id, info_commands['Начало'], reply_markup=keyboard)
        bot.send_photo(message.chat.id, photo)
    if state_player == 1:
        state_player = 2
        photo = open('1.jpg', 'rb')
        bot.send_message(message.chat.id, game_commands['1'], reply_markup=keyboard1)
        bot.send_photo(message.chat.id, photo)
    if message.text == 'Осмотреться':
        state_keyItem+=1
        photo = open('3.jpg', 'rb')
        bot.send_message(message.chat.id, game_commands['2'], reply_markup=keyboard2)
        bot.send_photo(message.chat.id, photo)
    if message.text == 'Идти на свет':
        photo = open('4.jpg', 'rb')
        bot.send_message(message.chat.id, game_commands['3'], reply_markup=keyboard3)
        bot.send_photo(message.chat.id, photo)
    if message.text == 'Сражаться':
        state_keyItem += 1
        photo = open('2.jpg', 'rb')
        bot.send_message(message.chat.id, game_commands['4'], reply_markup=keyboard4)
        bot.send_photo(message.chat.id, photo)
    if message.text == 'Идти далее':
        photo = open('5.jpg', 'rb')
        bot.send_message(message.chat.id, game_commands['8'], reply_markup=keyboard5)
        bot.send_photo(message.chat.id, photo)
    if message.text == 'Бежать':
        photo = open('5.jpg', 'rb')
        bot.send_message(message.chat.id, game_commands['5'], reply_markup=keyboard5)
        bot.send_photo(message.chat.id, photo)
    if message.text == 'Вступить в бой':
        photo = open('6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        if state_keyItem == 2:
            state_player = 0
            photo = open('7.jpg', 'rb')
            bot.send_message(message.chat.id, game_commands['6'], reply_markup=keyboard6)
            bot.send_photo(message.chat.id, photo)
        else:
            photo = open('8.jpg', 'rb')
            bot.send_message(message.chat.id, game_commands['7'], reply_markup=keyboard6)
            bot.send_photo(message.chat.id, photo)
            state_player = 0

bot.polling()
