import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def answer(message):
    bot.send_message(message.chat.id, "ПАШОЛ НАХУЙ!")

@bot.message_handler(commands=['info', "bot_info"])
def answer(message):
    bot.send_message(message.chat.id, "Че те нада? ИДИ нахуй")
    
# code running

bot.polling(none_stop=True)