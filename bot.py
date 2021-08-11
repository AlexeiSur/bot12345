import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord import Activity, ActivityType, role

bot = commands.Bot(command_prefix="~")

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def info_player(ctx,member:discord.Member):
    emb = discord.Embed(title='Информация о пользователе',color=0xff0000)
    emb.add_field(name="Когда присоединился:",value=member.joined_at,inline=False)
    emb.add_field(name='Имя:',value=member.display_name,inline=False)
    emb.add_field(name='Айди:',value=member.id,inline=False)
    emb.add_field(name="Аккаунт был создан:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Вызвано:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command(pass_context=True)
@commands.has_permissions(view_audit_log=True)
async def ban(ctx,member:discord.Member,reason):
    channel = bot.get_channel(744584045807271989)
    emb = discord.Embed(title="Кик",color=0xff0000)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Нарушитель',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    await member.ban()
    await channel.send(embed = emb)


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx,member:discord.Member,reason):
    channel = bot.get_channel(744584045807271989)
    emb = discord.Embed(title="Кик", color=0xff0000)
    emb.add_field(name='Модератор', value=ctx.message.author.mention, inline=False)
    emb.add_field(name='Нарушитель', value=member.mention, inline=False)
    emb.add_field(name='Причина', value=reason, inline=False)
    await member.kick()
    await channel.send(embed = emb)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx,amount=10):
    await ctx.message.channel.purge(limit=amount + 1)
    await ctx.send(f'Успешно удалено {amount} сообщений')

@bot.command(pass_context=True)
async def info(ctx):
    await ctx.send('~ban [Ник] [Причина]\n~mute [Ник] [Время в минутах] [Причина]\n~unmute [Ник]\n~kick [Ник] [Причина]\n~clear [Количество сообщений]\n~info_player')

@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx,member:discord.Member,time:int,*,reason=None):
    guild = ctx.guild
    muterole = discord.utils.get(guild.roles,id=765555149879771157)
    await member.add_roles(muterole,reason=reason)
    await ctx.send(f'{member} замьючен на {time} минут за {reason}')
    await member.send(f'Ты замьючен на {guild.name} за {reason} на {time} минут.')
    await asyncio.sleep(time*60)
    await member.remove_roles(muterole)

@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx,member:discord.Member):
    guild = ctx.guild
    muterole = discord.utils.get(guild.roles,id=765555149879771157)
    await member.remove_roles(muterole)
    await ctx.send(f"C {member} досрочно снят мут")
    await member.send(f'Тебя досрочно размутили на {guild.name}')


@bot.event
async def on_ready():
    print("ready")


token = ("gWOTALu1B6n4lOAOpdIDkzQt1leLChEh")
# os.environ.get("BOT_TOKEN")

bot.run(token)
bot.run('gWOTALu1B6n4lOAOpdIDkzQt1leLChEh')