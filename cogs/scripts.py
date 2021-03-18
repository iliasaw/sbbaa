import discord
from discord.ext import commands
from Cybernator import Paginator
import json
import requests


class scripts(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def is_owner(ctx):
		return ctx.author.id == 342317507991961602
	 # Айди создателя бота



	@commands.command(aliases=['scripts'])
	async def скрипты(self, ctx):

		embed = discord.Embed(title='**Страницы**', description='\n\n `1` **- 1 Страница: 1 - 20**\n `2` **- 2 Страница: 21 - 32**'    	
			'\n\n **F.A.Q** \n\n ```Мы не несём ответственность если вас забанят в роблоксе. Мы лишь даём вам скрипты. Скрипты проверялись на EasyExploit и KRNL API. Используйте команду #script и цифру скрипта, вот так: #script 22. Я буду выдавать пред тем кто не читает FAQ и пишет к примеру: -dungeon quest```'
			'\n\n ```Скрипты обновляются каждый день и добавляются новые.Просьба не копировать названиe на сайте по типу: 🔥Z X-LEGENDS!⚡Ninja Legends.```', color=0xa400fc)
		embed1 = discord.Embed(title='**Страница 1**', description='`1` **- Flee the Facility**\n `2` **- Arsenal**\n `3` **- CB:RO**\n `4` **- Murder Mystery**\n `5` **- Work At A Pizza Place**\n `6` **- Tower of Hell**\n `7` **- 2 Player Ninja Tycoon**\n `8` **- Speed Run 4**\n `9` **- S.W.A.T Simulator**\n `10` **- The Crusher**\n `11` **- Hole Simulator**\n `12` **- Lifting Simulator**\n `13` **- Break In**\n `14` **- Doomspire Brickbattle**\n `15` **- Breaking Point**\n `16` **- Survive and Kill the Killers in Area 51**\n `17` **- Sky Wars**\n `18` **- KAT**\n `19` **- Be A Parkour Ninja**\n `20` **- Project Lazarus**', color=0xa400fc)
		embed2 = discord.Embed(title='**Страница 2**', description='`21` **- RGranny**\n `22` **- Zombie Rush**\n `23` **- Car Crushers 2**\n `24` **- Mad Paintball 2**\n `25` **- Zombie Strike**\n `26` **- Energy Assault**\n `27` **- Survive the Killer**\n `28` **- Field Trip Z**\n `29` **- Super Power Fighting Simulator**\n `30` **- Wizard Simulator**\n `31` **- A Wolf Or Other**\n `32` **- Army Tycoon**\n `33` **- Super Power Training Simulator**', color=0xa400fc)
		embeds = [embed, embed1, embed2]

		message = await ctx.send(embed=embed)
		page = Paginator(self.bot, message, only=ctx.author, embeds=embeds, time_stamp=False)
		await page.start()
	
	@commands.command(aliases=['script'])
	async def скрипт(self, ctx, *, amount):


	
		if amount == '1':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Flee_the_Facility.txt'))

		if amount == '2':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Arsenal Owl Hub.txt'))
			await ctx.channel.send(file = discord.File(fp = 'scripts/Arsenal Aim+Esp.txt'))

		if amount == '3':
			await ctx.channel.send(file = discord.File(fp = 'scripts/CBRO Esp+Aim.txt'))
			await ctx.channel.send(file = discord.File(fp = 'scripts/CBRO Owl Hub.txt'))

		if amount == '4':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Murder Mystery.txt'))
		if amount == '5':
			await ctx.channel.send(file = discord.File(fp = 'scripts/Work At A Pizza Place Manager.txt'))
			await ctx.channel.send(file = discord.File(fp = 'scripts/Work At A Pizza Place AutoFarm.txt'))

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
			await ctx.channel.send(file = discord.File(fp = 'scripts/Energy Assault.txt'))
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
			

		scripts = self.bot.get_channel(688458452317765645)
		
		
		embed = discord.Embed(description=f'```fix\n Обновление скрипта```\n\n **Был переделан скрипт на игру:** `{reason}`', color=0xa400fc)
		emb = discord.Embed(description=f'```yaml\n Добавление скрипта```\n\n **Был добавлен скрипт на игру:** `{reason}`', color=0xa400fc)
		embedd = discord.Embed(description=f'```fix\n Добавление скрипта к цифре```\n\n **Был добавлен скрипт к игре:** `{reason}`', color=0xa400fc)

		if amount == '1':
			await scripts.send(embed=embed)
		if amount == '2':
			await scripts.send(embed=emb)
		if amount == '3':
			await scripts.send(embed=embedd)
	
	@commands.command()
	async def update(self, ctx):
		newData = requests.get('https://pastebin.com/raw/9zCieekb') # https://pastebin.com/9zCieekb
		oldData = requests.get('https://pastebin.com/raw/kuP3Er90') # https://pastebin.com/kuP3Er90


		#embed = discord.Embed(description=f'```fix\n Обновление облокса```\n\n **Был обновлён роблокс. Новая версия:**\n ```yaml\n{newData}```\n', color=0xa400fc)
		#await ctx.send(embed=embed)
		embed1 = discord.Embed(title=f"Splash", description="SplashBot обнаружил обновление роблокса, подождите пока обновят длл", color=0xa400fc)
		embed1.add_field(name=f'Новая Версия:', value=newData, inline=True)
		embed1.add_field(name=f'Старая Версия:', value=oldData, inline=True)
		await ctx.send(embed=embed1)



	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, discord.ext.commands.errors.CommandNotFound):
			await ctx.send(embed=discord.Embed(description=f'**Команда не найдена**', color=0xa400fc))
		if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
			await ctx.send(embed=discord.Embed(description='**Не правильно введена команда.\nЧтобы узнать как вводить команду #help**', color=0xa400fc))

def setup(bot):
	bot.add_cog(scripts(bot))
	print("[SplashBot] Ког: Скрипты. Загружен")
