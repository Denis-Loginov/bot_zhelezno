from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6977637669:AAEp49Z-Peu1S7OUiM_slkTGHKnBi3ZgR4o'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Мы рады приветствовать тебя, {name}, в нашем чат-боте, оказывающим помощь при покупке квартиры в ЖК Знак.')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# import os
# import random

# from bd import answer_links, article_links

# from datetime import date
# from dotenv import load_dotenv
# from telegram import ParseMode, ReplyKeyboardMarkup
# from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


# load_dotenv()
# secret_token = os.getenv('TOKEN_ZH')

# updater = Updater(token=secret_token)


# def wake_up(update, context):
#     """Функция именного приветствия при старте бота"""
#     chat = update.effective_chat
#     name = update.message.chat.first_name
#     button = ReplyKeyboardMarkup(
#         [['Пошаговая инструкция покупки квартиры']],
#         resize_keyboard=True)
#     context.bot.send_message(
#         chat_id=chat.id,
#         text=f'Мы рады приветствовать тебя, {name}, в нашем чат-боте, оказывающим помощь при покупке квартиры в ЖК Знак.',
#         reply_markup=button,
#         )


# def nazproect(update, context):
#     """Функция отправки контакта РЦК для консультации по Нац проекту"""
#     chat = update.effective_chat
#     name = update.message.chat.first_name
#     button = ReplyKeyboardMarkup(
#         [['Новогодние задачки', 'Cколько дней до волшебства'],
#         ['Лучшие статьи уходящего года', 'Как вступить в Нац проект']],
#         resize_keyboard=True)
#     telefon = '+7 (3412) 78-50-90'
#     Email = 'rck@umcluster.ru'
#     context.bot.send_message(
#         chat_id=chat.id,
#         text=f'{name}, позвони в офис РЦК Удмуртии по номеру {telefon} или напиши по адресу: {Email}',
#         reply_markup=button,
#         )


# updater.dispatcher.add_handler(CommandHandler('start', wake_up))
# updater.dispatcher.add_handler(MessageHandler(Filters.text('Cколько дней до волшебства'), until_new_year))


# updater.start_polling(poll_interval=3.00)
# updater.idle()
