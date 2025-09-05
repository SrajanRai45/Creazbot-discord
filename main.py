#app id: 1347970262003617792
#public key: face9d8bbaba67cec4d1147d82891beec2f914723bf511e8d56896e2af8a2012


import discord
from response import getval
from discord.ext import commands

with open('token.txt' , 'r') as token_file:
    token = token_file.readline()


intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '/' , intents = intents)

#commands
@bot.command()
async def getdata(ctx: commands.context , *msg):
    await ctx.send(getval(' '.join(msg)))


bot.run(token)
