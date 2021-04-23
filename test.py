# -*- coding: utf-8 -*-
import socket, telebot

a = socket.gethostbyname(socket.gethostname())

print(a)

token = "1725730451:AAG8bGzd5s2fMQgXeIv5ICuf5h7rN6n55-U"
bot = telebot.TeleBot(token)

bot.send_message(1356201546, "ip socket server:\n" + str(a))
bot.send_message(1024861899, "ip socket server:\n" + str(a))