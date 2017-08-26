#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot

from key import key
from managers.GameManager import GameManager
from managers.RegistrationManager import RegistrationManager

bot = telebot.TeleBot(key)


@bot.message_handler(commands=['love_reg'])
def handle_text(message):
    print('start love_bot')
    rm = RegistrationManager(message)
    rm.create_user()


@bot.message_handler(commands=['love'])
def handle_text(message):
    print('start love game')
    gm = GameManager(message)
    gm.start_game()


@bot.message_handler(commands=['lovestat'])
def handle_text(message):
    print('stats love game')
    gm = GameManager(message)
    gm.get_stats()


bot.polling(none_stop=True, interval=0)
