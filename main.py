from functools import update_wrapper
import discord
from discord import client
from discord import channel
from discord import user
from discord import member
from discord import message
from discord import guild
from discord import mentions
from discord.ext import commands
from discord.ext.commands.core import has_permissions, has_role
from discord.ext.commands.errors import ExpectedClosingQuoteError
from requests.api import get
from discord import DMChannel
import requests
import json 
import re
from GoogleNews import GoogleNews
from bs4.element import ResultSet

#import libarari 
import json
import os

bot = commands.Bot(command_prefix='!')

#removing commands
bot.remove_command("help")



#get google news data
googlenews = GoogleNews()
googlenews.search('computers')

resutl = googlenews.gettext()



#get quote code data
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" +json_data[0] ['a']
    return quote

#quote code
@bot.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.channel.send(quote)

bot.warnings = {} # guild_id : {member_id: [count, [(admin_id, reason)]]}
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong {round (bot.latency * 1000)} ms")



@bot.event
async def on_ready():
    print("Bot is live")
    
@bot.command()
async def hello(ctx):
    await ctx.send(f"hello, {ctx.author.mention}")

@bot.command()
async def news(ctx):
    await ctx.send(resutl)


@bot.command(pass_context=True)
async def warn(ctx, *, user: discord.Member = None):
    if ctx.author.guild_permissions.administrator:
        await ctx.send(f"``▏you have been warned`` {user.mention}")
        await user.send(f"``▏``you have been warned`` {user.mention}")
    else:
        await ctx.send("you dont have permissions to use this command")

# give role 
@bot.command()
async def addrole(ctx, role: discord.Role , user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.add_roles(role)  
        await ctx.send(f"▏``Successfully give`` {role.mention} ``Role to`` {user.mention} ")
    else:
        await ctx.send("you dont have permissions to use this command")

# remove role
@bot.command()
async def remove(ctx, role:discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.remove_roles(role)
        await ctx.send(f"``▏Successfully remove`` {role.mention} ``Role to`` {user.mention}")
    else:
        await ctx.send("you dont have permission to use this command")


# kick member
@bot.command()
async def kick( ctx, user: discord.Member,*, reason=None):
    if ctx.author.guild_permissions.administrator:
        await user.kick(reason=reason)
        await ctx.send(f"{user.mention} has been removed")
    else: 
        await ctx.send(f"you dont have permissions to use this command")
    

#leveling system
@bot.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)


@bot.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    await client.process_commands(message)


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end

@bot.command()
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'You are at level {lvl}!')
    else:
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'{member} is at level {lvl}!')


#help
helpvar = [
    "type !inspire",
    "type !ping",
    "type !hello"
]

@bot.command()
async def help(ctx):
    await ctx.send(helpvar)

bot.run('ODQzNTUwMTk3NTU5NTkwOTMz.YKFfVw.sfK80g0CsLwGyFWGV3p0FX4hl5c')