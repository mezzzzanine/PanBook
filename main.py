import telebot
import config
# from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])  # decorator pattern are used
def start(message):
    bot.send_message(message.chat.id, config.INFO)


@bot.message_handler(commands=['charts'])  # decorator pattern are used
def start(message):
    bot.send_message(message.chat.id, 'Most popular books of this week:')


@bot.message_handler(commands=['search'])  # decorator pattern are used
def start(message):
    bot.send_message(message.chat.id, 'Please type')


# code running

bot.polling(none_stop=True)
