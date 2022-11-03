import telebot
import config
from search import Search
from charts import Charts

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])  # decorator pattern are used
def start(message):
    bot.send_message(message.chat.id, config.INFO)


@bot.message_handler(commands=['charts'])  # decorator pattern are used
def charts(message):
    bot.send_message(message.chat.id, 'Most popular books of this week:')


@bot.message_handler(commands=['search'])  # decorator pattern are used
def search(message):
    bot.send_message(message.chat.id, 'What you looking for?')



@bot.message_handler(commands=['mezza9'])  # decorator pattern are used
def admin(message):
    bot.send_message(message.chat.id, "welcome")
    


# code running
bot.polling(none_stop=True)
