import random
from collections import OrderedDict

from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from config import *
from loader import db

def shuffle_dict(d):
    keys = list(d.keys())
    random.shuffle(keys)
    return OrderedDict([(k, d[k]) for k in keys])


def send_stavka():
    keybord = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='💸 Сделать ставку', url=db.get_URL().get('checks'))]

    ])
    return keybord.as_markup()


def kb_url_Channel():
    keybord = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='💸 Сделать ставку', url=db.get_URL().get('channals'))]

    ])
    return keybord.as_markup()

def send_okey():
    keybord = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='✅ completed', callback_data=f'null')]
    ])
    return keybord.as_markup()


def get_cashback(user, amount):
    keybord = InlineKeyboardBuilder([
        [InlineKeyboardButton(text=f'💸 Получить {round(float(amount), 2)}$', callback_data=f'GET_CASH|{user}|{amount}')]
    ])
    return keybord.as_markup()

def get_fake_cashback(amount, status):
    text = f'✅ Кэшбэк получен [{amount}$]' if status else f'💸 Получить {round(float(amount), 2)}$'
    keybord = InlineKeyboardBuilder([
        [InlineKeyboardButton(text=text, callback_data=f'None')]
    ])
    return keybord.as_markup()

def okay_cashback(amount):
    keybord = InlineKeyboardBuilder([
        [InlineKeyboardButton(text=f'✅ Кэшбэк получен [{amount}$]', callback_data=f'nul')]
    ])
    return keybord.as_markup()



def keybord_add_balance(url):
    keybord = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='💸 Оплатить', url=url)]
    ])
    return keybord.as_markup()

def commands_game():
    keybord = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='📄 Команды', url=db.get_URL('command_game'))]
    ])
    return keybord.as_markup()

def ikb_stop():
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='⛔️ Выйти из режима ввода данных', callback_data='back_admin')]
    ])
    return bilder.as_markup()


def kb_menu(user):
    keybord = ReplyKeyboardBuilder()
    kb1 = KeyboardButton(text='📎 Реферальная программа')
    kb2 = KeyboardButton(text='👑 Админка')
    kb3 = KeyboardButton(text='💭 Информация')
    if user in ADMIN:
        keybord.add(kb1).add(kb3).add(kb2).adjust(1)
        return keybord.as_markup(resize_keyboard=True)
    keybord.add(kb1).add(kb3).adjust(1)
    return keybord.as_markup(resize_keyboard=True)




def kb_admin():
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='📊 Статистика казино', callback_data='stats_project')],
        [InlineKeyboardButton(text='📊 Статистика игроков', callback_data='stats_user')],
        [InlineKeyboardButton(text='💸 Пополнить баланс казино', callback_data='add_balance')],
        [InlineKeyboardButton(text='🎲 Фейк ставка', callback_data='settings_fake'),
         InlineKeyboardButton(text='📁 Скачать бд', callback_data='send_db')],
        [InlineKeyboardButton(text='📊 Коэффициенты', callback_data='kef_edit'),
         InlineKeyboardButton(text='✍️ Рассылка', callback_data='all_message_send')],
        [InlineKeyboardButton(text='🪨✂️📄 Подкрутка', callback_data='knb'),
         InlineKeyboardButton(text='🔗 Ссылки', callback_data='urls')],
        [InlineKeyboardButton(text='🗑 Удалить чеки', callback_data='deleted_checks')]
    ])
    return bilder.as_markup()

def ikb_tip_rassilka():
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='📸 Фото', callback_data='photo'),
         InlineKeyboardButton(text='✍️ Текст', callback_data='Texts')],
        [InlineKeyboardButton(text='« Назад', callback_data='back_admin')]
    ])
    return bilder.as_markup()

def kb_answer_delete():
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='✅ Да', callback_data='YesDel'),
         InlineKeyboardButton(text='❌ Нет', callback_data='back_admin')],
    ])
    return bilder.as_markup()


def kb_info():
    urls = db.get_URL()
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='🎲 Играть', url=urls.get('channals')),
         InlineKeyboardButton(text='📄 Новости', url=urls.get('news'))],
        [InlineKeyboardButton(text='✍️ Ключевые слова', url=urls.get('command_game'))],
        [InlineKeyboardButton(text='💸 Выплаты', url=urls.get('transfer')),
         InlineKeyboardButton(text='❓ Правила', url=urls.get('rules'))]
    ])
    return bilder.as_markup()

def kb_fake_switch(values: int):
    text_button = "🔴 Отключить" if values else '🟢 Включить'
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text=text_button, callback_data=f'fake|{values}')],
        [InlineKeyboardButton(text='« Назад', callback_data=f'back_admin')]
    ])
    return bilder.as_markup()


def kb_back_admin():
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='« Назад', callback_data=f'back_admin')]
    ])
    return bilder.as_markup()

def kb_edit_kef(data: dict):
    bilder = InlineKeyboardBuilder()
    for index, values in enumerate(data.items(), start=1):
        bilder.add(InlineKeyboardButton(text=f"{index}) [{values[1]}x]", callback_data=f'new_kef|{values[0]}|{values[1]}'))
    bilder.adjust(3)
    bilder.row(InlineKeyboardButton(text='« Назад', callback_data=f'back_admin'), width=1)

    return bilder.as_markup()


def kb_KNB_twist(cur_value:int):
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text=f'⚙️ {cur_value}%', callback_data=f'Twist_knb|{cur_value}')],
        [InlineKeyboardButton(text='« Назад', callback_data=f'back_admin')]
    ])
    return bilder.as_markup()


def kb_send_chek(url):
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text=f'🎁 Забрать приз', url=url)],
        [InlineKeyboardButton(text='💸 Сделать ставку', url=db.get_URL().get('checks'))]

    ])
    return bilder.as_markup()


def kb_viev_post(url, amount):
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text=f'🎁 [{round(float(amount), 2)}$]', url=url)],
    ])
    return bilder.as_markup()

def get_cashback_check(url, amount):
    keybord = InlineKeyboardBuilder([
        [InlineKeyboardButton(text=f'💸 Получить {round(float(amount), 2)}$', url=url)]
    ])
    return keybord.as_markup()


def ikb_send_post_photo():
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='✅ Запустить рассылку', callback_data='post_photo_go'),
         InlineKeyboardButton(text='❌ Отменить', callback_data='close_del')],
    ])
    return bilder.as_markup()


def ikb_send_post():
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='✅ Запустить рассылку', callback_data='post_go'),
        InlineKeyboardButton(text='❌ Отменить', callback_data='close_del')],
    ])
    return bilder.as_markup()


def kb_urls():
    bilder = InlineKeyboardBuilder([
        [InlineKeyboardButton(text='Канал', callback_data=f'UrlEdit|channals|Канал'),
         InlineKeyboardButton(text='Правила', callback_data=f'UrlEdit|rules|Правила')],
        [InlineKeyboardButton(text='Счет для оплаты', callback_data=f'UrlEdit|checks|Счет для оплаты')],
        [InlineKeyboardButton(text='Выплаты', callback_data=f'UrlEdit|transfer|Выплаты'),
         InlineKeyboardButton(text='Новости', callback_data=f'UrlEdit|news|Новости')],
        [InlineKeyboardButton(text='Как сделать ставку', callback_data=f'UrlEdit|info_stavka|Как сделать ставку')],
        [InlineKeyboardButton(text='Ключевые слова', callback_data=f'UrlEdit|command_game|Ключевые слова')],
        [InlineKeyboardButton(text='« Назад', callback_data=f'back_admin')]

    ])
    return bilder.as_markup()
