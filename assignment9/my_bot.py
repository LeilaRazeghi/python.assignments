import random
import telebot
from telebot import types

my_keyboard=types.ReplyKeyboardMarkup(row_width=3)
key1=types.KeyboardButton("backward")
key2=types.KeyboardButton("forward")
key3=types.KeyboardButton("calculator")
key4=types.KeyboardButton("")
key5=types.KeyboardButton("")

my_keyboard.add(key1,key2,key3,key4,key5)

bot = telebot.TeleBot("5906004353:AAH3-tRSHUZ9uL3IqFdJWxvfoae07xdgJvc", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "How can i help you?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text=="salam":
	    bot.send_message(message.chat.id, "how do you do!")
	elif message.text=="how are you?":
        bot.send_message(message.chat.id,"fine, thanks") 
    elif message.text=="i love you!":
        bot.send_message(message.chat.id,"love you too")
    else:
       bot.send_message(message.chat.id, " i dont understand what you say!",reply_markup=my_keyboard)
	   
bot.infinity_polling()