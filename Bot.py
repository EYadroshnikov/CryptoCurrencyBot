import config as cfg
import telebot
import data
from telebot import types
import msg
import datetime

from pprint import pprint


def log(message):
    ss = f"{message.from_user.first_name} {message.from_user.last_name}:     {message.text}"
    print(
        f"{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')} | {ss:^45} ")


bot = telebot.TeleBot(cfg.token, parse_mode=None)


def construct_murkup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton("Bitcoin"),
               types.KeyboardButton("Ethereum"),
               types.KeyboardButton("BNB"),
               types.KeyboardButton("XRP"),
               types.KeyboardButton("Solana"),
               types.KeyboardButton("Dogecoin"),
               types.KeyboardButton("Tether"),
               types.KeyboardButton("Terra"),

               )
    return markup


def construct_inline_murkup():
    inlineKeyBoard = types.InlineKeyboardMarkup()
    inlineKeyBoard.add(types.InlineKeyboardButton(text="Обновить", callback_data="reload"))
    return inlineKeyBoard


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}, Выберите валюту",
                     reply_markup=construct_murkup())


@bot.message_handler(func=lambda message: True)
def handler(message):
    log(message)
    bot.delete_message(message.chat.id, message.message_id)
    try:
        img = open(f'img/{data.getImgName(message)}', 'rb')
    except Exception as es:
        img = open("img/404.png", "rb")
    bot.send_photo(message.chat.id, img, caption=msg.construct_message(message), reply_markup=construct_inline_murkup())


@bot.callback_query_handler(func=lambda call: call.data == 'reload')
def reload(call):
    call.text = data.getCur(call.message.caption)

    bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.id,
                             caption=msg.construct_message(call), reply_markup=construct_inline_murkup())


bot.polling()
