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

res  = 684724479209111563

class event(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command() # создаём команду
	async def флаги(self, ctx): # функцию
		event_members = {} # создаём словарь, он нужен для того, чтобы подсчитывать баллы каждого участника игры
		with open('flags.json','r',encoding='utf8') as f: # открываем файл с кодировкой utf8, чтобы всё было ок
			flags = json.load(f) # превращаем в словарь
			count = 1 # подсчёт раундов
			while count <= 10: # всего 10 раундов, Вы можете изменить это значение
				otvet = random.choice(flags['Флаги']) # выбираем рандомный флаг, который скинет бот и будет ожидать ответа к нему (всё из файла flags.json)
				e = discord.Embed(title = f"Флаг {count}") # создаём эмбед, с названием "Флаг №", на месте номера будет число раунда
				e.set_image(url = otvet['url']) # ставит изображение, взяв ссылку из файла flags.json
				await ctx.send(embed = e) # отправляет эмбед
				def check(m):
					return otvet['answer'] in m.content or otvet['answer'].capitalize() in m.content or otvet['answer'].lower() in m.content or otvet['answer'].upper() in m.content and ctx.channel == ctx.channel

				msg = await self.client.wait_for('message', check=check) # ожидает ответа
				if str(msg.author.id) not in event_members: # проверка на то, есть ли автор ответа в нашем созданном ранее словаре, если нет то заносит и даёт количество очков 1
					event_members[str(msg.author.id)] = {} # заносим в словарь
					event_members[str(msg.author.id)]["score"] = 1 # количество очков задаём
				elif str(msg.author.id) in event_members: # если автор ответа уже есть в ранее созданном словаре - срабатывает эта проверка
					event_members[str(msg.author.id)]["score"] += 1 # добавляет 1 очко
				em = discord.Embed(title = "Правильный ответ!") # создаём эмбед, который говорит о том что был правильный ответ
				em.add_field(name = "Ответил:", value = f"{msg.author.mention}") # кто ответил
				em.add_field(name = "Правильный ответ:",value = f"{otvet['answer']}") # какой правильный ответ
				await ctx.channel.send(embed = em) # отправляет
				count = count + 1 # следующий раунд
				await asyncio.sleep(1) # ждём, чтобы всё слишком быстро не было
				if count == 11: # если так называемый 11 раунд (конец по умолчанию) то эта проверка срабатывает
					e = discord.Embed(title = "Конец игры!", description = f"Таблица лидеров:") # создаёт эмбед с таблицой участников, и их баллами
					leaders = sorted(event_members, key=lambda score: event_members[score]['score'], reverse=True) # сортирует словарь по ключу score (очки)
					position = 1 # начинаем с 1 чела в таблице
					for leader in leaders: # создаём цикл для перебора словаря
						leader = self.client.get_user(int(leaders[position-1])) # получаем человека
						leader_score = event_members[str(leader.id)]['score'] # получаем очки этого человека
						e.add_field(name=f"{position} место:", value=f"{leader.mention} | очки: **{leader_score}**",inline=False) # заносим в его нашу таблицу
						position += 1 # строчка, чтобы далее перебирать всех
					await ctx.send(embed = e) # отправляет эмбед объявляя конец
					return # конец, ценок!

	

	@commands.command(aliases = ['g'])
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
