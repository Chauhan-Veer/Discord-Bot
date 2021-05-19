from logging import Manager
import discord
from discord import client
from discord import channel
from discord.ext import commands
from discord.ext.commands.core import has_permissions, has_role
from requests.api import get
from discord import DMChannel
import requests
import json
import re
from GoogleNews import GoogleNews
from bs4.element import ResultSet



bot = commands.Bot(command_prefix='!')

#removing commands
bot.remove_command("help")



#get google news data
googlenews = GoogleNews()
googlenews.search('computers')

result = googlenews.gettext()



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
@commands.has_permissions(administrator=True)
async def warn(ctx, *, user: discord.Member = None):
    await ctx.send(f"``▏you have been warned`` {user.mention}")
    await user.send(f"``▏``you have been warned`` {user.mention}")

# give role 
@bot.command()
async def addrole(ctx, role: discord.Role , user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.add_roles(role)  
        await ctx.send(f"▏``Successfully give`` {role.mention} ``Role to`` {user.mention} ")


@bot.command()
async def remove(ctx, role:discord.Role, user: discord.Member):
        await user.remove_roles(role)
        await ctx.send(f"``▏Successfully remove`` {role.mention} ``Role to`` {user.mention}")



#help
helpvar = [
    "type !inspire",
    "type !ping"
]

@bot.command()
async def help(ctx):
    await ctx.send(helpvar)

bot.run('ODQzNTUwMTk3NTU5NTkwOTMz.YKFfVw.sfK80g0CsLwGyFWGV3p0FX4hl5c')