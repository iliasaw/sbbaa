import discord
from discord.ext import commands
from Cybernator import Paginator
import json
import requests
import googletrans
from googletrans import Translator
from datetime import timedelta


class scripts(commands.Cog):

	def __init__(self, bot):
		self.bot = bot




	translator = Translator()

	@commands.Cog.listener()
	async def is_owner(ctx):
		return ctx.author.id == 342317507991961602
	 # Айди создателя бота


	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		embed = discord.Embed(
			title=("SplashBot"),
			description=f"Добрый день!\n\n Вы получили это сообщение т.к на ваш сервер **{guild.name}** был добавлен SplashBot.\nЭто чисто информативное сообщение, сделанное для того, чтобы вы знали немного больше о том, чем пользуетесь.",
			color=0x800080
		)
		embed.add_field(
			name="Полезная информация:",
			value=f"Создатель бота - <@342317507991961602>\n Префикс - `-`\n Справка по командам - `-help`\n **Приятного использования SplashBot**"
		)
		embed.set_footer(
			text='ⓥⓞⓓⓚⓐ#2362 © | Все права защищены',
			icon_url=self.bot.user.avatar_url
		)

		await guild.owner.send(embed=embed)
		channel = self.bot.get_channel(702844002684370945)
		j_e = discord.Embed(
			title=f"Бот присоединился к серверу {guild.name}",
			description=f"**Информация о сервере:**\n\nСервер - {guild.name}\nID сервера - {guild.id}\nВладелец сервера - {guild.owner}",
		)
		await channel.send(embed=j_e)



	@commands.command(aliases=['scripts'])
	async def скрипты(self, ctx):

		embed = discord.Embed(title='**Страницы**', description='\n\n `1` **- 1 Страница: 1 - 20**\n `2` **- 2 Страница: 21 - 32**'    	
			'\n\n **F.A.Q** \n\n ```Мы не несём ответственность если вас забанят в роблоксе. Мы лишь даём вам скрипты. Скрипты проверялись на EasyExploit API. Используйте команду -script и цифру скрипта, вот так: -script 22. Я буду выдавать пред тем кто не читает FAQ и пишет к примеру: -dungeon quest```'
			'\n\n ```Скрипты обновляются каждый день и добавляются новые.Просьба не копировать названиe на сайте по типу: 🔥Z X-LEGENDS!⚡Ninja Legends.```', color=0xa400fc)
		embed1 = discord.Embed(title='**Страница 1**', description='`1` **- Flee the Facility**\n `2` **- Arsenal**\n `3` **- CB:RO**\n `4` **- Murder Mystery**\n `5` **- Work At A Pizza Place**\n `6` **- Tower of Hell**\n `7` **- 2 Player Ninja Tycoon**\n `8` **- Speed Run 4**\n `9` **- S.W.A.T Simulator**\n `10` **- The Crusher**\n `11` **- Hole Simulator**\n `12` **- Lifting Simulator**\n `13` **- Break In**\n `14` **- Doomspire Brickbattle**\n `15` **- Breaking Point**\n `16` **- Survive and Kill the Killers in Area 51**\n `17` **- Sky Wars**\n `18` **- KAT**\n `19` **- Be A Parkour Ninja**\n `20` **- Project Lazarus**', color=0xa400fc)
		embed2 = discord.Embed(title='**Страница 2**', description='`21` **- RGranny**\n `22` **- Zombie Rush**\n `23` **- Car Crushers 2**\n `24` **- Mad Paintball 2**\n `25` **- Zombie Strike**\n `26` **- Driving Simulator**\n `27` **- Survive the Killer**\n `28` **- Field Trip Z**\n `29` **- Super Power Fighting Simulator**\n `30` **- Wizard Simulator**\n `31` **- A Wolf Or Other**\n `32` **- Army Tycoon**\n `33` **- Super Power Training Simulator**', color=0xa400fc)
		embeds = [embed, embed1, embed2]

		message = await ctx.send(embed=embed)
		page = Paginator(self.bot, message, only=ctx.author, embeds=embeds, time_stamp=False)
		await page.start()
	
	@commands.command(aliases=['script'])
	async def скрипт(self, ctx, *, amount):
		if ctx.author.id == 465390488963514368:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))

		if ctx.author.id == 655034611889471498:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))

	
		if amount == '1':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Flee_the_Facility.txt'))

		if amount == '2':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Arsenal.txt'))

		if amount == '3':
			await ctx.channel.send(file = discord.File(fp = 'scripts/fps_gui.txt'))

		if amount == '4':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Murder Mystery.txt'))
		if amount == '5':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Work At A Pizza Place.txt'))

		if amount == '6':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Tower of Hell.txt'))
		if amount == '7':
			await ctx.channel.send(file = discord.File(fp = 'scripts/2 Player Ninja Tycoon.txt'))
		if amount == '8':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Speed Run 4.txt'))
		if amount == '9':
			await ctx.channel.send(file = discord.File(fp = 'scripts/S.W.A.T Simulator.txt'))
		if amount == '10':
			await ctx.channel.send(file = discord.File(fp = 'scripts/The Crusher.txt'))
		if amount == '11':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Hole Simulator.txt'))
		if amount == '12':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Lifting Simulator1.txt'))
			await ctx.channel.send(file = discord.File(fp = 'scripts/Lifting Simulator2.txt'))
		if amount == '13':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Break In.txt'))
		if amount == '14':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Doomspire Brickbattle.txt'))
		if amount == '15':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Breaking Point.txt'))
		if amount == '16':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Survive and Kill the Killers in Area 51.txt'))
		if amount == '17':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Sky Wars.txt'))
		if amount == '18':
			await ctx.channel.send(file = discord.File(fp = 'scripts/KAT (Press 2).txt'))
		if amount == '19':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Be A Parkour Ninja.txt'))
		if amount == '20':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Project Lazarus.txt'))
		if amount == '21':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Granny.txt'))
		if amount == '22':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Zombie Rush.txt'))
		if amount == '23':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Car Crushers 2.txt'))
		if amount == '24':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Mad Paintball 2.txt'))
		if amount == '25':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Zombie Strike.txt'))
		if amount == '26':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Driving Simulator.txt'))
		if amount == '27':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Survive the Killer.txt'))
		if amount == '28':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Field Trip Z.txt'))
		if amount == '29':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Super Power Fighting Simulator.txt'))
		if amount == '30':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Wizard Simulator.txt'))
		if amount == '31':
			await ctx.channel.send(file = discord.File(fp = 'scripts/A Wolf Or Other.txt'))
		if amount == '32':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Army Tycoon.txt'))
		if amount == '33':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Super Power Training Simulator.txt'))

	@commands.command(aliases=['сновости'])
	async def snews(self, ctx, amount, *, reason):
			

		scripts = self.bot.get_channel(728496532529217558)
		
		role = ctx.guild.get_role(733966022008111224)
		
		msg = (f"{role.mention}")
		
		embed = discord.Embed(description=f'```fix\n Обновление скрипта```\n\n **Был переделан скрипт на игру:** `{reason}`', color=0xa400fc)
		emb = discord.Embed(description=f'```yaml\n Добавление скрипта```\n\n **Был добавлен скрипт на игру:** `{reason}`', color=0xa400fc)
		embedd = discord.Embed(description=f'```fix\n Добавление скрипта к цифре```\n\n **Был добавлен скрипт к игре:** `{reason}`', color=0xa400fc)

		if amount == '1':
			await scripts.send(embed=embed,content=msg)
		if amount == '2':
			await scripts.send(embed=emb,content=msg)
		if amount == '3':
			await scripts.send(embed=embedd,content=msg)


	@commands.command(aliases=['найти'])
	async def search(self, ctx, *, question):
		if ctx.author.id == 465390488963514368:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		url = 'https://google.gik-team.com/?q=' + str(question).replace(' ', '+') + '+script+roblox+site%3Apastebin.com'
		await ctx.send(embed=discord.Embed(description=f'**Ссылка на поиск скрипта:** \n {url}', color=0xa400fc))


	@commands.command(aliases=['музыка'])
	async def music(self, ctx):
		if ctx.author.id == 465390488963514368:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		embed = discord.Embed(title='**Музыка**', description='Музыку вводить в специалные боксы (Boom Box)', color=0xa400fc)
		embed.set_author(name= 'Сервер бота', url='https://discord.gg/JDUjTFS')
		embed1 = discord.Embed(title='**Страница 1**', description='`1`**-** `2195981163` **- Гимн СССР**\n `2` **-** `4570427470` **- Чикибамбони**\n `3` **-** `4618705402` **- Ра-Та-Та**\n `4` **-** `1170717899` **- Надо поле притоптать**\n `5` **-** `3451822109` **- Пчеловод**\n `6` **-** `3767981596` **- Новый Мерин**\n `7` **-** `4769003793` **- Луна не знает пути**\n `8` **-** `4512058571` **- Валим на Гелике**\n `9` **-** `4775523993` **- Uno**\n'
			'`10` **-** `4624968216` **- Она-Оно**\n `11` **-** `1183241009` **- Кукушка**\n `11` **-** `4557767957` **- АнтиГерой**\n `12` **-** `3374996665` **- Укуси меня пчела**\n `13` **-** `1201137555` **- Виталя**\n `14` **-** `3585329779` **- Люби меня**\n `15` **-** `324499479` **- Хард Басс**\n `16` **-** `2183258114` **- Гиги за Шаги**\n `17` **-** `2275257213` **- Пачка Сигарет**\n `18` **-** `756453639` **- Тает Лёд**\n `19` **-** `848803701` **- Хайпанём Немножечко**\n `20` **-** `4244590201` **- Паравозик тыр тыр тыр**', color=0xa400fc)
		embed1.set_author(name= 'Сервер бота', url='https://discord.gg/JDUjTFS')
		embeds = [embed, embed1]

		message = await ctx.send(embed=embed)
		page = Paginator(self.bot, message, only=ctx.author, embeds=embeds, time_stamp=False, reactions=["<:left:735570849750581258>", "<:right:735570788526194759>"])
		await page.start()

	@commands.command(aliases=['коронавирус', 'ковид', 'cov'])
	async def covid(self, ctx, country):
		if ctx.author.id == 465390488963514368:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		for item in json.loads(requests.get("https://corona.lmao.ninja/v2/countries").text):
			if item['country'] == country: 
				embed = discord.Embed(title=f'Статистика Коронавируса | {country}', color=0xa400fc)
				embed.add_field(name='**Выздоровело:**',          value=f'`{item["recovered"]}` **человек**')
				embed.add_field(name='**Заболеваний:**',          value=f'`{item["cases"]}` **человек**')
				embed.add_field(name='**Погибло:**',              value=f'`{item["deaths"]}` **человек**')
				embed.add_field(name='**Заболеваний за сутки:**', value=f'`+{item["todayCases"]}` **человек**')
				embed.add_field(name='**Погибло за сутки:**',     value=f'`+{item["todayDeaths"]}` **человек**')
				embed.add_field(name='**Проведено тестов:**',     value=f'`{item["tests"]}` **человек**')
				embed.add_field(name='**Активные зараженные:**',  value=f'`{item["active"]}` **человек**')
				embed.add_field(name='**В тяжелом состоянии:**',  value=f'`{item["critical"]}` **человек**')
				embed.set_thumbnail(url=item["countryInfo"]['flag'])
				embed.set_footer(text="© Copyright 2020 ⓥⓞⓓⓚⓐ#2362 | Все права защищены")

				return await ctx.send(embed=embed)





	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, discord.ext.commands.errors.CommandNotFound):
			await ctx.send(embed=discord.Embed(description=f'**Команда не найдена**', color=0xa400fc))
		if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
			await ctx.send(embed=discord.Embed(description='**Не правильно введена команда.\nЧтобы узнать как вводить команду -help**', color=0xa400fc))

	@commands.command(name="Fight")
	async def FightCmd(self, ctx):
		if ctx.author.id == 465390488963514368:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))

		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		embed1 = discord.Embed(title='**Страница 1**', description='`1` **- Flee the Facility**\n `2` **- Pet Ranch 2 Simulator**\n `3` **- Parkour**\n `4` **- Arsenal**\n `5` **- CB:RO**\n `6` **- Ninja Legends**\n `7` **- Mad City**\n `8` **- Scripthub**\n `9` **- Murder Mystery**\n `10` **- Prison Life**\n `11` **- Piggy**\n `12` **- Build a Boat**\n `13` **- Dungeon Quest**\n `14` **- Fishing Simulator**\n `15` **- Blade Throwing Simulator**\n `16` **- Flood Escape 2**\n `17` **- Bee Swarm Simulator**\n `18` **- Pizza Factory Tycoon**\n `19` **- Work At A Pizza Place**\n `20` **- Texting Simulator**', color=0xa400fc)
		emb2 = discord.Embed(title='**Страницы**', description='\n\n `1` **- 1 Страница: 1 - 20**\n `2` **- 2 Страница: 21 - 40**\n `3` **- 3 Страница 41 - 60**\n `4` **- 4 Страница 61 - 80**\n `5` **- 5 Страница 81 - 84**'    	
			'\n\n **F.A.Q** \n\n ```Мы не несём ответственность если вас забанят в роблоксе. Мы лишь даём вам скрипты. Скрипты проверялись на EasyExploit API. Используйте команду -script и цифру скрипта, вот так: -script 22. Я буду выдавать пред тем кто не читает FAQ и пишет к примеру: -dungeon quest```'
			'\n\n ```Скрипты обновляются каждый день и добавляются новые.Просьба не копировать название на сайте по типу: 🔥Z X-LEGENDS!⚡Ninja Legends.```', color=0xa400fc)
		embed3 = discord.Embed(title='**Страница 3**', description='`41` **- Super Power Training Simulator**\n `42` **- Pet Simulator**\n `43` **- Boxing Simulator**\n `44` **- S.W.A.T Simulator**\n `45` **- Boss Fighting Simulator**\n `46` **- Sizzling Simulator**\n `47` **- Merge Battle Simulator**\n `48` **- The Crusher**\n `49` **- Speed Champions**\n `50` **- Superhero Simulator**\n `51` **- Hole Simulator**\n `52` **-JailBreak**\n `53` **- Lifting Simulator**\n `54` **- Horrific Housing**\n `55` **- Break In**\n `56` **- Fitness Simulator**\n `57` **- Doomspire Brickbattle**\n `58` **- Breaking Point**\n `59` **- Sky Block**\n `60` **- Survive and Kill the Killers in Area 51**', color=0xa400fc)
		embed4 = discord.Embed(title='**Страница 4**', description='`61` **- Sky Wars**\n `62` **- Knife Ability Test (KAT)**\n `63` **- Reaper Simulator 2**\n `64` **- Be A Parkour Ninja**\n `65` **- Natural Disaster Survival**\n `66` **- Weight Lifting Simulator 4**\n `67` **- Lost**\n `68` **- Zombie Attack**\n `69` **- Bakon**\n `70` **- Robot Inc**\n `71` **- Duckie Simulator**\n `72` **- Adopt Me**\n `73` **- Kitty**\n `74` **- Clicking Simulator**\n `75` **- Lucky Blocks Battlegrounds**\n `76` **- Pet Simulator 2**\n `77` **- Project Lazarus**\n `78` **- Granny**\n `79` **- Silent Assassin**\n `80` **- Knife Simulator**', color=0xa400fc)
		embed5 = discord.Embed(title='**Страница 5**', description='`81` **- Zombie Rush**\n `82` **- Car Crushers 2**\n `83` **- Mad Paintball 2**\n `84` **- Magnet Battery Simulator**', color=0xa400fc)
		msg = await ctx.send(embed=emb2)
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
			await msg.edit(embed=embed1)
			await msg.clear_reactions()
		elif rea.emoji == '2️⃣':
			await msg.edit(embed=embed2)
			await msg.clear_reactions()
		elif rea.emoji == '3️⃣':
			await msg.edit(embed=embed3)
			await msg.clear_reactions()
		elif rea.emoji == '4️⃣':
			await msg.edit(embed=embed4)
			await msg.clear_reactions()
		elif rea.emoji == '5️⃣':
			await msg.edit(embed=embed5)
			await msg.clear_reactions()
		else:
			pass

def setup(bot):
	bot.add_cog(scripts(bot))
	print("[SplashBot] Ког: Скрипты. Загружен")
