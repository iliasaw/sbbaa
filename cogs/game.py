import discord
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
import sqlite3
from random import choice
import datetime
import time

from config import instar_info, category_name, seat_amount, channel_names, role_names, format_time

import Uno

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


def get_lang(guild, ru_text:str, en_text:str):
    if cursor.execute(f"SELECT lang FROM servers WHERE id = {guild.id}").fetchone()[0] == 'ru':
        return ru_text
    elif cursor.execute(f"SELECT lang FROM servers WHERE id = {guild.id}").fetchone()[0] == 'en':
        return en_text
    else:
        return en_text

class OccupiedUNOSeats(commands.CheckFailure):
	pass

def check_seats():
	async def predictate(ctx):
		category = discord.utils.get(ctx.guild.categories, name=category_name)

		if category:
			for channel in category.text_channels:
				msg = await channel.history().flatten()

				if len(msg) > 0:
					raise OccupiedUNOSeats("Там уже есть игра на прогресс прямо сейчас! Подождите, пока это не закончится")
		return True
	return commands.check(predictate)

class GameCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.cog_name = ["Uno"]

	

	@commands.command(aliases=["старт"],
		description="Начать игру в уно",
		usage="start [Ничего]")
	@check_seats()
	async def start(self, ctx):
		user_lst = [ctx.author]
		join_msg = "join"

		# Join Stage

		await ctx.send(f"**{ctx.author}** уже началась игра в Уно, но им нужно как минимум два игрока.\n"
						f"Если вы хотите присоединиться к этой игре, напишите `{join_msg}`.")

		for _ in range(1, seat_amount):
			def join_check(m):
				return m.content.lower() == join_msg and m.channel == ctx.channel and m.author not in user_lst

			try:
				r = await self.bot.wait_for("message", check=join_check, timeout=60.0)
			except asyncio.TimeoutError:
				break
			else:
				user_lst.append(r.author)
				await ctx.send(f"**{r.author}** присоединился к игре!")

		if len(user_lst) < 2:
			await ctx.send("Похоже, что больше никто не хочет играть прямо сейчас!")
			return

		# Preparation Stage

		wait_msg = await ctx.send("Подождите, пока я подготовлю игру...")

		emoji_dict = {}
		gui_lst = []
		roles_lst = []

		async with ctx.channel.typing():
			for key, name in Uno.emojis.items():
				emoji = discord.utils.get(ctx.guild.emojis, name=name)
				if emoji:
					emoji_dict[key] = str(emoji)

			channels_lst = discord.utils.get(ctx.guild.categories, name=category_name).text_channels

			for i in range(0, len(user_lst)):
				await channels_lst[i].send( Uno.game_help(emoji_dict) )
				gui_lst.append( await channels_lst[i].send("[Placeholder]") )

				roles_lst.append(discord.utils.get(ctx.guild.roles, name=role_names[i]))

			UnoGame = Uno.Game(user_lst, channels_lst, gui_lst, roles_lst, emoji_dict)

			await Uno.update_gui(self.bot, UnoGame)

			for user, role in UnoGame.player_roles():
				await user.add_roles(role, reason="Чтобы дать доступ к их месту в UNO.")
			
		cancel_game = False

		await wait_msg.edit(content="Игра готова к началу!")
		game_start_time = datetime.datetime.now()

		async def send_notification(msg, game_obj):
			for player in game_obj.players:
				if not player == game_obj.actual_player:
					await player.channel.send(msg, delete_after=5.0)

		# Game Phase

		while True:
			player = UnoGame.actual_player
			top_card = UnoGame.table.top_played_card
			
			def response_check(m):
				return m.channel == player.channel and m.author == player.user

			if not top_card.do_skip:
				await player.channel.send(f"Теперь твоя очередь, **{player.user}**!", delete_after=10.0)

				while True:
					try:
						r = await self.bot.wait_for("message", check=response_check, timeout=120.0)
						response = r.content.lower()
						await r.delete(delay=2.0)

					except asyncio.TimeoutError:
						cancel_game = True
						break

					else:
						if response == Uno.uno_call_cmd and player.called_uno == False:
							if player.call_uno():
								await player.channel.send("Ты вызвал Уно!", delete_after=5.0)
								await send_notification(f"**{player.user}** Вызвал Уно!", UnoGame)
							else:
								await player.channel.send("Ты не можешь вызвать Уно прямо сейчас!", delete_after=5.0)

						elif player.play(response):
							break

						else:
							await player.channel.send("Недействительное действий!", delete_after=5.0)
			else:
				await player.channel.send("Ты потерял свою очередь!", delete_after=5.0)

				if top_card.is_draw_two:
					player.draw_card(2)

				if top_card.is_draw_four:
					player.draw_card(4)

			if UnoGame.table.top_played_card.is_wild:
				wild_instruction = await player.channel.send( Uno.wild_help(emoji_dict) )

				while True:
					try:
						c = await self.bot.wait_for("message", check=response_check, timeout=60.0)
						color = c.content.lower()
						await c.delete(delay=2.0)

					except asyncio.TimeoutError:
						cancel_game = True
						break

					else:
						if UnoGame.table.top_played_card.change_color(color):
							break
						else:
							await player.channel.send("Это не допустимый цвет!", delete_after=5.0)

				await wild_instruction.delete(delay=1.0)

			if UnoGame.table.top_played_card.do_reverse:
				UnoGame.reverse()

				await player.channel.send("Вы поменяли местами ходы!", delete_after=5.0)
				await send_notification(f"**{player.user}** поменял местами ходы!", UnoGame)

			if player.do_penalize():
				await player.channel.send("Вы были наказаны за отсутствие вызова UNO!", delete_after=5.0)
				await send_notification(f"**{player.user}** был наказан за отсутствие вызова UNO!", UnoGame)

			if cancel_game:
				await send_notification(f"Похоже на то **{player.user}** отказался.\nИгра была отменена!", UnoGame)

				await ctx.send("Игра была отменена!")
				break
			
			if player.hand_size == 0:
				await player.channel.send("У тебя не осталось ни одной карты! **Вы выиграли эту игру в UNO!**!", delete_after=5.0)
				await send_notification(f"**{player.user}** у него не осталось ни одной карты! **Он выиграли эту игру в UNO!**", UnoGame)

				game_time = datetime.datetime.now() - game_start_time
				await ctx.send(f"**{player.user}** победил в игре UNO!\nИгровое время: **{format_time(game_time.total_seconds())}**")
				break

			top_card.deactivate()

			UnoGame.next_turn()
			await Uno.update_gui(self.bot, UnoGame)

	@start.before_invoke
	async def prepare_server(self, ctx):
		if category_name in [c.name for c in ctx.guild.categories]:
				return

		async with ctx.channel.typing():
			for name in Uno.emojis.values():
				try:
					with open(f"./{name}.png", "rb") as image:
						await ctx.guild.create_custom_emoji(name=name, image=image.read())
				except FileNotFoundError:
					pass
			
			game_roles = []

			for role in role_names:
				game_roles.append( await ctx.guild.create_role(name=role) )

			perms = {
				ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
				ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
			}
			
			game_category = await ctx.guild.create_category_channel(category_name, overwrites=perms, reason="Для игры в UNO.")

			for i in range(0, seat_amount):
				channel_perms = {
					ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
					ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
					game_roles[i]: discord.PermissionOverwrite(read_messages=True)
				}

				await game_category.create_text_channel(channel_names[i], overwrites=channel_perms)

	@start.after_invoke
	async def clean_up(self, ctx):
		await asyncio.sleep(5)
		
		for channel in discord.utils.get(ctx.guild.categories, name=category_name).text_channels:
			for user in channel.members:
				for role in user.roles:
					if role.name in role_names:
						await user.remove_roles(role, reason="Уборка")

			await channel.purge()

	

	@commands.command(aliases=["reset", "рестарт"],
		description="Удалить всё что связано с уно",
		usage="reset [Ничего]")
	async def __reset(self, ctx):
		async with ctx.channel.typing():
			for name in Uno.emojis.values():
				emoji = discord.utils.get(ctx.guild.emojis, name=name)
				if emoji:
					await emoji.delete(reason="Ресэт")
			
			guild_roles = ctx.guild.roles

			for role in role_names:
				for i in range(0, len(guild_roles)):
					if role == guild_roles[i].name:
						await guild_roles[i].delete(reason="Ресэт")
						break

			guild_channels = ctx.guild.text_channels

			for channel in channel_names:
				for i in range(0, len(guild_channels)):
					if channel == guild_channels[i].name:
						await guild_channels[i].delete(reason="Ресэт")
						break

			guild_categories = ctx.guild.categories

			for i in range(0, len(guild_categories)):
				if category_name == guild_categories[i].name:
					await guild_categories[i].delete(reason="Ресэт")
					break

		await ctx.send("Все, что связано с Уно, было удалено!")

	@commands.command(aliases=["info", "инфо"],
		description="Показать информацию о игре в уно",
		usage="info [Ничего]")
	async def __info(self, ctx):
		await ctx.send(instar_info)

def setup(bot):
	bot.add_cog(GameCog(bot))
	print("[SplashBot] Ког: Уно. Загружен")
