from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import pandas as pd

import os


'''**********************************************************команды*****************************************************************************'''
token= 5697385909:AAE6HLFD0JcSUk1Nkk_YM7RNRhvCDuyqF3I

bot= Bot(token=token)
dp= Dispatcher(bot)
async def on_startup(_):
	await bot.send_message(290662407,'я тута')


@dp.message_handler(commands=['список'])
async def echo_send(message : types.Message):
	sheet_url='https://docs.google.com/spreadsheets/d/1ILaTyyvuy0djIemys1qBKp72sIPIPH_9P6rjVzWlX2s/edit#gid=0'
	url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
	df = pd.read_csv(url_1)
	
	await message.reply(df['город'])


@dp.message_handler()
async def echo_send(message : types.Message):
	sheet_url='https://docs.google.com/spreadsheets/d/1ILaTyyvuy0djIemys1qBKp72sIPIPH_9P6rjVzWlX2s/edit#gid=0'
	url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
	df = pd.read_csv(url_1)
	df['город']=df['город'].str.lower()
	message.text=message.text.lower()
		#await message.reply(df[df['город']==message.text])
	if message.text in  df['город'].unique():
		await message.reply(df[df['город']==message.text])
	else:
		await message.reply('нет такого города введите команду /список для ознакомления со списком городов')
		



executor.start_polling(dp,skip_updates=True, on_startup=on_startup)
