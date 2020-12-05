# Импорт
import discord
import time
from discord.ext import commands

res  = 407865383157235722

# Код
class Moder(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None
		self.cog_name = ["Модераторские"]

	@commands.command()
	@commands.has_any_role(764776537588760623, 764776537588760624, 764776537588760625, 764776537600950282, 764776537600950283, 764776537600950284, 764776537600950286, 772079106410020875)
	async def mute(ctx, member: discord.Member, arg: str, *, reason = None):
		if ctx.author.id == res:
			return await ctx.send(f"{ctx.author.mention} Вы в чёрном списке")
		await ctx.message.delete()
		now_date = datetime.datetime.now()
		mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Muted')
		if not mute_role:
			mute_role = await ctx.guild.create_role(name = 'Muted', permissions = discord.Permissions(send_messages = False), color = 0xa400fc)
			for i in ctx.guild.channels:
				await i.set_permissions(mute_role, send_messages = False)
			mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Muted')
		if mute_role in member.roles:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Данный пользователь, {member.mention}, уже замьючен!**', color=0xa400fc))
		if not member and not arg:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Правильное использование команды: `#mute @user 10m причина`', color=0xa400fc))
		if member.id == ctx.guild.owner.id:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Данный пользователь, {member.mention}, является создателем этого сервера!**', color=0xa400fc))
		if member.id == ctx.guild.me.id:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Я не могу замутить самого себя!**', color=0xa400fc))
		if ctx.author.top_role.position < member.top_role.position:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Ты не можешь замутить человека с позицией выше твоей!**', color=0xa400fc))
		if member.id == ctx.author.id:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Напомню, суицид - это не выход!**', color=0xa400fc))
		if member.top_role > ctx.guild.me.top_role:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Я не могу замутить {member.mention}, так как его роль выше моей!**', color=0xa400fc))
		if mute_role.position > ctx.guild.me.top_role.position:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Я не могу замутить {member.mention}, так как роль мута выше моей!**', color=0xa400fc))
		emb = discord.Embed(title = 'Мут', colour = 0xa400fc)
		emb.set_author(name = member.name, icon_url = member.avatar_url)
		emb.add_field(name = '**Выдал:**', value = '{}'.format(ctx.author.display_name), inline = False)
		emb.add_field(name = '**Тип наказания:**', value = 'Тектовый мут', inline = False)
		emb.add_field(name = '**Время выдачи:**', value = '{}'.format(now_date), inline = False)
		amount = int(arg[:-1])
		tip = arg[-1]
		if tip == "s":  
			if reason is None:
				emb.add_field(name = '**Причина:**', value = 'Не указана.', inline = False)
				await member.add_roles(mute_role, reason = "Не указана", atomic = True)
				await ctx.send(f'```SplashBot » Пользователь "{member.display_name}" был заглушен на {amount} секунд.\nПричина: Не указана.```')
			else:
				emb.add_field(name = '**Причина:**', value = '{}'.format(reason), inline = False)
				await member.add_roles(mute_role, reason = reason, atomic = True)
				await ctx.send(f'```SplashBot » Пользователь "{member.display_name}" был заглушен на {amount} секунд.\nПричина: {reason}```')
			await member.send(embed = emb) 
			await asyncio.sleep(amount)       
		elif tip == "m":
			if reason is None:
				emb.add_field(name = '**Причина:**', value = 'Не указана.', inline = False)
				await member.add_roles(mute_role, reason = "Не указана", atomic = True)
				await ctx.send(f'```SplashBot » Пользователь "{member.display_name}" был заглушен на {amount} минут.\nПричина: Не указана.```')
			else:
				emb.add_field(name = '**Причина:**', value = '{}'.format(reason), inline = False)
				await member.add_roles(mute_role, reason = reason, atomic = True)
				await ctx.send(f'```SplashBot » Пользователь "{member.display_name}" был заглушен на {amount} минут.\nПричина: {reason}```')
			await member.send(embed = emb)
			await asyncio.sleep(amount * 60)
		elif tip == "h":
			if reason is None:
				emb.add_field(name = '**Причина:**', value = 'Не указана.', inline = False)
				await member.add_roles(mute_role, reason = "Не указана", atomic = True)
				await ctx.send(f'```SplashBot » Пользователь "{member.display_name}" был заглушен на {amount} часов.\nПричина: Не указана.```')
			else:
				emb.add_field(name = '**Причина:**', value = '{}'.format(reason), inline = False)
				await member.add_roles(mute_role, reason = reason, atomic = True)
				await ctx.send(f'```SplashBot » Пользователь "{member.display_name}" был заглушен на {amount} часов.\nПричина: {reason}```')
			await member.send(embed = emb)
			await asyncio.sleep(amount * 60 * 60)
		elif tip == "d":
			if reason is None:
				emb.add_field(name = '**Причина:**', value = 'Не указана.', inline = False)
				await member.add_roles(mute_role, reason = "Не указана", atomic = True)
				await ctx.send(f'```SplashBot » Пользователь "{member.display_name}" был заглушен на {amount} дней.\nПричина: Не указана.```')
			else:
				emb.add_field(name = '**Причина:**', value = '{}'.format(reason), inline = False)
				await member.add_roles(mute_role, reason = reason, atomic = True)
				await ctx.send(f'```SplashBot » Пользователь "{member.display_name}" был заглушен на {amount} дней.\nПричина: {reason}```')
			await member.send(embed = emb)
			await asyncio.sleep(amount * 60 * 60 * 24)
		await member.remove_roles(mute_role)
	
	@commands.command(pass_context = True)
	@commands.has_any_role(764776537588760623, 764776537588760624, 764776537588760625, 764776537600950282, 764776537600950283, 764776537600950284, 764776537600950286, 772079106410020875)
	async def unmute(ctx, member: discord.Member, *, reason = None):
		if ctx.author.id == res:
			return await ctx.send(f"{ctx.author.mention} Вы в чёрном списке")
		mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Muted')
		if not member and not arg:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Правильное использование команды: `unmute @пользователь причина`', color=0xa400fc))
		if mute_role.position > ctx.guild.me.top_role.position:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Я не могу размутить {member.mention}, так как роль мута выше моей!**', color=0xa400fc))
		now_date = datetime.datetime.now()
		emb = discord.Embed(title = 'Размут', colour = 0xa400fc)
		await ctx.message.delete()
		if mute_role in member.roles:
			await member.remove_roles(mute_role)
			emb.set_author(name = member.name, icon_url = member.avatar_url)
			emb.add_field(name = '**Выдал:**', value = '{}'.format(ctx.author.display_name), inline = False)
			emb.add_field(name = '**Тип наказания:**', value = 'text_unmute', inline = False)
			emb.add_field(name = '**Время выдачи:**', value = '{}'.format(now_date), inline = False)
			emb.add_field(name = '**Причина:**', value = '{}'.format(reason), inline = False)
			emb.set_footer(text = 'Не отвечайте на это сообщение.', icon_url = ctx.author.avatar_url)
			await channel_log.send(embed = emb)
			await member.send(embed = emb)
			await ctx.send(f'```SplashBot » Пользователь "{member.display_name}" был размучен.\nПричина: {reason}```')
		else:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Данный пользователь, {member.mention}, не замучен!**', color=0xa400fc))
	
	@commands.command()
	@commands.has_any_role(764776537588760624, 764776537588760625, 764776537600950282, 764776537600950283, 764776537600950284, 764776537600950286, 772079106410020875)
	async def kick(ctx, member: discord.Member, *, reason = None):
		if ctx.author.id == res:
			return await ctx.send(f"{ctx.author.mention} Вы в чёрном списке")
		await ctx.message.delete()
		if not member:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Правильное использование команды: `#kick @user причина`', color=0xa400fc))
		if member.id == ctx.guild.owner.id:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Данный пользователь, {member.mention}, является создателем этого сервера!**', color=0xa400fc))
		if member.id == ctx.guild.me.id:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Я не могу кикнуть самого себя!**', color=0xa400fc))
		if ctx.author.top_role.position < member.top_role.position:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Ты не можешь кикнуть человека с позицией выше твоей!**', color=0xa400fc))
		if member.id == ctx.author.id:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Напомню, суицид - это не выход!**', color=0xa400fc))
		if member.top_role > ctx.guild.me.top_role:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Я не могу кикнуть {member.mention}, так как его роль выше моей!**', color=0xa400fc))
		emb = discord.Embed(title = 'Кик', colour = 0xa400fc)
		now_date = datetime.datetime.now()
		emb.set_author(name = member.name, icon_url = member.avatar_url)
		emb.add_field(name = '**Выдал:**', value = '{}'.format(ctx.author.display_name), inline = False)
		emb.add_field(name = '**Тип наказания:**', value = 'Кик', inline = False)
		emb.add_field(name = '**Время выдачи:**', value = '{}'.format(now_date), inline = False)
		if reason is None:
			emb.add_field(name = '**Причина:**', value = 'Не указана.', inline = False)
			await member.send(embed = emb)
			await ctx.send(f'```SplashBot » Пользователь "{member.display_name}" был кикнут.\nПричина: Не указана.```')
			enter_reason = ctx.author.display_name + " - Не указана."
			await member.kick(reason = enter_reason)
		else:
			emb.add_field(name = '**Причина:**', value = '{}'.format(reason), inline = False)
			await member.send(embed = emb)
			await ctx.send(f'```SplashBot » Пользователь "{member.display_name}" был кикнут.\nПричина: {reason}```')
			enter_reason = ctx.author.display_name + " - " + reason
			await member.kick(reason = enter_reason)


def setup(client):
	client.add_cog(Moder(client))
	print("[SplashBot] Ког: Модерация. Загружен")
