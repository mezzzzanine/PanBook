import telebot
import config
from search import Search
from charts import Charts

bot = telebot.TeleBot(config.TOKEN)

find = Search()
most_popular = Charts()


@bot.message_handler(commands=['start', 'help'])  # decorator pattern are used
def start(message):
    bot.send_message(message.chat.id, config.INFO)


@bot.message_handler(commands=['charts'])  # decorator pattern are used
def charts(message):
    bot.send_message(message.chat.id, most_popular.charts())


@bot.message_handler()  # decorator pattern are used
def search(message):
    bot.send_message(message.chat.id, find.find_book(message.text))


@bot.message_handler(commands=['mezza9'])  # decorator pattern are used
def admin(message):
    bot.send_message(message.chat.id, message.text)


# code running
bot.polling(none_stop=True)
