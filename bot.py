#!/usr/bin/python3 -u
import telebot
import time
import urllib
import subprocess
from telebot import types

bot = telebot.TeleBot("Yout TeleBot code")
tiempo = time.strftime("%H horas %M minutos y %S segundos exactamente")

@bot.message_handler(commands=['start'])
def send_photo(message):
    bot.send_message(message.chat.id, 'Type')

def recibe(messages):
    for m in messages:
        if m.content_type == "text":
            ok = subprocess.call(m.text + ' >> archivoSalida', shell=True)
            if ok == 0:
                archivo = open('archivoSalida','r+')
                archivo.write('OK')
                show = archivo.read()
                subprocess.call('rm archivoSalida', shell=True)
                bot.send_message(m.chat.id,show + "ok")

            else:
                bot.send_message(m.chat.id,"Error")

bot.set_update_listener(recibe)

bot.polling()
