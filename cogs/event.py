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

class event(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def флаги(self, ctx):
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

	@commands.command()
	@commands.has_any_role(762695458920726528, 632650506707140618)
	async def say(self, ctx, *, arg):
		await ctx.message.delete()
		await ctx.send(embed = discord.Embed(description = f'{arg}', color=0xa400fc))
	


	@commands.command()
	@commands.has_any_role(762695458920726528, 632650506707140618)
	async def event(self, ctx):
		embed = discord.Embed(
			colour = discord.Colour.green()
		)
		embed.set_image(url=link)
		await ctx.send(embed = embed)

	

	@commands.command()
	@commands.has_any_role(762695458920726528, 632650506707140618)
	async def event(self, ctx):
		top = discord.Embed(description = f'**1. Музыка**\n**2. Uno**\n**3. Угадай Флаг**\n**4. Дорисуй-ка**\n**5. Придумай слово**', color=0xa400fc)
		music = discord.Embed(title='**Музыка**', description='Участники должны угадать музыку по словам. __**Кто угадает, получает +1 балл**__\nПравила \n 1. Запрещено использовать любой сайт или приложение для узнавания музыки (Дисквалификация)', color=0xa400fc)
		Uno = discord.Embed(title='**Uno**', description='Участник должен выиграть других людей в Uno.', color=0xa400fc)
		flag = discord.Embed(title='**Угадай Флаг**', description='Участники должны угадать флаг по картинке. __**Кто угадает, получает +1 балл**__', color=0xa400fc)
		paint = discord.Embed(title='**Дорисуй-ка**', description='Ведущий должен нарисовать что-то, а участники должны дорисовать что-то красивое.\nПравила \n 1. Запрещено рисовать слова с матами(Дисквалификация+Мут)\n 2. Запрещено рисовать гениталии(Дисквалификация+Мут)', color=0xa400fc)
		slovo = discord.Embed(title='**Угадай слово**', description='Участники должны понять что за слово придумал ведущий. __**Кто угадает, получает +1 балл**__', color=0xa400fc)
		msgs = '<@&759446462022549555>'
		channel = self.bot.get_channel(759064771428614195)
		msg = await ctx.send(embed=top)
		await msg.add_reaction("1️⃣")
		await msg.add_reaction("2️⃣")
		await msg.add_reaction("3️⃣")
		await msg.add_reaction("4️⃣")
		await msg.add_reaction("5️⃣")
		def check(reaction, user):
			return user.id == ctx.author.id and reaction.message.id == msg.id
		try:
			rea, use = await self.bot.wait_for('reaction_add', check=check, timeout=30.0)
		except asyncio.TimeoutError:
			await msg.delete()
		if rea.emoji == '1️⃣':
			await ctx.channel.purge( limit = 1 )
			await channel.send(embed=music,content=msgs)
			await msg.clear_reactions()
		elif rea.emoji == '2️⃣':
			await ctx.channel.purge( limit = 1 )
			await channel.send(embed=Uno,content=msgs)
			await msg.clear_reactions()
		elif rea.emoji == '3️⃣':
			await ctx.channel.purge( limit = 1 )
			await channel.send(embed=flag,content=msgs)
			await msg.clear_reactions()
		elif rea.emoji == '4️⃣':
			await ctx.channel.purge( limit = 1 )
			await channel.send(embed=paint,content=msgs)
			await msg.clear_reactions()
		elif rea.emoji == '5️⃣':
			await ctx.channel.purge( limit = 1 )
			await channel.send(embed=slovo,content=msg)
			await msg.clear_reactions()
		else:
			pass

	@commands.command()
	@commands.has_any_role(762695458920726528, 632650506707140618)
	async def events(self, ctx):
		events = ["Музыка", "Uno", "Угадай флаг", "Дорисуй-ка", "Придумай слово"]
		e1 = random.choice(events)
		e2 = random.choice(events)
		e3 = random.choice(events)
		if e1 == e2 or e3:
			ee1 = random.choice(events)
			await asyncio.sleep(0.5)
		if e2 == e1 or e3:
			ee2 = random.choice(events)
			await asyncio.sleep(0.5)
		if e3 == e2 or e1:
			ee3 = random.choice(events)
			await asyncio.sleep(0.5)

		ees1 = ee1
		ees2 = ee2
		ees3 = ee3
		if ees1 == ees2 or ees3:
			eee1 = random.choice(events)
			await asyncio.sleep(0.5)
		if ees2 == ees1 or ees3:
			eee2 = random.choice(events)
			await asyncio.sleep(0.5)
		if ees3 == ees2 or ees1:
			eee3 = random.choice(events)
			await asyncio.sleep(0.5)
		eees1 = eee1
		eees2 = eee2
		eees3 = eee3
		if eees1 == eees2 or eees3:
			eeee1 = random.choice(events)
			await asyncio.sleep(0.5)
		if eees2 == eees1 or eees3:
			eeee2 = random.choice(events)
			await asyncio.sleep(0.5)
		if eees3 == eees2 or eees1:
			eeee3 = random.choice(events)
			await asyncio.sleep(0.5)
		await ctx.send(embed = discord.Embed(description = f'{eeee1}\n{eeee2}\n{eeee3}', color=0xa400fc))

	@commands.command()
	async def even(self, ctx):
		embed = discord.Embed(title=f'Аватар пользователя', color= 0xa400fc)

		embed.set_image(url='https://cdn.discordapp.com/attachments/765186831385231370/765192362506715166/30.png')
		await ctx.send(embed = embed)

	@commands.command(aliases = ['g'])
	@commands.has_any_role(632652083228573741, 632650509487964180, 632650506707140618)
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

	@commands.command()
	async def ehelp(self, ctx):
		embed = discord.Embed(title='**Помощь**', description='***Навигация по секретным командам для ивентеров :gear:\n () - Обязательные параметры\n [] - Необязательные параметры***\n *P.S: Листай с помощью эмодзи*', color=0xa400fc)
		embed1 = discord.Embed(title='**Музыка**', description='\n', color=0xa400fc)
		embed2 = discord.Embed(title='**Основные :bulb:**', description='`-botinfo` **- Показывает информацию о боте**\n `-today` **- Показывает события сегодняшнего дня в мировой истории** \n `-wiki (text)` **- Показывает самую популярную статью в википедии по запросу**\n `-news` **- Показывает нынешние важные события во всём мире**\n `-facts` **- Показывает интересные факты из википедии**\n `-image` **- Показывает изображение дня**\n'
			'`-translate (lang) (text)` **- Перевести сообщение**\n `-avatar [@user]` **- Показывает аватар**\n `-count` **- Калькулятор**', color=0xa400fc)

		embeds = [embed, embed1, embed2]

		message = await ctx.send(embed=embed)
		page = Paginator(self.bot, message, only=ctx.author, embeds=embeds, time_stamp=False)
		await page.start()

def setup(bot):
	bot.add_cog(event(bot))
	print("[SplashBot] Ког: Ивент. Загружен")
