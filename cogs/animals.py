import discord,json,requests
from discord.ext import commands
import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()



def get_lang(guild, ru_text:str, en_text:str):
	if cursor.execute(f"SELECT lang FROM servers WHERE id = {guild.id}").fetchone()[0] == 'ru':
		return ru_text
	elif cursor.execute(f"SELECT lang FROM servers WHERE id = {guild.id}").fetchone()[0] == 'en':
		return en_text
	else:
		return en_text

class animals(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.cog_name = ["animals"]
		db = sqlite3.connect("Marry.db")
		cursor = db.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS marrys(
		id1 BIGINT
		)""")
		db.commit()
		db.close()
		cursor.execute(f"SELECT * FROM marrys WHERE id1='{ctx.message.author.id}'")
		res = cursor.fetchall()


	@commands.command(aliases=["cat", "кот"],
		description="Показать котика",
		usage="cat [Ничего]")
	async def __cat(self, ctx):
		if ctx.author.id == 465390488963514368:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))

		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		response = requests.get('https://some-random-api.ml/img/cat')
		jsoninf = json.loads(response.text)
		url = jsoninf['link']
		embed = discord.Embed(title="Вот тебе котик", color = 0xa400fc)
		embed.set_image(url = url)
		await ctx.send(embed = embed)

	@commands.command(aliases=["panda", "панда"],
		description="Показать панду",
		usage="panda [Ничего]")
	async def __panda(self, ctx):
		if ctx.author.id == 465390488963514368:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		response = requests.get('https://some-random-api.ml/img/panda')
		jsoninf = json.loads(response.text)
		url = jsoninf['link']
		embed = discord.Embed(title="Вот тебе панда", color = 0xa400fc)
		embed.set_image(url = url)
		await ctx.send(embed = embed)

	@commands.command(aliases=["fox", "лиса"],
		description="Показать лисичку",
		usage="fox [Ничего]")
	async def __fox(self, ctx):
		if ctx.author.id == 465390488963514368:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		response = requests.get('https://some-random-api.ml/img/fox')
		jsoninf = json.loads(response.text)
		url = jsoninf['link']
		embed = discord.Embed(title="Вот тебе лисичка", color = 0xa400fc)
		embed.set_image(url = url)
		await ctx.send(embed = embed)

	@commands.command(aliases=["koala", "коала"],
		description="Показать коалу",
		usage="koala [Ничего]")
	async def __koala(self, ctx):
		if ctx.author.id == 465390488963514368:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		response = requests.get('https://some-random-api.ml/img/koala')
		jsoninf = json.loads(response.text)
		url = jsoninf['link']
		embed = discord.Embed(title="Вот тебе коала", color = 0xa400fc)
		embed.set_image(url = url)
		await ctx.send(embed = embed)

	@commands.command(aliases=["собака", "dog"],
		description="Показать собачку",
		usage="dog [Ничего]")
	async def __dog(self, ctx):
		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		if ctx.author.id == 465390488963514368:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		response = requests.get('https://some-random-api.ml/img/dog')
		jsoninf = json.loads(response.text)
		url = jsoninf['link']
		embed = discord.Embed(title="Вот тебе собачка", color = 0xa400fc)
		embed.set_image(url = url)
		await ctx.send(embed = embed)			

	@commands.command(aliases=["bird", "птица"],
		description="Показать птичку",
		usage="bird [Ничего]")
	async def __bird(self, ctx):
		if ctx.author.id == 465390488963514368:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		response = requests.get('https://some-random-api.ml/img/birb')
		jsoninf = json.loads(response.text)
		url = jsoninf['link']
		embed = discord.Embed(title="Вот тебе птичка", color = 0xa400fc)
		embed.set_image(url = url)
		await ctx.send(embed = embed)

	@commands.command(aliases=["red-panda", "redpanda"],
		description="Показать красную панду",
		usage="red-panda [Ничего]")
	async def __redpanda(self, ctx):
		if ctx.author.id == 465390488963514368:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		if ctx.author.id == 719605055547768894:
			return await ctx.send(embed = discord.Embed(description = f'**Ты не можешь использовать эту команду**', color=0xa400fc))
		response = requests.get('https://some-random-api.ml/img/red_panda')
		jsoninf = json.loads(response.text)
		url = jsoninf['link']    
		embed = discord.Embed(title="Вот тебе красная панда", color = 0xa400fc)
		embed.set_image(url = url)
		await ctx.send(embed = embed)




def setup(bot):
	bot.add_cog(animals(bot))
	print("[SplashBot] Ког: Животные. Загружен")
