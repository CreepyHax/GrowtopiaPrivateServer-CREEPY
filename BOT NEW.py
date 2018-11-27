print ("Updating Bot File")
print ("Updating Command Bot")
print ("Successfully 2 success 0 error")
print ("Welcome Back, CreepyHax")
print (" ")

import discord
from discord.ext import commands
import asyncio
discord.__version__
'1.0.0a'
 
bot = commands.Bot(command_prefix='.')
 
@bot.event
async def on_ready():
    print ('Actived Bot Has Online')
    print ('Bot.Py Started!')
    print (bot.user.id)
    print (bot.user.name)

@bot.command()
async def hi():
	await bot.say ('Hello im a bot created by CreepyHax#8039')
	
@bot.command()
async def pingwifi():
	await bot.say ('Ping Wifi `20ms`')
	await bot.say ('Ping Wifi `64ms`')
	await bot.say ('Ping Wifi `33ms`')
	await bot.say ('Ping Wifi `12ms`')
	await bot.say ('Ping Wifi `30ms`')
	await bot.say ('Ping Wifi `84ms`')
	await bot.say ('Ping Wifi `153ms`')
	await bot.say ('Ping Wifi `19ms`')
	await bot.say ('Test Ping Successfully')

@bot.command()
async def hater():
	await bot.say ('NabzGT `noob`')
	await bot.say ('NabzGT `racist`')
	await bot.say ('NabzGT `abuser`')
	await bot.say ('NabzGT `never pro`')
	await bot.say ('NabzGT ` 100% gay`')
	await bot.say ('NabzGT `fk`')
	await bot.say ('do .hater2 for more')

@bot.command()
async def hater2():
	await bot.say ('raiterjaki `ddos noob`')
	await bot.say ('raiterjaki is `kids`')
	await bot.say ('raiterjaki `no have brain!`')
	await bot.say ('raiterjaki is `100% GAY`')
	await bot.say ('raiterjaki `will got demote by 1337 when online`')
	await bot.say ('do .hater3 Last Command')

@bot.command()
async def hater3():
	await bot.say ('NabzGT & raiterjaki is')
	await bot.say ('GOT DEMOTE WHEN 1337 ONLINE')

@bot.command()
async def mcc():
	await bot.say ('Meow,Coco IS BEST FRIEND I TRUSTED HIM!')

@bot.command()
async def pornhub():
	await bot.say ('You Dont Have Permission To Use This Command!')

@bot.command()
async def bestfriend():
	await bot.say ('Best Friend `Coco, Meow, CreepyHax`')

@bot.command()
async def bestbot():
	await bot.say ('`Coco BOT` Is Best Bot')
	await bot.say ('`CreepyHax BOT` Is Beginner Bot')

@bot.command()
async def kickme():
	await bot.say ('really you want kick you self? i can kick you from This Discord Group')

bot.remove_command('help')

# Help


@bot.command(pass_context=True)


async def help(ctx):


    embed = discord.Embed(title="BOT commands!, prefix is (.) ", description="Working", color=0xD1F1EA)
    
    embed.add_field(name="Public Command", value="`pornhub, hater, hater2, hater3, bestfriend, kickme, bestbot, mcc, hi`")

    embed.add_field(name="New Commands", value="`hater, hater2, hater3, mcc`")

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/516489615872360454/516489663117131787/creepygam.jpg")


    await bot.say(embed=embed)
    
@bot.command()
async def say(*args):
        output = ''
        for word in args:
            output += word
            output += ' '
        await bot.say(output)

@bot.command(pass_context=True)
async def serverinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

 
bot.run("NTE1NDgzNTg2MjUwNTM5MDEz.Dtoulg.8que2jZvJTWaLmjrZ9Or8W27RdE")