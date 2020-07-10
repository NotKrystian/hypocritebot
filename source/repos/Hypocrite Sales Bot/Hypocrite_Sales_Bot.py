# Work with Python 3.6
import discord
from discord.ext import commands

TOKEN = 'NzMwNzYyMjMzMzYxMjAzMjc3.XwcOfA.VFRki0DHmiZuciMBB5BMDVuV2QE'


client = discord.Client()

bot = commands.Bot(command_prefix='>')

@bot.command()
async def test(ctx):
    await ctx.send('Making Order')
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
@commands.has_role('owner')
async def stop(ctx):
    await ctx.send('[ - ] Stopping Bot...')
    await ctx.send('[ - ] Bot Offline.')
    await bot.close()

@bot.command()
async def say(ctx, msg):
    await ctx.send(msg)

@bot.command()
async def sayc(ctx, channel : int, msg):
    channel = bot.get_channel(channel)
    await channel.send(msg)

@bot.command()
async def cmds(ctx):
    await ctx.send('**Command List :**')
    await ctx.send('help : Displays all commands avaliable')
    await ctx.send('say : Bot says whatever is said after the prefix e.g say "hi guys"')
    await ctx.send('stop : Only accessible by owner rank - Stops bot.')
    await ctx.send('buy <days> : Shows link to product - useable values : 1,3,7,30,999')

@bot.command()
async def buy(ctx, days):
    if(days == '1'):
        await ctx.send('**BUY 1D KEYS HERE : https://shoppy.gg/product/gVD1XJz**')
    if(days == '3'):
        await ctx.send('**BUY 3D KEYS HERE : https://shoppy.gg/product/wq9SXWj**')
    if(days == '7'):
        await ctx.send('**BUY WEEK KEYS HERE : https://shoppy.gg/product/ddQPEaV**')
    if(days == '30'):
        await ctx.send('**BUY MONTH KEYS HERE : https://shoppy.gg/product/QREpG36**')
    if(days == '999'):
        await ctx.send('**BUY LIFETIME KEYS HERE : https://shoppy.gg/product/cY1Vx9R**')
    else:
        await ctx.send('**Usage : >buy <days> [1,3,7,30,999]**')



@bot.command()
async def resell(ctx):
    await ctx.send('**To resell the spoofer please contact NotKrystian**')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    channel = bot.get_channel(727599929601818735)
    await channel.send('[ + ] Initialised Bot.\n[ + ] Logged In.')

    

bot.run(TOKEN)
