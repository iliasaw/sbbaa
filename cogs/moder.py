# Импорт
import discord
import time
from Utils import DB
from discord.ext import commands


# Код
class Moder(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None
		self.cog_name = ["Модераторские"]

	@commands.command(
		aliases=["мьют", "мут", "Мут", "Мьют", "Mute"],
		description="Дать мьют пользователю",
		usage="мьют <юзер> <время> <тип времени> <причина>")
	@commands.has_permissions(manage_messages=True)
	async def mute(self, ctx, member: discord.Member, timenumber: int, typetime, *, reason):

		timed = 0

		if typetime == "s" or typetime == "сек" or typetime == "секунд":
			timed = timenumber
		elif typetime == "m" or typetime == "мин" or typetime == "минут":
			timed = timenumber * 60
		elif typetime == "h" or typetime == "час" or typetime == "часов":
			timed = timenumber * 60 * 60
		elif typetime == "d" or typetime == "день" or typetime == "дней":
			timed = timenumber * 60 * 60 * 24

		times = time.time()
		times += timed

		mute_role = discord.utils.get(ctx.message.guild.roles, name="SB-Muted")

		if not mute_role:
			mute_role = await ctx.guild.create_role(name="SB-Muted")

		if mute_role in member.roles:
			await ctx.send(
				embed=discord.Embed(description=f'**:warning: Пользователь {member.mention} уже замьючен!**',
									color=0xa400fc))
		else:
			DB.Set().mute(member, times)

			await member.add_roles(mute_role,
								   reason=f"Пользователь {ctx.author.display_name} выдал мьют на {timenumber} {typetime} по причине {reason}",
								   atomic=True)
			await ctx.send(
				embed=discord.Embed(
					description=f'**:shield: Мьют пользователю {member.mention} успешно выдан по причине {reason}!**',
					color=0xa400fc))

	@mute.error
	async def mute_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(embed=discord.Embed(
				description=f'**:grey_exclamation: {ctx.author.name}, обязательно укажите юзера и время!**\n!!мьют <юзер> <время> <тип времени>',
				color=0xa400fc))

	# Размьют
	@commands.command(
		aliases=["размьют", "размут", "Размут", "Разьют", "Unmute"],
		description="снять мьют у пользователя",
		usage="размьют <юзер>")
	@commands.has_permissions(manage_messages=True)
	async def unmute(self, ctx, member: discord.Member):

		mutes = DB.Get().mute(member)
		mute = mutes[1]

		mute_role = discord.utils.get(ctx.message.guild.roles, name="Mute")

		if mute != 0:
			DB.Set().mute(member, 0)

			await member.remove_roles(mute_role)
			await ctx.send(embed=discord.Embed(
				description=f'**:white_check_mark: Мьют у пользователя {member.mention} Успешно снят! **',
				color=0xa400fc))
		else:
			await ctx.send(
				embed=discord.Embed(description=f'**:warning: Пользователь {member.mention} Не замьючен!**',
									color=0xa400fc))

	@unmute.error
	async def unmute_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(embed=discord.Embed(
				description=f'**:grey_exclamation: {ctx.author.name}, обязательно укажите юзера!**\n+размьют <юзер>',
				color=0x0c0c0c))

	@commands.command(
		aliases=["пред", "Пред", "Варн", "варн", "Warn"],
		description="Выдать предупреждение юзеру",
		usage="пред <юзер> <причина>")
	@commands.has_permissions(kick_members=True)
	async def warn(self, ctx, member: discord.Member, *, arg):

		ids = DB.Set().warns("add", member, ctx.author, arg)

		await ctx.send(
			f"Предупреждение пользователю {member.display_name} с причиной {arg} успешно выдано! (ID предупреждения - `{ids}`)")

	@commands.command(
		aliases=[
			"снятьпред",
			"снятьварн"
			"Unwarn"],
		description="Снять предупреждение юзеру",
		usage="снятьпред <ID варна>")
	@commands.has_permissions(
		kick_members=True
	)
	async def unwarn(self, ctx, ids: int):
		DB.Set().warns("remove", None, ids, None)
		unwarn_embed = discord.Embed(
			description=f"Варн, уникальный номер которого: `{ids}` был успешно снят!",
			color=0xa400fc)

		unwarn_embed.set_footer(
			text='Valera#0077 © | Все права защищены',
			icon_url='https://cdn.discordapp.com/avatars/342317507991961602/1b8f564f9ec30dd29513a3ca1cf77673.webp?size=1024')
		await ctx.send(embed=unwarn_embed)

	@unwarn.error
	async def unwarn_error(self, ctx, error):

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(embed=discord.Embed(
				description=f'❗️ {ctx.author.name}, обязательно укажите уникальный номер варна!',
				color=0xa400fc))

	@commands.command(
		aliases=[
			"преды",
			"варны",
			"Warns"
		],
		description="Просмотреть предупреждения юзера",
		usage="преды [юзер]"
	)
	async def warns(self, ctx, member: discord.Member = None):
		if not member:
			member = ctx.author

		a = []

		for i in DB.Get().warns(member):
			a.append(f"`ID - {i[0]}` | Модератор - {ctx.guild.get_member(int(i[2]))} | Причина - {i[3]}\n")

		if not a:
			a = ["Юзер не имеет варнов"]

		embed = discord.Embed(
			title=f"Варны {member.display_name}",
			description="".join(a),
			color=0xa400fc
		)

		embed.set_footer(
			text='Valera#0077 © | Все права защищены',
			icon_url='https://cdn.discordapp.com/avatars/342317507991961602/1b8f564f9ec30dd29513a3ca1cf77673.webp?size=1024'
		)
		embed.set_thumbnail(url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	# <!-- Бан -->
	@commands.command(aliases=["Бан", "бан", "Ban"], description="Забанить юзера", usage="бан <юзер>")
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member, *, reason=None):
		if member == ctx.message.author:
			return await ctx.send("Ты не можешь забанить сам себя.")

		msgg = f'Пользователь: {member.mention}, забанен по причине: `{reason}`.'
		msgdm = f'Вы были забанены на сервере {ctx.guild.name}, по причине: `{reason}`.'

		if not reason:
			msgdm = f'Вы были забанены на сервере : {ctx.guild.name}.'
			msgg = f'Пользователь: {member.mention}, забанен.'
			reason = "Не указанна"

		await member.ban(reason=f"Модератор {ctx.author.name}, по причине {reason}")
		await ctx.send(msgg)
		await member.send(msgdm)

	# <!-- Разбан -->
	@commands.command(aliases=["разбан", "Разбан", "Unban"], description="Разбанить юзера", usage="разбан <юзер>")
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx, member: discord.User):
		banned_users = await ctx.guild.bans()

		for ban_entry in banned_users:
			user = ban_entry.banned_users

			if user.id == member.id:
				await ctx.guild.unban(user)
				await ctx.send(f'Пользователь: {user.name}, разбанен.')
				break

	# <!-- Обработка ошибок бана -->
	@ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(
				embed=discord.Embed(description=f'❗️ {ctx.author.name},обязательно укажите юзера'))



	@commands.command(aliases=["кик", "Кик", "Kick"], description="Кикнуть юзера", usage="kick <юзер> [причина]")
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		if member == ctx.message.author:
			return await ctx.send("Ты не можешь кикнуть сам себя.")

		msgg = f'Пользователь : {member.mention}, кикнут по причине : {reason}.'
		msgdm = f'Вы были забанены на сервере {ctx.guild.name}, по причине : {reason}.'

		if not reason:
			msgdm = f'Вы были кикнуты с сервера : {ctx.guild.name}.'
			msgg = f'Пользователь : {member.mention}, кикнут.'
			reason = "Не указанна"

		await member.kick(reason=f"Модератор {ctx.author.name}, по причине {reason}")
		await ctx.send(msgg)
		await member.send(msgdm)

	# <!-- Обработка ошибок кика -->
	@kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(
				embed=discord.Embed(description=f'❗️ {ctx.author.name},обязательно укажите юзера'))


def setup(client):
	client.add_cog(Moder(client))
	print("[SplashBot] Ког: Модерация. Загружен")