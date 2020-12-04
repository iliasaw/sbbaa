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



def bytes2human(number, typer=None):
	# Пример Работы Этой Функции перевода чисел:
	# >> bytes2human(10000)
	# >> '9.8K'
	# >> bytes2human(100001221)
	# >> '95.4M'

	if typer == "system":
		symbols = ('KБ', 'МБ', 'ГБ', 'TБ', 'ПБ', 'ЭБ', 'ЗБ', 'ИБ')  # Для перевода в Килобайты, Мегабайты, Гигобайты, Террабайты, Петабайты, Петабайты, Эксабайты, Зеттабайты, Йоттабайты
	else:
		symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')  # Для перевода в обычные цифры (10k, 10MM)

	prefix = {}

	for i, s in enumerate(symbols):
		prefix[s] = 1 << (i + 1) * 10

	for s in reversed(symbols):
		if number >= prefix[s]:
			value = float(number) / prefix[s]
			return '%.1f%s' % (value, s)

	return f"{number}B"
connection = sqlite3.connect('data.db')
cursor = connection.cursor()




class allсommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.cog_name = ["Commands"]


	
		

	@commands.command(aliases=['help', 'хелп'])
	async def shelp(self, ctx):
		embed = discord.Embed(title='**Помощь**', description='***Навигация по секретным командам :gear:\n () - Обязательные параметры\n [] - Необязательные параметры***\n *P.S: Листай с помощью эмодзи*', color=0xa400fc)
		embed1 = discord.Embed(title='**Развлечение :balloon:**', description='\n `#ttt (@user)` **- Сыграть с человеком в крестики нолики**\n `#coin` **- Подкинуть монетку**\n `#rand (number1) (number2)` **- Рандомайзер**\n `#caesar (arg)` **- Зашифровать шифром цезаря**\n `#reverse (text)` **- Зазеркалить слово**\n `#rps (arg)` **- Камень Ножницы Бумага**\n'
			'`#panda` **- Показывет панду**\n `#bird` **- Показывает птичку**\n `#fox` **- Показывает лисичку**\n `#cat` **- Показать котика**\n `#koala` **- Показать коалу**\n `#dog` **- Показать собачку**\n `#invert [@user]` **- Инвертировать**\n `#wasted [@user]` **- Арестовать**\n `#greyscale [@user]` **- Чёрно-Белое**', color=0xa400fc)
		embed2 = discord.Embed(title='**Основные :bulb:**', description='`#botinfo` **- Показывает информацию о боте**\n `#today` **- Показывает события сегодняшнего дня в мировой истории** \n `#wiki (text)` **- Показывает самую популярную статью в википедии по запросу**\n `#news` **- Показывает нынешние важные события во всём мире**\n `#facts` **- Показывает интересные факты из википедии**\n `#image` **- Показывает изображение дня**\n'
			'`#translate (lang) (text)` **- Перевести сообщение**\n `#avatar [@user]` **- Показывает аватар**\n`#server` **- показывает информацию о сервере**\n `#suggest (idea)` **- Предложить идею боту**', color=0xa400fc)

		embeds = [embed, embed1, embed2]

		message = await ctx.send(embed=embed)
		page = Paginator(self.bot, message, only=ctx.author, embeds=embeds, time_stamp=False)
		await page.start()

	@commands.command(aliases=['арестован'])
	async def wasted(self, ctx, member : discord.Member = None):

		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))

		user = ctx.message.author if (member == None) else member

		embed = discord.Embed(description=f'**{user.mention} арестован**', color= 0xa400fc)

		embed.set_image(url='https://some-random-api.ml/canvas/wasted?avatar=https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024'.format(user))

		await ctx.send(embed=embed)

	@commands.command(aliases=['инверт', 'инвертировать'])
	async def invert(self, ctx, member : discord.Member = None):

		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))

		user = ctx.message.author if (member == None) else member

		embed = discord.Embed(description=f'**{user.mention} инвертирован**', color= 0xa400fc)

		embed.set_image(url='https://some-random-api.ml/canvas/invert?avatar=https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024'.format(user))

		await ctx.send(embed=embed)
	
	@commands.command(aliases=['серый'])
	async def greyscale(self, ctx, member : discord.Member = None):

		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))

		user = ctx.message.author if (member == None) else member

		embed = discord.Embed(description=f'**{user.mention} Hello Darkness Smile Friend**', color= 0xa400fc)

		embed.set_image(url='https://some-random-api.ml/canvas/greyscale?avatar=https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024'.format(user))

		await ctx.send(embed=embed)

	@commands.command()
	async def avatar(self, ctx, member : discord.Member = None):

		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))

		user = ctx.message.author if (member == None) else member

		embed = discord.Embed(title=f'Аватар пользователя {user}', color= 0xa400fc)

		embed.set_image(url='https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024'.format(user))

		await ctx.send(embed=embed)





	@commands.command()
	async def suggest(self, ctx , * , agr ):
		await ctx.message.add_reaction('✅')
		suggest_chanell = self.bot.get_channel( 771809550273085550 ) #Айди канала предложки
		embed = discord.Embed(title=f"{ctx.author.name} Предложил :", description= f" {agr} \n\n")

		embed.set_thumbnail(url=ctx.guild.icon_url)

		message = await suggest_chanell.send(embed=embed)
		await message.add_reaction('✅')
		await message.add_reaction('❎')




	@commands.command()
	async def password(self, ctx, lenght: int = None, number: int = None):

		if not lenght or not number:
			await ctx.send(embed = discord.Embed(description = f'Пожалуйста, укажите длину пароля и количество символов в нем.', color=0xa400fc)) 

		chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
		for x in range(number):
			password = ''

			for i in range( lenght ):
				password += random.choice(chars)

			await ctx.message.add_reaction('✅')

			await ctx.message.author.send(embed = discord.Embed(description = f'**Сгенерированный пароль:**\n``{password}``', color=0xa400fc))
			print(f'Сгенерированный пароль у {ctx.message.author}:{password}')
			return

	@commands.command(
	aliases=['сервер', 'серверинфо'])
	async def server(self, ctx):
		members = ctx.guild.members
		bots = len([m for m in members if m.bot])
		users = len(members) - bots
		online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
		offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
		idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
		dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
		allvoice = len(ctx.guild.voice_channels)
		alltext = len(ctx.guild.text_channels)
		allroles = len(ctx.guild.roles)
	 
		embed = discord.Embed(title=f"{ctx.guild.name}", color=0xa400fc, timestamp=ctx.message.created_at)
		embed.set_thumbnail(url=ctx.guild.icon_url)
	 
		embed.add_field(name=f"Пользователей", value=f"<:user:771689279667699722> Участников: **{users}**\n"
												f"<:bot:771689206434234368> Ботов: **{bots}**\n"
												f"<:online1:771689227926765578> Онлайн: **{online}**\n"
												f"<:online2:771689242685603880> Отошёл: **{idle}**\n"
												f"<:online3:771689252261330975> Не Беспокоить: **{dnd}**\n"
												f"<:noonline2:771689217641938975> Оффлайн: **{offline}**")
	 
		embed.add_field(name=f"Каналов", value=f"<:voice:771689271539007509> Голосовые: **{allvoice}**\n"
											 f"<:text:771689264404365322> Текстовые: **{alltext}**\n")
	 
		embed.add_field(name=f"Уровень Буста", value=f"{ctx.guild.premium_tier} (Бустеров: {ctx.guild.premium_subscription_count})")
		embed.add_field(name=f"Количество Ролей", value=f"{allroles}")
		embed.add_field(name=f"Создатель сервера", value=f"{ctx.guild.owner}")
		embed.add_field(name=f"Регион сервера", value=f"{ctx.guild.region}")
		embed.add_field(name=f"Дата создания сервера", value=f"{ctx.guild.created_at.strftime('%b %#d %Y')}")
	 
		await ctx.send(embed=embed)


	@commands.command(
		aliases=["монетка", "орел-решка", "coin"],
		description="Подкинуть монетку",
		usage="coin [Ничего]")
	async def __coin(self, ctx ):

		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		coins = [ 'Орёл', 'Решка' ]
		coins_r = random.choice( coins )
		coin_win = 'Орёл'

		if coins_r == coin_win:
			if ctx.author.id == 764776986819821569:
				await ctx.send(embed = discord.Embed(description= f''':tada: {ctx.author.mention}, выиграл! 
					Тебе повезло у тебя: **`Орёл`**''', color = 0xa400fc))
			else:
				await ctx.send(embed = discord.Embed(description= f''':tada: {ctx.author.mention}, выиграл! 
					Тебе повезло у тебя: **`{ coins_r }`**''', color = 0xa400fc))

		if coins_r != coin_win:
			if ctx.author.id == 764776986819821569:
				await ctx.send(embed = discord.Embed(description= f''':tada: {ctx.author.mention}, выиграл! 
					Тебе повезло у тебя: **`Орёл`**''', color = 0xa400fc))
			else:
				await ctx.send(embed = discord.Embed(description= f''':thumbsdown:  {ctx.author.mention}, проиграл! 
					Тебе не повезло у тебя: **`{ coins_r }`**''', color = 0xa400fc))

	@commands.command(
		aliases=["rand", "рандом", "рандомайзер", "random", "randomizer"],
		description="Рандомайзер",
		usage="рандом [первое число] [второй число]")
	async def __randomizer(self, ctx, number1=1, number2=100):
		await ctx.message.delete()
		try:
			if not number1:
				embed = discord.Embed()
				embed.set_author(name="Ошибка!",
								 icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
				embed.add_field(name="Проблема:", value="Вы забыли написать цельные числа!")
				embed.add_field(name="Решение:", value="Введите команду с 2 цельными числами (`/рандомайзер 1 10`)",
								inline=False)
				await ctx.send(embed=embed)
				return
			elif not number2:
				embed = discord.Embed()
				embed.set_author(name="Ошибка!",
								 icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
				embed.add_field(name="Проблема:", value="Отсутствует 2 число!")
				embed.add_field(name="Решение:", value="Введите 2 цельное число!", inline=False)
				await ctx.send(embed=embed)
				return
			elif int(number1) > 1_000_000 or int(number2) > 1_000_000:
				embed = discord.Embed()
				embed.set_author(name="Ошибка!",
								 icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
				embed.add_field(name="Проблема:", value="Превышение лимита!")
				embed.add_field(name="Решение:", value="Введите цельное число от 0 до 1млн!", inline=False)
				await ctx.send(embed=embed)
				return
			else:
				number1 = int(number1)
				number2 = int(number2)
				if number1 != number2:
					e = discord.Embed()
					e.set_author(name="Утилиты: рандомайзер",
								 icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
					e.add_field(name="‎‎‎‎", value=f"{random.randint(number1, number2)}")
					e.add_field(name="Число:", value=f" {random.randint(number1, number2)}")
					e.add_field(name="‎‎‎‎", value=f"{random.randint(number1, number2)}")
					message_with_random = await ctx.send(embed=e)
					popitka = 0
					while popitka < 4:
						em = discord.Embed()
						em.set_author(name="Утилиты: рандомайзер",
									  icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
						em.add_field(name="‎‎‎‎", value=f"{random.randint(number1, number2)}")
						em.add_field(name="Число:", value=f" {random.randint(number1, number2)}")
						em.add_field(name="‎‎‎‎", value=f"{random.randint(number1, number2)}")
						await message_with_random.edit(embed=em)
						popitka += 1
						await asyncio.sleep(0.3)
					if popitka == 4:
						em = discord.Embed()
						em.set_author(name="Утилиты: рандомайзер",
									  icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
						em.add_field(name="‎‎‎‎", value=f"{random.randint(number1, number2)}")
						em.add_field(name="Число:", value=f"__** {random.randint(number1, number2)}**__")
						em.add_field(name="‎‎‎‎", value=f"{random.randint(number1, number2)}")
						await message_with_random.edit(embed=em)
				elif number1 == number2:
					e = discord.Embed()
					e.set_author(name="Ошибка!",
								 icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
					e.add_field(name="Проблема:", value="Указанные аргументы одинаковы!")
					e.add_field(name="Решение:",
								value="Введите 2 разных цельных числа, чтобы бот смог создать диапазон из чисел",
								inline=False)
					await ctx.send(embed=e)
		except ValueError:
			e = discord.Embed()
			e.set_author(name="Ошибка!",
						 icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
			e.add_field(name="Проблема:", value="Введено не цельное число!")
			e.add_field(name="Решение:", value="Введите цельное число!", inline=False)

	@commands.command()
	async def avatar(self, ctx, member : discord.Member = None):

		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))

		user = ctx.message.author if (member == None) else member

		embed = discord.Embed(title=f'Аватар пользователя {user}', color= 0xa400fc)

		embed.set_image(url='https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024'.format(user))

		await ctx.send(embed=embed)



	@commands.command(
		aliases=["цезарь", "caesar"],
		description="Зашифровать слово с помощью шифра цезаря",
		usage="caesar [слово]")
	async def __caesar(self, ctx, arg):
		alfpabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',
		 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
		key = int(3)
		word = str(arg)
		decrypt = []

		for i in word:
			decrypt.append(i)

		decrypted = []

		for i in decrypt:
			for j in alfpabet:
				if i == j:
					position = alfpabet.index(j)
					newposition = position + key
					decrypted.append(alfpabet[newposition])
					break
				if i == ' ':
					decrypted.append(i)
					break
		decrypted1 = ''.join(decrypted)
		await asyncio.sleep(0.3)
		await ctx.send(embed = discord.Embed(description= f'**Ваше слово:** `{decrypted1}`', color = 0xa400fc))

	@commands.command(
		aliases=["reverse", "ревёрс"],
		description="Зазеркалить слово",
		usage="reverse [слова]")
	async def __reverse(self, ctx, *, arg):
		text = arg[::-1]

		await ctx.send(embed = discord.Embed(description= f'**Ваше слова(-о):** `{text}`', color = 0xa400fc))

	@commands.command(
		aliases=["chatbot", "чатбот"],
		description="Зазеркалить слово",
		usage="chatbot [слова]")
	async def __chatbot(self, ctx, *, arg):
		r = requests.get("https://some-random-api.ml/chatbot", params = {"message": arg})
		await ctx.send(json.loads(r.text)["response"])

	@commands.command(aliases=['calculator'])
	async def calc(self, ctx, *,exp = None):
		if exp is None:
			await ctx.send('**Укажите пример!**')
		else:
			link = 'http://api.mathjs.org/v4/'

			data = {"expr": [f"{exp}"]}

			try:
				re = requests.get(link, params=data)
				responce = re.json()

				e = discord.Embed(title='Калькулятор', color = 0xa400fc)
				e.add_field(name='Задача:', value=exp)
				e.add_field(name='Решение:', value=str(responce))
				await ctx.send(embed=e)
			except:
				await ctx.send('**Это калькулятор, текст нельзя -.-**')

	@commands.command()
	async def user(self, ctx, member: discord.Member = None ):

		user = ctx.message.author if (member == None) else member

		roles = (role for role in user.roles )
		emb = discord.Embed(title='Информация о пользователе.'.format(user.name), description=f":clock: **Участник зашёл на сервер:** ``{user.joined_at.strftime('%A %b %#d, %Y')}``\n\n "
																							f":slight_smile: **Имя:** ``{user.name}``\n\n"
																							f":wink: **Никнейм:** ``{user.nick}``\n\n"
																							f":green_apple:  **Статус:** ``{user.status}``\n\n"
																							f":desktop: **Активность:** ``{user.activity}``\n\n"
																							f":credit_card: **ID:** ``{user.id}``\n\n"
																							f":mountain: **Высшая роль: {user.top_role.mention}**\n\n"
																							f":timer: **Аккаунт создан:** ``{user.created_at.strftime('%A %b %#d, %Y')}``", 
																							color=0xa400fc, timestamp=ctx.message.created_at)
		emb.set_thumbnail(url= user.avatar_url)
		emb.set_footer(icon_url= user.avatar_url)
		emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
		await ctx.send(embed=emb)

	


		
	@commands.command(aliases=["bot", "botinfo", "ботинфо"])
	async def _bot(self, ctx):
		await ctx.message.delete()
 
		members_count = 0
		guild_count = len(self.bot.guilds)
 
		for guild in self.bot.guilds:
			members_count += len(guild.members)
 
		embed1 = discord.Embed(title=f"{self.bot.user.name}#{self.bot.user.discriminator}",
							   description="Информация о боте **WinterBpt**.\nБот был написан для сервера Winter!",
							   color=0xa400fc)
		embed1.add_field(name=f'Бота создал:', value="<@764776986819821569>", inline=True)  # Создает строку
		embed1.add_field(name=f'Самый Лучший Человек:', value="<@369886134861561858>", inline=True)  # Создает строку
		embed1.add_field(name="‎‎‎‎", value="‎", inline=True)
		embed1.add_field(name=f'Бот написан на:', value="Discord.py", inline=True)  # Создает строку
		embed1.add_field(name=f'Лицензия:', value="CC BY-SA-NC", inline=True)  # Создает строку
		embed1.add_field(name="‎‎‎‎", value="‎", inline=True)
		embed1.add_field(name=f'Серверов:', value=f"{guild_count}", inline=True)  # Создает строку
		embed1.add_field(name=f'Шардов:', value=f"{self.bot.shard_count}", inline=True)  # Создает строку
		embed1.add_field(name=f'Сервер Winter:', value="[Тык](https://discord.gg/jNuEDPHhfX)",
						 inline=True)  # Создает строку
		embed1.set_thumbnail(url=self.bot.user.avatar_url)
 
		# ==================
 
		mem = ps.virtual_memory()
		ping = self.bot.latency
 
		ping_emoji = "🟩🔳🔳🔳🔳"
		ping_list = [
			{"ping": 0.00000000000000000, "emoji": "🟩🔳🔳🔳🔳"},
			{"ping": 0.10000000000000000, "emoji": "🟧🟩🔳🔳🔳"},
			{"ping": 0.15000000000000000, "emoji": "🟥🟧🟩🔳🔳"},
			{"ping": 0.20000000000000000, "emoji": "🟥🟥🟧🟩🔳"},
			{"ping": 0.25000000000000000, "emoji": "🟥🟥🟥🟧🟩"},
			{"ping": 0.30000000000000000, "emoji": "🟥🟥🟥🟥🟧"},
			{"ping": 0.35000000000000000, "emoji": "🟥🟥🟥🟥🟥"}
		]
		for ping_one in ping_list:
			if ping <= ping_one["ping"]:
				ping_emoji = ping_one["emoji"]
				break
 
		embed2 = discord.Embed(title='Статистика Бота', color=0xa400fc)
 
		embed2.add_field(name='Использование CPU',
						 value=f'В настоящее время используется: {ps.cpu_percent()}%',
						 inline=True)
 
		embed2.add_field(name='Использование RAM',
						 value=f'Доступно: {bytes2human(mem.available, "system")}\n'
							   f'Используется: {bytes2human(mem.used, "system")} ({mem.percent}%)\n'
							   f'Всего: {bytes2human(mem.total, "system")}',
						 inline=True)
 
		embed2.add_field(name='Пинг Бота',
						 value=f'Пинг: {ping * 1000:.0f}ms\n'
							   f'{ping_emoji}',
						 inline=True)
 
		embeds = [embed1, embed2]
 
		message = await ctx.send(embed=embed1)
		page = Paginator(self.bot, message, only=ctx.author, embeds=embeds, time_stamp=False)
		await page.start()

	@commands.command(aliases=["rps", "кнб", "knb"],
		description="Камень, ножницы, бумага",
		usage="rps [Камень, ножницы, бумага]")
	async def __rps(self, ctx, *, mess):
		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		robot = ['Камень', 'Ножницы', 'Бумага']
		if mess == "Камень" or mess == "К" or mess == "камень" or mess == "к":
			robot_choice = random.choice(robot)
			emb = discord.Embed(title = robot_choice, colour = 0xa400fc)
			if robot_choice == 'Ножницы':
				emb.add_field(name = '✂', value = 'Вы выиграли!')
			elif robot_choice == 'Бумага':
				emb.add_field(name = '📜', value = 'Вы проиграли :с')
			else:
				emb.add_field(name = '🗿', value = 'Ничья!')
			await ctx.send(embed = emb)

		elif mess == "Бумага" or mess == "Б" or mess == "бумага" or mess == "б":
			robot_choice = random.choice(robot)
			emb = discord.Embed(title = robot_choice, colour = 0xa400fc)
			if robot_choice == 'Ножницы':
				emb.add_field(name = '✂', value = 'Вы проиграли :с')
			elif robot_choice == 'Камень':
				emb.add_field(name = '🗿', value = 'Вы выиграли!')
			else:
				emb.add_field(name = '📜', value = 'Ничья!')
			await ctx.send(embed = emb)
			
		elif mess == "Ножницы" or mess == "Н" or mess == "ножницы" or mess == "н":
			robot_choice = random.choice(robot)
			emb = discord.Embed(title = robot_choice, colour = 0xa400fc)
			if robot_choice == 'Бумага':
				emb.add_field(name = '📜', value = 'Вы выиграли!')
			elif robot_choice == 'Камень':
				emb.add_field(name = '🗿', value = 'Вы проиграли :с')
			else:
				emb.add_field(name = '✂', value = 'Ничья!')
				await ctx.send(embed = emb)

	


def setup(bot):
	bot.add_cog(allсommands(bot))
	print("[SplashBot] Ког: Команды. Загружен")
