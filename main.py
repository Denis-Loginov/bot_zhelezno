import os
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from dotenv import load_dotenv
from bd import steps

load_dotenv()

bot = Bot(token=os.getenv('TOKEN_ZH'))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.CRITICAL)

"""Блок создания клавиатуры основного меню"""
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
buttons = [
    "Выбрать квартиру",
    "Условия по ипотеке",
    "Шаги при покупке квартиры",
    "Перечень необходимых документов",
    "Подписаться на Znak news"
    ]
keyboard.add(*buttons)


"""Блок создания клавиатуры выбора квартиры"""
room_kb = InlineKeyboardMarkup(row_width=2)
one_room = InlineKeyboardButton(text='Однокомнатные', url='https://zhcom.ru/flats?rooms%5B%5D=1')
two_room = InlineKeyboardButton(text='Двухкомнатные', url='https://zhcom.ru/flats?rooms%5B%5D=2')
room_kb.add(one_room, two_room)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """Функция именного приветствия при старте бота"""
    await message.reply(f'Мы рады приветствовать тебя, {message.from_user.first_name}, в нашем чат-боте, оказывающим помощь при покупке квартиры в ЖК Знак.', reply_markup=keyboard)


@dp.message_handler(Text(equals='Выбрать квартиру'))
async def apartment_choosing(message: types.Message):
    """Функция отправки имеющихся в продаже вариантов планировок"""
    await message.answer('Выберите количество комнат:', reply_markup=room_kb)


@dp.message_handler(Text(equals='Подписаться на Znak news'))
async def subscription_znak(message: types.Message):
    """Функция подписки на новостного бота новостройки"""
    await message.reply(f'{message.from_user.first_name}, подписаться на новости и объявления ЖК Знак можно перейдя по ссылке https://t.me/ZnakBot', reply_markup=keyboard)


@dp.message_handler(Text(equals='Условия по ипотеке'))
async def send_conditions(message: types.Message):
    """Функция отправки условий по ипотеке"""
    doc = open(('Условия') + '.pdf', 'rb')
    await message.reply_document(doc)


@dp.message_handler(Text(equals='Перечень необходимых документов'))
async def send_list_doc(message: types.Message):
    """Функция отправки переченя необходимых документов"""
    doc = open(('Перечень') + '.pdf', 'rb')
    await message.reply_document(doc)


@dp.message_handler(Text(equals='Шаги при покупке квартиры'))
async def send_steps(message: types.Message):
    """Функция отправки схемы покупки квартиры"""
    await message.reply(steps)

if __name__ == '__main__':
    executor.start_polling(dp)
