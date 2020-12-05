import discord
from discord.ext import commands
import os
from discord.utils import get
from random import randint
import json
import requests
import random
import sqlite3
import random as r
import asyncio
import random
from random import choice
import datetime
from random import randint
from Cybernator import Paginator
from discord.ext.commands import Bot
import sys
import traceback
import wikipedia
from googletrans import Translator
from time import sleep
import googletrans
import socket
import psutil as ps
import time 
import os
import yaml

res  = 407865383157235722

class event(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def флаги(self, ctx):
		if ctx.author.id == res:
			return await ctx.send(f"{ctx.author.mention} Вы в чёрном списке")
		with open('flags.json','r',encoding='utf8') as f: #открываем файл, который будет возле файла бота, и ставим кодировку utf-8 чтобы кириллица нормально отображалась и воспринималась
			flags = json.load(f) #получаем содержимое
			count = 1 #щас будет подсчёт раундов игры
			while count <= 10: #цикл игры, число 10 означает допустимое количество раундов, можете поменять
				otvet = random.choice(flags['Флаги']) #получаем рандомный флаг
				e = discord.Embed(title = f"**Флаг** `{count}`", color=0xa400fc) #создаём эмбед
				e.set_image(url = otvet['url'])
				await ctx.send(embed = e)
				def check(m): #создаём проверку ответа
					return m.content == otvet['answer'] and ctx.channel == ctx.channel

				msg = await self.bot.wait_for('message', check=check)
				em = discord.Embed(title = "**Правильный ответ!**", color=0xa400fc) #пишет когда чел правильно ответил
				em.add_field(name = "**Ответил:**", value = f"**{msg.author.mention}, +1 балл**")
				em.add_field(name = "**Правильный ответ:**",value = f"`{otvet['answer']}`")
				await ctx.channel.send(embed = em)
				count = count + 1 #вступаем в следующий раунд
				await asyncio.sleep(1)
				if count == 11: #проверка
					e = discord.Embed(title = "**Конец игры!**", description = f"**Ивент был проведён {ctx.author.mention}, и мы всем желаем удачи! Спасибо за участие!**\n ||Подождите когда пройдёт подсчёт баллов||", color=0xa400fc)
					await ctx.send(embed = e)

	

	@commands.command(aliases = ['g'])
	@commands.has_any_role(764776537600950286)
	async def giveaway( self, ctx, seconds: int, *, text ):
		def time_end_form( seconds ):
			h = seconds//3600
			m = (seconds - h*3600)//60
			s = seconds%60
			if h < 10:
				h = f"0{h}"
			if m < 10:
				m = f"0{m}"
			if s < 10:
				s = f"0{s}"
			time_reward = f"{h} : {m} : {s}"
			return time_reward
 
		author = ctx.message.author
		time_end = time_end_form(seconds)
		msgs = '<@&763389887272976385>'
		message = await ctx.send(embed = discord.Embed(
			description = f"**Разыгрывается : `{text}`\nЗавершится через: `{time_end}` \n\nОрганизатор: {author.mention} \nДля участия нажмите на реакцию ниже.**",
			colour = 0xa400fc), content=msgs)
		await message.add_reaction("🎉")
		while seconds > -1:
			time_end = time_end_form(seconds)
			text_message = discord.Embed(
				description = f"**Разыгрывается: *_{text}_*\nЗавершится через: `{time_end}` \n\nОрганизатор: {author.mention} \nДля участия нажмите на реакцию ниже.**",
				colour = 0xa400fc)
			await message.edit(embed = text_message)
			await asyncio.sleep(1)
			seconds -= 1
			if seconds < -1:
				break
		channel = message.channel
		message_id = message.id
		message = await channel.fetch_message(message_id)
		reaction = message.reactions[ 0 ]
 
		users = await reaction.users().flatten()
		if reaction.count == 1:
 
			win = discord.Embed(
				description = f'**В этом розыгрыше нет победителя!**',
				colour = 0xa400fc)
			await message.edit(embed = win)
		else:
			user_win = random.choice(users)
			while str(user_win.id) == str(self.bot.user.id):
				user_win = random.choice(users)
		
			win = discord.Embed(
				description = f'**Розыгрыш завершён!\nПобедитель розыгрыша: {user_win.mention}!\nНапишите организатору, {author.mention}, чтобы получить награду.**',
				colour = 0xa400fc)
			await message.edit(embed = win)

def setup(bot):
	bot.add_cog(event(bot))
	print("[SplashBot] Ког: Ивент. Загружен")
