import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="~")


@bot.event
async def on_ready():
    print("ready")
    while True:
        await asyncio.sleep(10)
        with open("any_name.txt","r+") as file:
            file.truncate(0)
@bot.event
async def on_message(message):
    counter = 0
    with open("any_name.txt", "r+") as file:
        for lines in file:
            if lines.strip("\n") == str(message.author.id):
                counter+=1
        file.writelines(f"{str(message.author.id)}\n")
        if counter > 5:
            await message.guild.ban(message.author, reason="Спам")
            await asyncio.sleep(1)
            await message.guild.unban(message.author)
            print("Упс")
token = os.environ.get("BOT_TOKEN")
bot.run(token)