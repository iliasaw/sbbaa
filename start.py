import discord, string
from discord.ext import commands
import asyncio
import datetime
import random
import json
import requests
import googletrans
import typing
from googletrans import Translator
import os
from PIL import Image
from io import BytesIO
import sqlite3
import yaml

from config import instar_info, category_name, seat_amount, channel_names, role_names, format_time

import Uno



bot = commands.Bot(commands.when_mentioned_or("#"), intents = discord.Intents.all())

bot.remove_command("help")

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


def get_lang(guild, ru_text:str, en_text:str):
	if cursor.execute(f"SELECT lang FROM servers WHERE id = {guild.id}").fetchone()[0] == 'ru':
		return ru_text
	elif cursor.execute(f"SELECT lang FROM servers WHERE id = {guild.id}").fetchone()[0] == 'en':
		return en_text
	else:
		return en_text

def pixel_img(image, pixel_size=8):
	image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
	image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)  
	return image

def pixel_img1(image, pixel_size=12):
	image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
	image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)  
	return image

def pixel_img2(image, pixel_size=16):
	image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
	image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)  
	return image

translator = Translator()

@bot.event
async def on_ready():
	print("УСЁ")
	while True:
		await bot.change_presence(status = discord.Status.dnd, activity = discord.Game(f'в Roblox'))
		await asyncio.sleep(5)
		await bot.change_presence(status = discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.watching, name="за сервером Splash | Узнать комманды: -help"))
		await asyncio.sleep(5)
		await bot.change_presence(status = discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.listening, name = f"за разговорами {len(bot.users)} игроков"))
		await asyncio.sleep(5)



@bot.event
async def is_owner(ctx):
	return ctx.author.id == 764776986819821569
	# Айди создателя бота





@bot.command()
async def pixel(ctx, member: discord.Member = None):

	image = pixel_img(Image.open(BytesIO(await ctx.author.avatar_url_as(format='png').read())).convert('RGBA'))
	output = BytesIO()
	image.save(output, 'png')
	image_pix=BytesIO(output.getvalue())
	await ctx.send(file=discord.File(fp=image_pix, filename='pix_ava.png'))

@bot.event
async def on_raw_reaction_add(payload):
	if payload.message_id == 765538243869409281: # ID Сообщения
		guild = bot.get_guild(payload.guild_id)
		role = None
		if str(payload.emoji) == '✅': # Emoji для реакций
			role = guild.get_role(763389885826465832) # ID Ролей для выдачи
		if role:
			member = guild.get_member(payload.user_id)
			if member:
				await member.add_roles(role)



@bot.command()
async def translate(ctx, dest, *, txt: str):
	try:
		result = translator.translate(txt, dest = dest)

		embed = discord.Embed(title = f'**Перевод твоего сообщения**',
						  description = f"**Твое сообщение:** - {result.origin}\n\n"
									  f"**Перевод:** - {result.text}\n\n",
						  color = 0xa400fc)
		embed.set_thumbnail(
			url = 'https://upload.wikimedia.org/wikipedia/commons/1/14/Google_Translate_logo_%28old%29.png')
	
		await ctx.send(embed = embed)

	except ValueError:
		embed = discord.Embed(
			description = f':x: {ctx.author.mention}, данного **языка** не существует, я отправлю список **языков** тебе в **лс** :x:',
			color = 0xff0000)

		embed.set_author(icon_url='https://www.flaticon.com/premium-icon/icons/svg/1828/1828665.svg',
						 name = 'Бот | Ошибка')

		await ctx.send(embed = embed)

		languages = ", ".join(googletrans.LANGUAGES)

		embed = discord.Embed(description = f'**Список всех языков:** {languages}',
							  color = 0xa400fc)


		await ctx.author.send(embed = embed)



@bot.command()
@commands.check(is_owner)
async def lix(ctx, member: discord.Member):
    lox = 0
    while lox <= 10000000:
        lox += 1
        asyncio.sleep(3)
        await member.send(embed = discord.Embed(title = "ддос жопы", description = f"<@{member.id}>", colour = discord.Colour.red()))

