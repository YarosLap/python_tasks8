import telebot
import os
import re

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Здравствуй, {message.from_user.first_name}! Ожидаю ваше обращение')

@bot.message_handler(content_types=['text'])
def read_text_commands(message):
    data = open('/Users/yaroslav/Desktop/GB/Python/dz8.nosync/log.txt', mode='a', encoding='utf-8')
    data.write(f'{message.from_user.id}:{message.text}\n')
    data.close()
    data2 = open('/Users/yaroslav/Desktop/GB/Python/dz8.nosync/ans.txt', mode='r', encoding='utf-8')
    answer = data2.readline()
    data.close()
    bot.reply_to(message, answer)

bot.polling()