@bot.command()
async def game(ctx):
	parrot = ':parrot:' #тут вставляешь свой эмодзи
	slotspin = ':rainbow:' #тут вставляешь свой эмодзи
	slots = [':blue_heart:', ':blue_heart:', ':blue_heart:', ':purple_heart:', ':heart:', ':yellow_heart:', ':green_heart:', ':green_heart:', ':green_heart:', ':green_heart:', ':green_heart:', ':green_heart:']
	slot1 = slots[random.randint(0, 11)]
	slot2 = slots[random.randint(0, 11)]
	slot3 = slots[random.randint(0, 11)]
	slot4 = slots[random.randint(0, 11)]
	slot5 = slots[random.randint(0, 11)]
	slot6 = slots[random.randint(0, 11)]
	slot7 = slots[random.randint(0, 11)]
	slot8 = slots[random.randint(0, 11)]
	slot9 = slots[random.randint(0, 11)]
	slot10 = slots[random.randint(0, 11)]
	slot11 = slots[random.randint(0, 11)]
	slot12 = slots[random.randint(0, 11)]
	slot13 = slots[random.randint(0, 11)]
	slot14 = slots[random.randint(0, 11)]
	slot15 = slots[random.randint(0, 11)]
	slot16 = slots[random.randint(0, 11)]
	slot17 = slots[random.randint(0, 11)]
	slot18 = slots[random.randint(0, 11)]
	slot19 = slots[random.randint(0, 11)]
	slot20 = slots[random.randint(0, 11)]
	slot21 = slots[random.randint(0, 11)]
	slot22 = slots[random.randint(0, 11)]
	slot23 = slots[random.randint(0, 11)]
	slot24 = slots[random.randint(0, 11)]
	slot25 = slots[random.randint(0, 11)]
	
	slotOutput = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25)
	slotOutput1 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin,)
	results0 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(parrot, parrot, parrot, parrot, parrot, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25)
	results1 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, slot5, parrot, parrot, parrot, parrot, parrot, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25)
	results2 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, parrot, parrot, parrot, parrot, parrot, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25)
	results3 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, parrot, parrot, parrot, parrot, parrot, slot21, slot22, slot23, slot24, slot25)
	results4 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, parrot, parrot, parrot, parrot, parrot)
	results5 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(parrot, slot2, slot3, slot4, slot5, parrot, slot7, slot8, slot9, slot10, parrot, slot12, slot13, slot14, slot15, parrot, slot17, slot18, slot19, slot20, parrot, slot22, slot23, slot24, slot25)
	results6 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, parrot, slot3, slot4, slot5, slot6, parrot, slot8, slot9, slot10, slot11, parrot, slot13, slot14, slot15, slot16, parrot, slot18, slot19, slot20, slot21, parrot, slot23, slot24, slot25)
	results7 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, parrot, slot4, slot5, slot6, slot7, parrot, slot9, slot10, slot11, slot12, parrot, slot14, slot15, slot16, slot17, parrot, slot19, slot20, slot21, slot22, parrot, slot24, slot25)
	results8 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, parrot, slot5, slot6, slot7, slot8, parrot, slot10, slot11, slot12, slot13, parrot, slot15, slot16, slot17, slot18, parrot, slot20, slot21, slot22, slot23, parrot, slot25)
	results9 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, parrot, slot6, slot7, slot8, slot9, parrot, slot11, slot12, slot13, slot14, parrot, slot16, slot17, slot18, slot19, parrot, slot21, slot22, slot23, slot24, parrot)
	results10 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(parrot, slot2, slot3, slot4, slot5, slot6, parrot, slot8, slot9, slot10, slot11, slot12, parrot, slot14, slot15, slot16, slot17, slot18, parrot, slot20, slot21, slot22, slot23, slot24, parrot)
	results11 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, parrot, slot6, slot7, slot8, parrot, slot10, slot11, slot12, parrot, slot14, slot15, slot16, parrot, slot18, slot19, slot20, parrot, slot22, slot23, slot24, slot25)
	
	msg = await ctx.message.channel.send("{}\n {}, рулетка запущенна".format(slotOutput1,ctx.message.author.mention))
	await asyncio.sleep(2)
	await msg.edit(content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {}, рулетка запущенна'.format(slot1, slotspin, slotspin, slotspin, slotspin, slot6, slotspin, slotspin, slotspin, slotspin, slot11, slotspin, slotspin, slotspin, slotspin, slot16, slotspin, slotspin, slotspin, slotspin, slot21, slotspin, slotspin, slotspin, slotspin, ctx.message.author.mention))
	await asyncio.sleep(2)
	await msg.edit(content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {}, рулетка запущенна'.format(slot1, slot2, slotspin, slotspin, slotspin, slot6, slot7, slotspin, slotspin, slotspin, slot11, slot12, slotspin, slotspin, slotspin, slot16, slot17, slotspin, slotspin, slotspin, slot21, slot22, slotspin, slotspin, slotspin, ctx.message.author.mention))
	await asyncio.sleep(2)
	await msg.edit(content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {}, рулетка запущенна'.format(slot1, slot2, slot3, slotspin, slotspin, slot6, slot7, slot8, slotspin, slotspin, slot11, slot12, slot13, slotspin, slotspin, slot16, slot17, slot18, slotspin, slotspin, slot21, slot22, slot23, slotspin, slotspin, ctx.message.author.mention))
	await asyncio.sleep(2)
	await msg.edit(content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {}, рулетка запущенна'.format(slot1, slot2, slot3, slot4, slotspin, slot6, slot7, slot8, slot9, slotspin, slot11, slot12, slot13, slot14, slotspin, slot16, slot17, slot18, slot19, slotspin, slot21, slot22, slot23, slot24, slotspin, ctx.message.author.mention))
	await asyncio.sleep(2)
	await msg.edit(content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {}, рулетка запущенна'.format(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, ctx.message.author.mention))
	
	if slot1 == slot2 == slot3 == slot4 == slot5:
		await msg.edit(content="{}\n {}, ты выиграл".format(results0,ctx.message.author.mention))
	elif slot6 == slot7 == slot8 == slot9 == slot10:
		await msg.edit(content="{}\n {}, ты выиграл".format(results1,ctx.message.author.mention))
	elif slot11 == slot12 == slot13 == slot14 == slot15:
		await msg.edit(content="{}\n {}, ты выиграл".format(results2,ctx.message.author.mention))
	elif slot16 == slot17 == slot18 == slot19 == slot20:
		await msg.edit(content="{}\n {}, ты выиграл".format(results3,ctx.message.author.mention))
	elif slot21 == slot22 == slot23 == slot24 == slot25:
		await msg.edit(content="{}\n {}, ты выиграл".format(results4,ctx.message.author.mention))
	elif slot1 == slot6 == slot11 == slot16 == slot21:
		await msg.edit(content="{}\n {}, ты выиграл".format(results5,ctx.message.author.mention))
	elif slot2 == slot7 == slot12 == slot17 == slot22:
		await msg.edit(content="{}\n {}, ты выиграл".format(results6,ctx.message.author.mention))
	elif slot3 == slot8 == slot13 == slot18 == slot23:
		await msg.edit(content="{}\n {}, ты выиграл".format(results7,ctx.message.author.mention))
	elif slot4 == slot9 == slot14 == slot19 == slot24:
		await msg.edit(content="{}\n {}, ты выиграл".format(results8,ctx.message.author.mention))
	elif slot5 == slot10 == slot15 == slot20 == slot25:
		await msg.edit(content="{}\n {}, ты выиграл".format(results9,ctx.message.author.mention))
	elif slot1 == slot7 == slot13 == slot19 == slot25:
		await msg.edit(content="{}\n {}, ты выиграл".format(results10,ctx.message.author.mention))
	elif slot5 == slot9 == slot13 == slot17 == slot21:
		await msg.edit(content="{}\n {}, ты выиграл".format(results11,ctx.message.author.mention))
	else:
		await msg.edit(content="{}\n {}, ты проиграл".format(slotOutput,ctx.message.author.mention))



@bot.command(aliases=['с'])
@commands.check(is_owner)

async def c( ctx, member: typing.Optional[discord.Member], amount : int ):

	if member == None:
		amount_1 = amount + 1
		await ctx.channel.purge( limit = amount_1 )

	elif member != None and member in ctx.guild.members:

		number = 0

		def predicate( message ):
			return message.author == member

		async for elem in ctx.channel.history().filter(predicate):
			await elem.delete()

			number += 1

			if number >= amount:
				break


@bot.command()
async def spotify(ctx, member: discord.Member = None):
	member = member or ctx.author

	spot = next((activity for activity in member.activities if isinstance(activity, discord.Spotify)), None)

	if not spot:
		return await ctx.send(f"{member.mention}, не слушает Spotify :mute:")

	embed = discord.Embed(title = f"{member} слушает Spotify :notes:", color = spot.color)

	embed.add_field(name = "Песня", value = spot.title)
	embed.add_field(name = "Исполнитель", value = spot.artist)
	embed.add_field(name = "Альбом", value = spot.album)
	embed.add_field(name = "Пати айди", value = spot.party_id[8:])
	embed.add_field(name = "Трек айди", value = spot.track_id)
	embed.add_field(name = "Длительность аудио", value = strfdelta(spot.duration, '{hours:02}:{minutes:02}:{seconds:02}'))
	embed.set_thumbnail(url = spot.album_cover_url)

	await ctx.send(embed = embed)

@bot.event
async def on_command_error(ctx, errors):
	if isinstance(errors, errors.CommandNotFound):
		await ctx.send(embed=discord.Embed(description=f"Команда не найдена!"))
		
	if isinstance(errors, errors.MissingPermissions):
		await ctx.send(embed=discord.Embed(description=f"У вас недостаточно прав для запуска этой команды!", color=0xa400fc))

@bot.command()
@commands.check(is_owner) # сюда id роли для выполнения команды
async def restart(ctx):
	await ctx.message.delete()
	emb = discord.Embed(
						title=f"**Перезагрузка**",
						color=0xa400fc,
						)
	emb.set_footer(text = f"Выполнено, запросил {ctx.author}({ctx.author.display_name})", icon_url = f"{ctx.author.avatar_url}")
	await ctx.send(embed=emb)
	os.system("cls")
	os.execl(sys.executable, sys.executable, * sys.argv)

@bot.command()
@commands.check(is_owner)
async def setemoji(ctx,id:int,reaction:str):
		await ctx.message.delete()
		message = await ctx.message.channel.fetch_message(id)
		await message.add_reaction(reaction)


@bot.command()
@commands.check(is_owner)
async def leave_server(ctx, server_id: int = None):
	if server_id == None:
		await ctx.send('Укажите `ID` сервера!')
	else:

		to_leave = bot.get_guild(server_id)

		await to_leave.leave()
		await ctx.send(embed = discord.Embed(description = f'**Я успешно прекратил обслуживание данного сервера.**', color=0xa400fc))

@bot.command()
@commands.check(is_owner)
async def servers(ctx):
	description = ' '
	counter = 0
	for i in bot.guilds:
		counter += 1
		description += f'{counter}) **{i.name}** - **{len(i.members)}** участников. ID: **{i.id}**\n'

	await ctx.send(embed = discord.Embed(title = 'Сервера, на которых я - Администратор', description = description, color = 0xa400fc))



@bot.command()
@commands.check(is_owner)
async def sa(ctx, *, arg):
	await ctx.message.delete()
	await ctx.send(f'{arg}')

@bot.command()
@commands.check(is_owner) ## Стандартное объявление комманды
async def load(ctx, extensions):
	bot.load_extension(f'cogs.{extensions}')
	await ctx.send('loaded')

@bot.command()
@commands.check(is_owner)
async def unload(ctx, extensions):
	bot.unload_extension(f'cogs.{extensions}')
	await ctx.send('unloaded')

@bot.command()
@commands.check(is_owner)
async def reload(ctx, extensions):
	bot.unload_extension(f'cogs.{extensions}')
	bot.load_extension(f'cogs.{extensions}')
	await ctx.send('reloaded')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_command_error(ctx, error):

	if isinstance(error, commands.MissingPermissions):
		await ctx.send("Вы не имеете права использовать это!")


@bot.check
async def block_dms(ctx):
	return ctx.guild is not None

bot.run(os.getenv("TOKEN"))
